from __future__ import print_function

import grpc

import cameramap_pb2
import cameramap_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = cameramap_pb2_grpc.CameramapStub(channel)

    response = stub.SayHello(cameramap_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
