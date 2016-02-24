#encoding=utf-8
# __author__ = 'johnny'
import sys
import os
import psutil
info = psutil.cpu_times()
# user = psutil.cpu_times().system
user = psutil.cpu_count()
print user
print "-------------------------------------------"
print info