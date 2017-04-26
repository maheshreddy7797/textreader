FROM ubuntu
RUN apt-get update
RUN apt-get -y install python3
RUN python3 -V

ADD . /code
WORKDIR /code

CMD ["python3","pyread.py"]
