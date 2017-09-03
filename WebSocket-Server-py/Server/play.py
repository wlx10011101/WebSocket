#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Sep 2, 2017

@author: wlx
'''
from bottle import route, run, request, response
import bottle
import json
import logging

from customer.data import shapeData


shapeDataHandler = shapeData()


@route('/tetris', method='get')
def getShapeData():
    response.content_type = 'application/json; charset=utf-8'
    return json.dumps(shapeDataHandler.get(int(request.params.get('id'))))


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
    run(host='0.0.0.0', port=3035, debug=logging.DEBUG)