#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function

import grpc

import hello_pb2
import hello_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_pb2_grpc.GreeterStub(channel)

    request = hello_pb2.RequestInfo()
    request.mtype = hello_pb2.HEART
    request.heart.devid = "xxxx-xxxx"
    request.heart.ver = "xxx"

    response = stub.SayHello(request)
    print("Greeter client received: " + str(response.rcode))


if __name__ == '__main__':
    run()
