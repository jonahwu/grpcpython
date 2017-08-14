from __future__ import print_function

import grpc

import cameramap_pb2
import cameramap_pb2_grpc
import json




def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = cameramap_pb2_grpc.CameramapStub(channel)
    dictt = {'api': 'douban_movie', 'domain': 'movie', 'time': '163ms'}
    listt = {"name":"dragon", "rating":7.8, "year":"2000"}
    listts = []
    listts.append(json.dumps(listt))
    listt1 = {"name":"dragon1", "rating":2.8, "year":"2001"}
    listts.append(json.dumps(listt1))
    response = stub.SayHello(cameramap_pb2.HelloRequest(mapfield=dictt, res=listts))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
