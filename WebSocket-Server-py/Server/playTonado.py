#!/usr/bin/python2.7
# coding=utf-8
'''
Created on 20170924

@author: WLX
'''
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    '''
    classdocs
    '''

    def get(self):
        self.write("start")


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
