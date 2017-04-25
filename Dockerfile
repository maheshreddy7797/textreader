FROM ubuntu
RUN apt-get update
RUN apt-get -y install python3
RUN python3 -V
WORKDIR /hdatabse
ADD . /database
CMD ["python3","readtext.py"]
