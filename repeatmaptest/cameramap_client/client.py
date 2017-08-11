from __future__ import print_function

import grpc

import cameramap_pb2
import cameramap_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = cameramap_pb2_grpc.CameramapStub(channel)
    data =[]
    data.append({'Name': 'Zara', 'Age': '7', 'Class': 'First'})
    data.append({'Name': 'Zara1', 'Age': '71', 'Class': 'First1'})
    dictt = {"data":str(data)}

    #a = [{'Name': 'Zara', 'Age': '7', 'Class': 'First'}, {'Name': 'Zara1', 'Age': '71', 'Class': 'First1'}]
    
    # changing list to a string
    #dictt["list"] = str(listt)
    response = stub.SayHello(cameramap_pb2.HelloRequest(mapfield=dictt))
    #response = stub.SayHello(bb)
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
