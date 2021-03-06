#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Sep 2, 2017

@author: wlx
'''


import json
import logging
import re

from bottle import route, run, request, response
import bottle
from bottle_websocket.plugin import websocket
from bottle_websocket.server import GeventWebSocketServer

from customer.data import shapeData


shapeDataHandler = shapeData()
registryWebsocket = {}


@route('/tetris', method='get')
def getShapeData():
    response.content_type = 'application/json; charset=utf-8'
    return json.dumps(shapeDataHandler.get(int(request.params.get('id'))))


@route('/websocket', apply=[websocket])
def communication(ws):
    while True:
        msg = ws.receive()
        if msg is not None:
            if re.search("registerWebsocket", msg):
                register(ws)
            else:
                print ws, msg
                send_msg_to_other_websocket(ws, msg)
        else:
            print msg


def send_msg_to_other_websocket(ws, msg):
    print ws, msg
    for _, websocket in registryWebsocket.items():
        if websocket != ws:
            websocket.send(msg)


def register(ws):
    wsKey = (ws.environ.get('SERVER_NAME'), ws.environ.get('REMOTE_PORT'))
    if wsKey not in registryWebsocket.keys():
        registryWebsocket.update({wsKey: ws})
        print "register", wsKey


@route('/websocketRegistery', apply=[websocket])
def socketRegister(ws):
    msg = ws.receive()
    print dir(ws)


@route('/')
def ret():
    return bottle.static_file('index.html', root='../public/')


@route('/static/css/<filename>')
def static_css_files(filename):
    return bottle.static_file(filename, root='../public/css/')


@route('/static/js/<filename>')
def static_js_files(filename):
    return bottle.static_file(filename, root='../public/js/')

if __name__ == "__main__":
    run(host='0.0.0.0', port=8888, debug=logging.DEBUG, server=GeventWebSocketServer)
