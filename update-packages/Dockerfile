FROM python:3.8.3

RUN apt-get update -y
RUN pip install -U pip pipenv
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
