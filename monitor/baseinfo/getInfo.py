#encoding=utf-8
# __author__ = 'johnny'
#This script is get the system info exp CPU Men Disk &
#2015/24/02
import os
import sys
import psutil
import time

class BaseInfo(object):
    def __init__(self):
        pass

    def getMen(self):
        totalMen = float(psutil.virtual_memory().total/1024/1024)
        useMen = float(psutil.virtual_memory().used/1024/1024)
        usedMen = int(useMen/totalMen * 100)
        return usedMen

    def getCpu(self):
        logicalCpu = psutil.cpu_count()


if __name__ == "__main__":
    info = BaseInfo()
    print info.getMen()
