#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function

import grpc

import api_pb2_grpc
import api_pb2


def test_heartpacket(stub):

    heart = api_pb2.HeartPacket()
    heart.devid = "hunan-hukungaosu-xiangtanbeizhan-3"
    heart.htype = "2"
    heart.ver = "123"

    response = stub.HeartPacketRpc(heart)
    print("heartpacket client received: " + response.rcode)


def test_monitorweightdata(stub):

    mdata = api_pb2.MonitorWeightData()
    mdata.devid = "hunan-hukungaosu-xiangtanbeizhan-3"
    mdata.weightype = "1"
    mdata.weight = 1000
    mdata.modeweight = 0
    mdata.chargeweight = 0
    mdata.speed = 5.5

    for i in range(2):
        ainfo = mdata.ainfo.add()
        ainfo.aw = 100
        ainfo.av = 5.5

    for i in range(12):
        sinfo = mdata.sinfo
        sinfo.append("1")

    response = stub.MonitorWeightDataRpc(mdata)
    print("monitorweightdata client received: " + response.rcode)


def test_monitorsensorwavedata(stub):

    mdata = api_pb2.MonitorSensorWaveData()
    mdata.devid = "hunan-hukungaosu-xiangtanbeizhan-3"

    for i in range(12):
        svalue = mdata.svalue
        svalue.append("10234")

    response = stub.MonitorSensorWaveDataRpc(mdata)
    print("monitorsensorwavedata client received: " + response.rcode)


def test_monitordevstatusdata(stub):

    mdata = api_pb2.MonitorDevStatusData()
    mdata.devid = "hunan-hukungaosu-xiangtanbeizhan-3"
    mdata.weightype = "1"
    mdata.light = "1"
    mdata.axlecheckup = "1"
    mdata.axlecheckdown = "1"

    for i in range(12):
        sinfo = mdata.sinfo
        sinfo.append("1")

    response = stub.MonitorDevStatusDataRpc(mdata)
    print("monitordevstatusdata client received: " + response.rcode)


def run():

    channel = grpc.insecure_channel('localhost:9000')
    stub = api_pb2_grpc.StoreDataStub(channel)

    test_heartpacket(stub)
    test_monitorweightdata(stub)
    test_monitorsensorwavedata(stub)
    test_monitordevstatusdata(stub)


if __name__ == '__main__':

    run()
