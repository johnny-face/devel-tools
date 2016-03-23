#__author__ = 'Johnny'
#The script process the base info
#2016/25/02
import getInfo
import ConfigParser

class ProcessInfo(object):
    def __init__(self):
        pass

    def monitorInfo(self):
        info = getInfo.BaseInfo()
        module = "disk"
        use_space = []

        menInfo = info.getMen()
        cpuInfo = info.getCpu()
        resolve = ConfigParser.ConfigParser()
        resolve.read("info.conf")
        disk_conf = resolve.options(module)
        for path in disk_conf:
            diskPath = info.getResolve(module, path)
            disk_use = info.getDisk(diskPath)
            use_space.append(disk_use)

        if cpuInfo >= 20 or menInfo <= 70 or min(use_space) <= 98:
            return False
