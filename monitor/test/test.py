#encoding=utf-8
# __author__ = 'johnny'
import sys
import os
import psutil
import re
# info = psutil.cpu_times()
# # user = psutil.cpu_times().system
# user = psutil.cpu_count()
# # for x in range(3):
# print user
# print "-------------------------------------------"
# print info
info = psutil.cpu_times()
print info
a = str(info)
out = a.find("idle")
print out
result =  a[out : len(a) - 1]
print result
search_out = re.compile(r'idle\s*=\s*(\d+)')
xx = search_out.search(result)
if xx != None:
    print float(xx.group(1))