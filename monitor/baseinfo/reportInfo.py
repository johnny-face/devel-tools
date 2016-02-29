#__author__ = 'Johnny'
#The script is report the base info
#2016/02/29
import getInfo
import processInfo


class ReportInfo(object):
    def __init__(self):
        pass

    def mailReport(self):
        info = getInfo.BaseInfo()
        process = processInfo.ProcessInfo()
        hostinfo = info.hostInfo()
        for x in hostinfo:
            print x
        rate = process.monitorInfo()
        print rate

if __name__ == "__main__":
    r = ReportInfo()
    r.mailReport()