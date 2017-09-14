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
    ws1.send("registerWebsocket")
    while True:
        msg = ws1.recv_data()
        if len(msg):
            print msg
