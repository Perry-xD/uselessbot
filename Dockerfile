FROM python:3.9.6-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN python3.9 -m pip install -U pip
COPY .
WORKDIR .
RUN python3.9 -m pip install -U -r requirements.txt
CMD ["bash", "badhiya"]
