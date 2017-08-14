from __future__ import print_function

import grpc

import cameramap_pb2
import cameramap_pb2_grpc
import json




def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = cameramap_pb2_grpc.CameramapStub(channel)
    dictt = {'api': 'douban_movie', 'domain': 'movie', 'time': '163ms'}
    
    s1 = cameramap_pb2.ResData(name ="haha", rating = 9.9, year = "2017") 
    s2 = cameramap_pb2.ResData(name ="haha1", rating = 9.99, year = "2017") 
    # it is allowed for the following way
    tmp={}
    tmp["name"]="haha2"
    tmp["rating"] = 9.342
    tmp["year"]="2017"

    s = []
    s.append(s1)
    s.append(s2)
    s.append(tmp)

    
    hq = cameramap_pb2.HelloRequest(mapfield=dictt, res=s)
    response = stub.SayHello(hq)
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
