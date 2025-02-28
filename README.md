# Liferay Client Extensions Extra Samples

Unofficial additional client extensions samples to complete the official samples that are mirrored
in [this repository](https://github.com/lgdd/liferay-client-extensions-samples).

## Usage

You can clone this repository under the `/client-extensions` directory of a Liferay workspace

Or you can clone this repository and directly use `docker compose up --build` to try those extra
samples.

## The samples

| **Name**           | **Port** | **Description**                                                                                                         | **Language**   |
|--------------------|----------|-------------------------------------------------------------------------------------------------------------------------|----------------|
| etc-golang         | 8126     | Go microservice using the built-in HTTP server package and [lestrrat-go/jwx](https://github.com/lestrrat-go/jwx)        | Go >= 1.24     |
| etc-python-fastapi | 8502     | Python microservice using [FastAPI](https://fastapi.tiangolo.com/) and [PyJWT](https://pyjwt.readthedocs.io/en/stable/) | Python >= 3.10 |
| etc-java-vertx     | 8082     | Java microservice using [Eclipse Vert.x](https://vertx.io/)                                                             | Java >= 21     |