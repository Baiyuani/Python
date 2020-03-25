import paramiko
from getpass import getpass
import sys
import threading
import os


class Rcmd:
    def __init__(self, user, port):
        self.user = user
        self.port = port

    def __call__(self, host, passwd=None, cmds=None):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, port=self.port, username=self.user, password=passwd)
        except:
            print('连接失败！')
        stdin, stdout, stderr = ssh.exec_command(cmds)
        out = stdout.read()
        err = stderr.read()
        if out:
            print('[\033[32;1m%s\033[0m] OUT:\n%s' % (host, out.decode()))
        if err:
            print('[\033[31;1m%s\033[0m] ERR:\n%s' % (host, err.decode()))
        ssh.close()


if __name__ == '__main__':
    try:
        fname = sys.argv[1]
        cmds = sys.argv[2]
        passwd = getpass()
    except IndexError:
        print("Usage: %s ipfile 'commands'" % sys.argv[0])
        exit(1)
    except (KeyboardInterrupt, EOFError):
        print('\nexit')
        exit(2)
    if not os.path.exists(fname):
        print('%s : file is not exists' % fname)
        exit(3)

    # 打开文件，文件中的每一行是一个ip地址，取出地址，执行命令
    with open(fname) as fobj:
        for line in fobj:
            ip = line.strip()  # 去除行尾的\n
            t = threading.Thread(target=Rcmd('root', 22), args=(ip, passwd, cmds))
            t.start()
