from concurrent import futures
import logging

import grpc

import services_pb2
import services_pb2_grpc


class SayHelloService(services_pb2_grpc.SayHelloServiceServicer):

  def Compute(self, request, context):
      increment()
      return services_pb2.SayHelloResponse(responseMsg='{Msg: \"' + request.requestMsg + ' <-> ' + 'Hello from python' + ' -> ' + str(COUNT) + '}')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_SayHelloServiceServicer_to_server(SayHelloService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

COUNT = 0

def increment():
    global COUNT
    COUNT+=1

if __name__ == '__main__':
    logging.basicConfig()
    serve()