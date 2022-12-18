FROM centos/python-310-centos7
USER root
WORKDIR /tmp

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt \
&&  rm -f /tmp/requirements.txt

COPY ./dist/* /tmp/build/

RUN pip install \
    /tmp/build/*  \
&&  rm -rf /tmp/build
