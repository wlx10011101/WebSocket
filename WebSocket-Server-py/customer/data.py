#!/usr/bin/python2.7
# coding=utf-8
'''
Created on Sep 2, 2017

@author: wlx
'''
import random

MAX_RANDOM_NUM = 10


class shapeData(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.shapeList = []
        self.shapeNum = 7
        self.allowGetTime = []
        self.delCount = 0
        self.generate_shape_list()

    def get(self, index):
        trueIndex = index - self.delCount
        while len(self.shapeList) <= trueIndex + 1:
            self.generate_shape_list()
        if self.allowGetTime[trueIndex] > 0:
            returnData = self.shapeList[trueIndex]
            self.allowGetTime[trueIndex] -= 1
        self.clean()
        return returnData

    def clean(self):
        for item in self.allowGetTime:
            if item <= 0:
                index = self.allowGetTime.index(item)
                self.allowGetTime.pop(index)
                self.shapeList.pop(index)
                self.delCount += 1

    def generate_shape_list(self):
        dataList = []
        for _ in range(MAX_RANDOM_NUM):
            dataList.append(random.randint(0, self.shapeNum - 1))
        self.shapeList.append(dataList)
        self.allowGetTime.append(2)
