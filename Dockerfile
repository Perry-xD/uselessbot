FROM python:3.10.4-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN python3.10 -m pip install -U pip
COPY .
WORKDIR .
RUN python3.10 -m pip install -U -r requirements.txt
CMD ["bash", "badhiya"]
