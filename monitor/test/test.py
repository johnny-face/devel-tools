#encoding=utf-8
# __author__ = 'johnny'
import sys
import os
import psutil
import socket

disk = psutil.disk_usage("/")
used = int(float(disk.free) / float(disk.total) * 100)
x = disk.free
y = disk.total
print x
print y
print used
s = socket.gethostname()
print s
# cf = ConfigParser.ConfigParser()
# cf.read("test.cfg")
# s = cf.sections()
# print s
# o = cf.options("db")
# print o
# key = cf.items("db")
# print key
# key1 = cf.get("db", "db_host")
# print key1
# info = psutil.cpu_times()
# # user = psutil.cpu_times().system
# user = psutil.cpu_count()
# # for x in range(3):
# print user
# print "-------------------------------------------"
# print info
# info = psutil.cpu_times()
# print info
# a = str(info)
# out = a.find("idle")
# print out
# result =  a[out : len(a) - 1]
# print result
# search_out = re.compile(r'idle\s*=\s*(\d+)')
# xx = search_out.search(result)
# if xx != None:
#     print float(xx.group(1))