FROM python:3.8-slim

RUN apt-get -y update \
  && apt-get install -y gettext build-essential python-dev \
  # Cleanup apt cache
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
