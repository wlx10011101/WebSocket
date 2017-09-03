#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Sep 2, 2017

@author: wlx
'''


class BaseCustomer(object):
    '''
    classdocs
    '''

    def __init__(self, uuid):
        '''
        Constructor
        '''
        self._person = uuid
