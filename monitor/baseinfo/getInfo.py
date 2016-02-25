#encoding=utf-8
# __author__ = 'johnny'
#This script is get the system info exp CPU Men Disk &
#2015/24/02
import psutil
import re

class BaseInfo(object):
    def __init__(self):
        pass

    #内存使用率
    def getMen(self):
        totalMen = float(psutil.virtual_memory().total/1024/1024)
        useMen = float(psutil.virtual_memory().used/1024/1024)
        usedMen = int(useMen/totalMen * 100)
        return usedMen

    #CPU使用率
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
            return float(use_rate.group(1))


    #Disk使用率
    def getDisk(self):
        print "disk"

if __name__ == "__main__":
    info = BaseInfo()
    print info.getMen()
    print info.getCpu()
