FROM python:3

ADD . /

RUN pip install pystrich
RUN pip install grpc
RUN pip install flask
RUN pip install flask_restful


CMD [ "python", "./client.py" ]