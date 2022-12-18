FROM python:3.10
USER root
WORKDIR /tmp

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt \
&&  rm -f /tmp/requirements.txt

RUN pip install \
    /tmp/build/*  \
&&  rm -rf /tmp/build

EXPOSE 4096

CMD ["uvicorn", "kaiyuanshe_werobot.__main__:app", "--port", "4096"]