FROM python:alpine

RUN apk add --update --no-cache openssh-client \
    && rm -rf /var/cache/apk/*

RUN pip install ssh-menu

ENTRYPOINT ["ssh-menu"]