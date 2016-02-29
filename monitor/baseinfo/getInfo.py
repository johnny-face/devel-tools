#encoding=utf-8
# __author__ = 'johnny'
#This script is get the system info exp CPU Men Disk &
#2016/24/02
import psutil
import re
import subprocess
import socket
import ConfigParser

class BaseInfo(object):
    def __init__(self):
        pass

    #Memory rate
    def getMen(self):
        totalMen = float(psutil.virtual_memory().total/1024/1024)
        useMen = float(psutil.virtual_memory().used/1024/1024)
        usedMen = int(useMen/totalMen * 100)
        return usedMen

    #CPU rate
    def getCpu(self):
        idle = "idle"
        logicalCpu = psutil.cpu_count()
        cpuInfo = psutil.cpu_times_percent(interval=1, percpu=False)
        sCpuInfo = str(cpuInfo)
        user_result = sCpuInfo.find(idle)
        strResult =  sCpuInfo[user_result : len(sCpuInfo) - 1]
        search_out = re.compile(r''+ idle +'\s*=\s*(\d+)')
        use_rate = search_out.search(strResult)
        if use_rate != None:
            return int(use_rate.group(1))


    #Disk rate
    def getDisk(self, path):
        diskUse = psutil.disk_usage(path)
        use_Rate = int(float(diskUse.free) / float(diskUse.total) * 100)
        return use_Rate

    #conf file resolve
    def getResolve(self, module, items):
        configParser = ConfigParser.ConfigParser()
        configParser.read("info.conf")
        getPath = configParser.get(module, items)
        return getPath

    #Host info
    def hostInfo(self):
        hostname = socket.gethostname()
        ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
        ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        ip_pattern = re.compile('(inet addr:%s)' % ipstr)
        pattern = re.compile(ipstr)
        iplist = []
        for ipaddr in re.finditer(ip_pattern, str(output)):
            ip = pattern.search(ipaddr.group())
            if ip.group() != "127.0.0.1":
                iplist.append(ip.group())
        return hostname, iplist