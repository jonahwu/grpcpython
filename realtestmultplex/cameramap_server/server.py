from concurrent import futures
import time
import math

import grpc

import cameramap_pb2
import cameramap_pb2_grpc
import json

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class CameramapServicer(cameramap_pb2_grpc.CameramapServicer):
    def SayHello(self, request, context):
        print request.mapfield
        mapdata = request.mapfield
        print mapdata['api']
        listts =  request.res
        # now it become a list
        print listts
        print '***************************'
        for listt in listts:
            print listt
            print '-------------------'
        return cameramap_pb2.HelloReply(message='Hello, %s!' % request.mapfield)

    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cameramap_pb2_grpc.add_CameramapServicer_to_server(CameramapServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
