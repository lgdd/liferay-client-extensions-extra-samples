![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/lgdd/liferay-client-extensions-extra-samples/build.yml)

# Liferay Client Extensions Extra Samples

Unofficial additional client extensions samples to complete the official samples that are mirrored
in [this repository](https://github.com/lgdd/liferay-client-extensions-samples).

## Usage

**If you want to create one of those samples in your Liferay workspace from a CLI,
checkout [this project](https://github.com/lgdd/lfr-cli).**

You can clone this repository under the `/client-extensions` directory of a Liferay workspace

Or you can clone this repository and directly use `docker compose up --build` to try those extra
samples.

## The samples

| **Name**                     | **Port** | **Description**                                                                                                                                                   | **Language**   |
|------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| sample-custom-element-svelte | _N/A_    | Frontend Custom Element using [Svelte](https://svelte.dev/) and [Vite](https://vite.dev/)                                                                         | JavaScript     |
| sample-custom-element-vue    | _N/A_    | Frontend Custom Element using [Vue.js](https://vuejs.org/) and [Vite](https://vite.dev/)                                                                          | JavaScript     |
| sample-etc-golang            | 8126     | Go microservice using the built-in HTTP server package and [lestrrat-go/jwx](https://github.com/lestrrat-go/jwx)                                                  | Go >= 1.24     |
| sample-etc-python-fastapi    | 8502     | Python microservice using [FastAPI](https://fastapi.tiangolo.com/) and [PyJWT](https://pyjwt.readthedocs.io/en/stable/)                                           | Python >= 3.10 |
| sample-etc-java-vertx        | 8082     | Java microservice using [Eclipse Vert.x](https://vertx.io/)                                                                                                       | Java >= 21     |
| sample-etc-java-quarkus      | 8083     | Java microservice using [Quarkus](https://quarkus.io/), [java-jwt](https://github.com/auth0/java-jwt) and [jwks-rsa-java](https://github.com/auth0/jwks-rsa-java) | Java >= 21     |
| sample-etc-bun               | 8228     | JavaScript microservice using [Bun](https://quarkus.io/) and [panva/jose](https://github.com/panva/jose)                                                          | TypeScript     |