import paramiko


def ssh_brute_scan(address, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(address, int(port), username, password)
        ssh_client.close()
        print(True)
    except Exception as exception:
        ssh_client.close()
        print(exception)
