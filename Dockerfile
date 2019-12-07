FROM python:3.8.0-buster
RUN apt update && apt upgrade
COPY . /app
WORKDIR /app
RUN apt install -fy firefox-esr
RUN pip3 install -r ./requirements.txt
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz && \
    tar -xvf geckodriver-v0.26.0-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    rm geckodriver*
