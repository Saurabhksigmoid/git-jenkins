From ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt-get install -y python3-psutil

WORKDIR /usr/app/src

COPY code.py ./

CMD [ "python3", "./code.py"]
