FROM ubuntu
RUN apt-get update
RUN apt-get -y install python3
RUN python3 -V
WORKDIR /helloapp
ADD . /helloapp
CMD ["python3","readtext.py"]
