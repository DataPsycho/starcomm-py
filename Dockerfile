FROM python:3.8-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

ENV REPO_URL=StarComm

COPY . $REPO_URL
WORKDIR $REPO_URL

RUN chmod +x gunicorn_starter.sh

EXPOSE 8080
ENTRYPOINT ["./gunicorn_starter.sh"]
