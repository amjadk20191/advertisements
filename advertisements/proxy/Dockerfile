FROM nginx:stable-alpine3.17
LABEL maintainer="localhost"

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

ENV APP_HOST=app
ENV APP_PORT=9000


RUN mkdir -p /vol/static && \
    chown -R nginx:nginx /vol/static && \
    chmod +x /run.sh

VOLUME /vol/static

COPY ./build  /usr/share/nginx/html
COPY ./build/static  /vol/static



CMD ["/run.sh"]