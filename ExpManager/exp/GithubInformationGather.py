import time
import github
from ..utils.GithHubAPI import Login, Search_Code


class GitHubGather:
    def __init__(self, token, keywords):
        self.scanner = None
        self.token = token
        self.keywords = keywords

    def login(self):
        self.scanner = Login(self.token)

    def search(self):
        results = None
        if self.scanner is not None:
            results = Search_Code(self.scanner, self.keywords)
            while True:
                try:
                    size = results.totalCount
                    print("\033[1;32m[+] We Got %s stuffs!"%str(size))
                    break
                except Exception as exception:
                    if isinstance(exception, github.RateLimitExceededException):
                        print("\033[1;31m[-] Too Fast, We Need Wait For 1 min")
                        time.sleep(60)
                        continue
                    else:
                        print("\033[1;31m[-] Unknown Failed, Reason:%s" % str(exception))
                        return
        index = 0
        if size > 0 and results is not None:
            for result in results:
                try:
                    print("\033[1;32m[Hit] : " + result.html_url)
                    index += 1
                    time.sleep(2)
                except Exception as exception:
                    if isinstance(exception, github.RateLimitExceededException):
                        print("\033[1;31m[-] Too Fast, We Need Wait For 1 min")
                        index += 1
                        time.sleep(60)
                        continue
                    else:
                        print("\033[1;3m[-] Unknown Failed, Reason:%s" % str(exception))
                        index += 1
                        continue
                self.percent.set_description("Processing[%s/%s]"%(str(index), str(size)))


