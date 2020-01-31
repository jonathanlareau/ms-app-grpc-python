from __future__ import print_function
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps

import logging

import grpc

import services_pb2
import services_pb2_grpc

app = Flask(__name__)
api = Api(app)

class SayHello(Resource):
    def get(self, msg):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = services_pb2_grpc.SayHelloServiceStub(channel)
            response = stub.Compute(services_pb2.SayHiRequest(requestMsg=msg))
        print("Msg received: " + response.responseMsg)
        return response.responseMsg


api.add_resource(SayHello, '/api/sayhello/<msg>') # Route_1

if __name__ == '__main__':
    logging.basicConfig()
    app.run(port='8080')