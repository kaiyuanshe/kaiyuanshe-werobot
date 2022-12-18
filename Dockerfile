FROM python:3.10
USER root
WORKDIR /tmp

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt \
&&  rm -f /tmp/requirements.txt

COPY ./dist/* /tmp/build/

RUN pip install \
    /tmp/build/*  \
&&  rm -rf /tmp/build

EXPOSE 4096

CMD ["uvicorn", "kaiyuanshe_werobot.__main__:app", "--host", "0.0.0.0", "--port", "4096"]