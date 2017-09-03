#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Sep 2, 2017

@author: wlx
'''
from bottle import route
from bottle import run
import bottle
from bottle_websocket.plugin import websocket
from bottle_websocket.server import GeventWebSocketServer


@route('/websocket', apply=[websocket])
def echo(ws):
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send(msg)
        else:
            break


@route('/')
def ret():
    return "welcome websocket server"

if __name__ == "__main__":
    run(host='127.0.0.1', port=8203, server=GeventWebSocketServer)
