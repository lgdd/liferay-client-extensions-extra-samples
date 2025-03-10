FROM azul/zulu-openjdk-alpine:21 AS builder

ENV NPM_CONFIG_PREFIX=/home/liferay/.npm-global
ENV PATH=$PATH:/home/liferay/.npm-global/bin
ENV PATH=$PATH:/home/liferay/.npm-global/lib
ENV NODE_ENV=production

ARG LIFERAY_UID

RUN apk --update --no-cache --repository https://dl-cdn.alpinelinux.org/alpine/v3.20/main/ add \
    curl \
    gcompat \
    nodejs=20.15.1-r0 \
    npm=10.9.1-r0 \
    dos2unix && \
    addgroup -S liferay && \
    adduser -S liferay -G liferay -u ${LIFERAY_UID:-100}

USER liferay
WORKDIR /home/liferay

RUN curl -fsSL https://raw.githubusercontent.com/liferay/liferay-blade-cli/master/cli/installers/local | sh
ENV PATH=$PATH:/home/liferay/jpm/bin
RUN blade init -v dxp-2025.q1.0-lts workspace --refresh-releases

WORKDIR /home/liferay/workspace

COPY --chown=liferay:liferay . client-extensions

RUN ./gradlew initBundle

RUN sed -i -e 's/localhost:8126/sample-etc-golang:8126/g' client-extensions/sample-etc-golang/client-extension.yaml
RUN sed -i -e 's/localhost:8502/sample-etc-python-fastapi:8502/g' client-extensions/sample-etc-python-fastapi/client-extension.yaml
RUN sed -i -e 's/localhost:8082/sample-etc-java-vertx:8082/g' client-extensions/sample-etc-java-vertx/client-extension.yaml
RUN sed -i -e 's/localhost:8083/sample-etc-java-quarkus:8083/g' client-extensions/sample-etc-java-quarkus/client-extension.yaml
RUN sed -i -e 's/localhost:8228/sample-etc-bun:8228/g' client-extensions/sample-etc-bun/client-extension.yaml

RUN ./gradlew clean deploy -PnodeDownload=false

FROM liferay/dxp:2025.q1.0-lts

ENV JAVA_VERSION=zulu21

COPY --chown=liferay:liferay --from=builder /home/liferay/workspace/bundles/osgi/client-extensions /opt/liferay/osgi/client-extensions

HEALTHCHECK --interval=15s --timeout=3s --retries=30 --start-period=30s \
  CMD curl --silent --fail 127.0.0.1:8080/c/portal/robots || exit 1