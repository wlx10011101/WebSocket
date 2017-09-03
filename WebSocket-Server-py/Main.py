#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Sep 2, 2017

@author: wlx
'''
import os
import sys

from websocket._core import create_connection


if __name__ == "__main__":
    ws1 = create_connection("ws://127.0.0.1:3035/websocket")
    ws2 = create_connection("ws://127.0.0.1:3035/websocket")
    print "start"
    ws2.send("start hello world")
    ws1.send("ws1- start hellpo world")
    print "receiving..."
    result2 = ws2.recv()
    result1 = ws1.recv()
    print "result", result2
    print "result1", result1
    os.system("pause")
#     ws2.close()
#     ws1.close()
