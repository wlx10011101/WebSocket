#!/usr/bin/python2.7
# coding=utf-8
'''
Created on 20170924

@author: WLX
'''

import json
import os
import re

import tornado.web

from customer.data import shapeData


shapeDataHandler = shapeData()

settings = {"static_path": os.path.join(os.path.dirname(__file__), "../public")}


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("../public/index.html")


class Shape(tornado.web.RequestHandler):

    def get(self):
        self.add_header('content_type', 'application/json; charset=utf-8')
        self.write(json.dumps(shapeDataHandler.get(int(self.get_argument('id')))))


class StaticFile(tornado.web.RequestHandler):

    def get(self, filename):
        if re.search('.*js', filename):
            self.render_linked_js(filename)
        elif re.search('.*css', filename):
            self.render_linked_css(filename)


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/tetris', Shape),
        (r'/static/(.*)', StaticFile), ],
        **settings
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
