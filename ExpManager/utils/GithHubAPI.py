import github


def Login(token):
    """Login Github with API Token! Return Github Operator Or None!"""
    print("\033[1;32m[+] Start To Login Github!")
    try:
        scanner = github.Github(login_or_token=token)
        print("\033[1;32m[+] Login Success!")
        return scanner
    except Exception as exception:
        print("\033[1;31m[-] Search Failed, Reason:%s" % str(exception))
        return None


def Search_Code(operator, domain, keyword):
    """Search Github with domain and keyword! Return search results Or None!"""
    print("\033[1;32m[+] Start To Search!")
    word = '"%s" %s' % (str(domain), str(keyword))
    result = None
    try:
        result = operator.search_code(word)
        print("\033[1;32m[+] Search Success!")
    except Exception as exception:
        print("\033[1;31m[-] Search Failed, Reason:%s" % str(exception))
        result = None
    return result