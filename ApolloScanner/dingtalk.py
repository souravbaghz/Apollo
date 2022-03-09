import json
import requests
from Configuration.models import Configuration


class ImNotice:
    """即时通讯工具消息推送基类"""
    def __init__(self, token):
        self.im_token = token
        self.data_post = None
        self.send_url = None
        self.header = {'Content-Type': 'application/json'}


class DingTalkNotice(ImNotice):
    """钉钉推送类"""
    def __init__(self):
        self.token = Configuration.objects.filter(name="2").values_list("value")[0][0]
        super().__init__(self.token)
        self.send_url = "https://oapi.dingtalk.com/robot/send?access_token=" + self.im_token
        self.data_post = {
            "msgtype": "text",
            "text": {
                "content": "黑客播报:\n"
            },
            "at": {
                "atMobiles": [],
                "isAtAll": True
            }
        }

    def send(self, message):
        self.data_post["text"]["content"] = "黑客播报:\n" + message
        requests.post(self.send_url, data=json.dumps(self.data_post), headers=self.header)


dingtalker = DingTalkNotice()