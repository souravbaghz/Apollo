import os
import uuid
import threading
import subprocess
from Work.models import Work
from ExpManager.models import ExpManager

class Scan(threading.Thread):
    def __init__(self, id):
        self.threadname = uuid.uuid1()
        threading.Thread.__init__(self, name=self.threadname)
        self.id = id
    def run(self):
        taskname = Work.objects.filter(id=self.id).values_list("name")[0][0]
        expid = Work.objects.filter(id=self.id).values_list("exp_id")[0][0]
        vulnid = ExpManager.objects.filter(id=expid).values_list("vulnid")[0][0]
        ipaddress = Work.objects.filter(id=self.id).values_list("ipdst")[0][0]
        path = ExpManager.objects.filter(id=expid).values_list("fileobj")[0][0]
        filepath = str(os.getcwd()) + "/" + str(path)
        port = Work.objects.filter(id=self.id).values_list("port")[0][0]
        command_string = ExpManager.objects.filter(id=expid).values_list("command")[0][0]
        command = command_string % (str(filepath), str(self.id), str(taskname), str(vulnid), str(ipaddress), str(port))
        logfile = str(os.getcwd())+"/Work/ScanLogs/%s.txt"%self.threadname
        print(logfile)
        subprocess.Popen(command, stdout=open(logfile, "w"), shell=True)
        #os.system(command)

