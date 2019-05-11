#!/usr/bin/env python
# -*- coding: utf8 -*-

from concurrent import futures
import time

import grpc

import hello_pb2
import hello_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def handlerdefault(info):

    print "handlerdefault"
    retinfo = hello_pb2.ResonseInfo()
    retinfo.rcode = hello_pb2.SUCCESS
    return retinfo


def handleheart(info):

    print "devid:%s ver:%s" % (info.heart.devid, info.heart.ver)
    retinfo = hello_pb2.ResonseInfo()
    retinfo.rcode = hello_pb2.DEBUG
    return retinfo


def serve():
    # gRPC 服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


# 将消息类型和对应的操作存在dict中，避免过多的if else
handlersfunc = {
    hello_pb2.HEART : handleheart
}


class greeter(hello_pb2_grpc.GreeterServicer):
	# 工作函数
    def SayHello(self, request, context): 
        return handlersfunc.get(request.mtype, handlerdefault)(request)


if __name__ == '__main__':
    serve()