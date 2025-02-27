from fastapi import FastAPI, Header, HTTPException, Request
import json
import jwt
from jwt import PyJWK
import logging
import os
import requests
from typing import Annotated
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()

def get_config():
    config = {}
    dxp_metadata = os.scandir("dxp-metadata")
    for entry in dxp_metadata:
        if entry.is_file():
            file = open(entry.path, "r")
            config[entry.name] = file.read()
    return config

def validate_jwt(token_str, config):
    protocol = config["com.liferay.lxc.dxp.server.protocol"]
    domain = config["com.liferay.lxc.dxp.mainDomain"]
    oauth2_jwks_uri = protocol + "://" + domain + "/o/oauth2/jwks"

    logger.info("JWT: " + token_str)

    jwks_response = requests.get(oauth2_jwks_uri)
    jwk_json = jwks_response.json()["keys"][0]
    jwk_json_str = str(jwk_json).replace("'", "\"")

    alg = jwk_json["alg"]

    project_protocol = os.getenv("PROJECT_PROTOCOL", "http")
    project_hostname = os.getenv("PROJECT_HOSTNAME", "localhost")
    project_port = os.getenv("PROJECT_PORT", "8502")
    aud = project_protocol + "://" + project_hostname + ":" + project_port

    jwk = PyJWK.from_json(jwk_json_str, algorithm=alg)

    return jwt.decode(jwt=token_str, key=jwk, algorithms=[alg], audience=aud)

def validate_client_id(client_id, config):
    protocol = config["com.liferay.lxc.dxp.server.protocol"]
    domain = config["com.liferay.lxc.dxp.mainDomain"]
    external_reference_codes = config["liferay.oauth.application.external.reference.codes"]
    external_reference_code = external_reference_codes.split(",")[0]

    oauth2_app_uri = protocol + "://" + domain + "/o/oauth2/application?externalReferenceCode=" + external_reference_code
    response = requests.get(oauth2_app_uri)

    if response.json()["client_id"] != client_id:
        error_msg = "client id from token and oauth application don't match"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)

@app.get("/ready")
async def ready():
    return "ready"

@app.post("/object/action/1")
async def object_action_1(request: Request, authorization: Annotated[str | None, Header()] = None):
    config = get_config()
    token = authorization.split("Bearer ")[1]

    decoded_token = validate_jwt(token, config)
    validate_client_id(decoded_token["client_id"], config)

    object_entry = await request.json()
    logger.info(object_entry)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8502, log_level="info", reload=True)
