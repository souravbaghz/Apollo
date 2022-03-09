import sys
import datetime
import threading
from Assets.models import AssetList
from ApolloScanner.dingtalk import dingtalker
from Configuration.models import Configuration
from VulnerableScan.models import ExploitRegister, VulnerableScanTasks, VulnerableScanResult


class ResultStruts:
    def __init__(self, task_id, task_name):
        self.cursor = VulnerableScanResult.objects
        self.result = {
            "task_id": task_id,
            "task_name": task_name,
            "ip_address": None,
            "port": None,
            "result_flag": False,
            "timestamp": None
        }

    def set_date(self):
        self.result["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d")

    def insert(self, address, port, result):
        self.result["ip_address"] = address
        self.result["port"] = int(port)
        self.result["result_flag"] = result
        self.set_date()
        self.cursor.create(**self.result)


class BruteScanner:
    def __init__(self, task_id):
        self.task_name = VulnerableScanTasks.objects.filter(id=task_id).values_list("name")[0][0]
        self.max_thread_count = int(Configuration.objects.filter(name="6").values_list("count")[0][0])
        self.thread_size = 0

        self.exploit_id = VulnerableScanTasks.objects.filter(id=task_id).values_list("exploit")[0][0]
        self.exploit_file = ExploitRegister.objects.filter(id=self.exploit_id).values_list("file_object")[0][0]
        self.exploit_name = ExploitRegister.objects.filter(id=self.exploit_id).values_list("exploit_name")[0][0]
        self.model_name = str(self.exploit_file).replace("/", ".").split(".py")[0]
        function_name = self.model_name.split(".")[-1]
        __import__(self.model_name)
        model = sys.modules[self.model_name]
        self.function = model.__getattribute__(function_name)

        self.targets = str(VulnerableScanTasks.objects.filter(id=task_id).values_list("targets")[0][0]).split(",")
        self.targets = [] if self.targets == [""] else self.targets
        self.target_id = VulnerableScanTasks.objects.filter(id=task_id).values_list("target")[0][0]
        if self.target_id is not None:
            address = AssetList.objects.filter(id=self.target_id).values_list("ip_address")[0][0]
            port = AssetList.objects.filter(id=self.target_id).values_list("port")[0][0]
            self.targets.append("%s:%s" % (address, str(port)))
        self.targets = list(set(self.targets))
        self.cursor = ResultStruts(task_id, self.task_name)

    def verify(self, address, port):
        result = self.function(address, port)
        if result:
            message = "漏洞: %s %s %s\n" % (str(self.exploit_name), address, str(port))
            dingtalker.send(message=message)
            self.cursor.insert(address, port, result)
        self.thread_size -= 1

    def run(self):
        for target in self.targets:
            address, port = target.split(":")
            port = int(port)
            while True:
                if self.thread_size < self.max_thread_count:
                    self.thread_size += 1
                    thread = threading.Thread(target=self.verify, args=(address, int(port),))
                    thread.start()
                    break
                else:
                    continue


def start_scan(task_id):
    scanner = BruteScanner(task_id)
    scanner.run()
