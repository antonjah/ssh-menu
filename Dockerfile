FROM python:alpine

LABEL maintainer="Anton Andersson <contact@antonandersson.se>"

RUN apk add --update --no-cache openssh-client \
    && rm -rf /var/cache/apk/*

RUN pip install ssh-menu

ENTRYPOINT ["python", "/usr/local/bin/sshmenu"]