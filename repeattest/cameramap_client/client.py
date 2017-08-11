from __future__ import print_function

import grpc

import cameramap_pb2
import cameramap_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = cameramap_pb2_grpc.CameramapStub(channel)
    #dictt = {'Name': 'Zara', 'Age': '7', 'Class': 'First'}
    listt = ["1","2","3"]
    # changing list to a string
    #dictt["list"] = str(listt)
    response = stub.SayHello(cameramap_pb2.HelloRequest(datatest=listt))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
