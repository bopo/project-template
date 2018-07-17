FROM alpine:3.8
ENV PYTHONUNBUFFERED 1

RUN echo 'http://mirrors.aliyun.com/alpine/v3.8/main/' > /etc/apk/repositories
RUN echo 'http://mirrors.aliyun.com/alpine/v3.8/community/' >> /etc/apk/repositories

RUN apk add --update python2 python2-dev py-pip py-bcrypt py-cffi
RUN apk add --update gcc g++ git
RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com git+https://github.com/bopo/mock-server.git

RUN mkdir /api

VOLUME /api

WORKDIR /api

CMD ["mock-server", "--address=0.0.0.0", "--dir=.", "--debug"]
