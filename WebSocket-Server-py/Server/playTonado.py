#!/usr/bin/python2.7
# coding=utf-8
'''
Created on 20170924

@author: WLX
'''
import json
import logging
import os
import re
import tornado.web
import tornado.websocket

from customer.data import shapeData


shapeDataHandler = shapeData()

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "../public")
}


class MainHandler(tornado.web.RequestHandler):
    '''
    classdocs
    '''

    def get(self):
        self.render("../public/index.html")


class Shape(tornado.web.RequestHandler):

    def get(self):
        self.add_header('content_type', 'application/json; charset=utf-8')
        return_data = tornado.escape.json_encode(shapeDataHandler.get(int(self.get_argument('id'))))
        self.write(return_data)


class StaticFile(tornado.web.RequestHandler):

    def get(self, filePath):
        if re.search('.*js', filePath):
            self.render_linked_js("../public/{0}".format(filePath))
        elif re.search('.*css', filePath):
            self.render_linked_css("../public/{0}".format(filePath))
        else:
            self.render("../public/{0}".format(filePath))


class Communication(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        logging.debug("socket open")

    def on_message(self, message):
        logging.debug("revice message: ", message)

    def on_close(self):
        logging.debug("socket close")


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/static/(.*)', StaticFile),
        (r'/tetris', Shape),
        (r'/websocket', Communication), ],
        debug=True,
        **settings
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
