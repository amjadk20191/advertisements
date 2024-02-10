FROM python:alpine3.18
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./advertisements/re.txt /tmp/re.txt
COPY ./advertisements/scripts /scripts

COPY ./advertisements /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip 
RUN apk update 
RUN  apk add --update  postgresql-client jpeg-dev 
RUN apk add --update  gcc
RUN apk add --update  --virtual .tmp-build-deps build-base postgresql-dev musl-dev zlib zlib-dev linux-headers

RUN /py/bin/pip install -r /tmp/re.txt

RUN apk add  --update supervisor
RUN apk add  --update python3-dev pcre-dev

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN  rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

        
ENV PATH="/scripts:/py/bin:$PATH"
USER django-user 
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
