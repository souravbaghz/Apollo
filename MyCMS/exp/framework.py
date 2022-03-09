import datetime
from utils import ScanResultInsert


class ExpFrameWork:
    def __init__(self, taskid, taskname, vulnid, ipaddress, port, scanfunc):
        self.taskid = taskid
        self.taskname = taskname
        self.vulnid = vulnid
        self.ipaddress = ipaddress
        self.port = port
        self.scanfunc = scanfunc
        self.result = None
        self.date = None

    def execute(self):
        self.result, self.scanlog = self.scanfunc(self.ipaddress, self.port)
        self.date = str(datetime.date.today())
        ScanResultInsert(self.taskid, self.taskname, self.vulnid, self.scanlog, self.result, self.date, self.ipaddress ,self.port)


class ScanTask:
    def __init__(self, taskid, taskname, expid, ipaddress, port):
        self.ScanTaskID = taskid
        self.ScanTaskName = taskname
        self.ExploitID = expid
        self.ScanTarget = ipaddress
        self.ScanPort = port
        self.ScanResult = 0
        self.ScanDate = None
        self.ScanLog = ""

    def Scan(self):
        pass

    def Run(self):
        self.Scan()
        self.ScanDate = str(datetime.date.today())
        ScanResultInsert(
            self.ScanTaskID,
            self.ScanTaskName,
            self.ExploitID,
            self.ScanLog,
            self.ScanResult,
            self.ScanDate,
            self.ScanTarget,
            self.ScanPort
        )