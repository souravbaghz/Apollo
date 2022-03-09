import sys
import datetime
import threading
from Assets.models import AssetList
from ApolloScanner.settings import BASE_DIR
from Configuration.models import Configuration
from BruteScan.models import BruteRegister, BruteTasks, BruteResult


class ResultStruts:
    def __init__(self, task_id, task_name):
        self.cursor = BruteResult.objects
        self.result = {
            "task_id": task_id,
            "task_name": task_name,
            "ip_address": None,
            "port": None,
            "username": None,
            "password": None,
            "timestamp": None
        }

    def set_date(self):
        self.result["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d")

    def insert(self, address, port, username, password):
        self.result["ip_address"] = address
        self.result["port"] = int(port)
        self.result["username"] = username
        self.result["password"] = password
        self.set_date()
        self.cursor.create(**self.result)


class BruteScanner:
    def __init__(self, task_id):
        self.task_name = BruteTasks.objects.filter(id=task_id).values_list("name")[0][0]
        self.max_thread_count = int(Configuration.objects.filter(name="6").values_list("count")[0][0])
        self.thread_size = 0

        self.username_file = str(BASE_DIR) + "/BruteScan/Dictionary/usernames.txt"
        self.password_file = str(BASE_DIR) + "/BruteScan/Dictionary/passwords.txt"
        self.usernames = []
        self.passwords = []
        for username in open(self.username_file, 'r').readlines():
            username = username.split("\n")[0]
            if username != "":
                self.usernames.append(username)
        for password in open(self.password_file, 'r').readlines():
            password = password.split("\n")[0]
            if password != "":
                self.passwords.append(password)

        self.exploit_id = BruteTasks.objects.filter(id=task_id).values_list("exploit")[0][0]
        self.exploit_file = BruteRegister.objects.filter(id=self.exploit_id).values_list("file_object")[0][0]
        self.model_name = str(self.exploit_file).replace("/", ".").split(".py")[0]
        function_name = self.model_name.split(".")[-1]
        __import__(self.model_name)
        model = sys.modules[self.model_name]
        self.function = model.__getattribute__(function_name)

        self.targets = str(BruteTasks.objects.filter(id=task_id).values_list("targets")[0][0]).split(",")
        self.targets = [] if self.targets == [""] else self.targets
        self.target_id = BruteTasks.objects.filter(id=task_id).values_list("target")[0][0]
        if self.target_id is not None:
            address = AssetList.objects.filter(id=self.target_id).values_list("ip_address")[0][0]
            port = AssetList.objects.filter(id=self.target_id).values_list("port")[0][0]
            self.targets.append("%s:%s" % (address, str(port)))
        self.targets = list(set(self.targets))
        self.cursor = ResultStruts(task_id, self.task_name)

    def verify(self, address, port, username, password):
        result = self.function(address, port, username, password)
        print("RET:" + str(result))
        if result:
            self.cursor.insert(address, port, username, password)
        self.thread_size -= 1

    def run(self):
        for target in self.targets:
            address, port = target.split(":")
            port = int(port)
            for username in self.usernames:
                for password in self.passwords:
                    while True:
                        if self.thread_size < self.max_thread_count:
                            self.thread_size += 1
                            thread = threading.Thread(target=self.verify, args=(address, int(port), username, password, ))
                            thread.start()
                            break
                        else:
                            continue


def scan(task_id):
    scanner = BruteScanner(task_id)
    scanner.run()
