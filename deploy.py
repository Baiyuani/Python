import wget
import os
import requests
import hashlib
import tarfile


def has_new_ver(ver_fname, ver_url):
    '用于判断jenkins服务器是否有新版本软件，有返回True，没有返回False'
    # 如果本地没有版本文件，则有新版本
    if not os.path.isfile(ver_fname):
        return True

    # 如果本地和服务器的版本号不一样，则有新版本
    r = requests.get(ver_url)    # 取出服务器上版本号
    with open(ver_fname) as fobj:
        local_ver = fobj.read()  # 读取本地版本号
    if local_ver != r.text:
        return True
    else:
        return False

def file_ok(fname, md5url):
    '判断下载的软件包是否损坏，未损坏返回True，否则返回False'
    # 计算本地的md5值
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    # 比较网上的md5值和本地的md5值
    r = requests.get(md5url)
    if m.hexdigest() == r.text.strip():  # 删除网上md5值尾部可能存在的\n
        return True
    else:
        return False

def deploy(pkg_fname, deploy_dir, dest):
    '用于部署软件包'
    # 将压缩包解压到deploy目录
    tar = tarfile.open(pkg_fname)
    tar.extractall(path=deploy_dir)
    tar.close()

    # 拼接出解压目录的绝对路径
    app_dir = pkg_url.split('/')[-1]
    app_dir = app_dir.replace('.tar.gz', '')
    app_dir = os.path.join(deploy_dir, app_dir)

    # 如果软链接已存在，先删除，再创建
    if os.path.exists(dest):
        os.remove(dest)
    os.symlink(app_dir, dest)

if __name__ == '__main__':
    # 判断是否有新版本，如果没有新版本则退出
    ver_fname = '/var/www/deploy/live_ver'
    ver_url = 'http://192.168.113.134/deploy/live_ver'
    if not has_new_ver(ver_fname, ver_url):
        print('未发现新版本')
        exit(1)

    # 下载新版本的软件包
    r = requests.get(ver_url)
    pkg_url = 'http://192.168.113.134/deploy/pkgs/myweb-%s.tar.gz' % r.text
    pkg_dir = '/var/www/download'
    wget.download(pkg_url, pkg_dir)

    # 校验下载的软件包是否损坏，如果损坏将其删除
    md5url = pkg_url + '.md5'
    pkg_fname = pkg_url.split('/')[-1]
    pkg_fname = os.path.join(pkg_dir, pkg_fname)
    if not file_ok(pkg_fname, md5url):
        print('文件已损坏')
        os.remove(pkg_fname)
        exit(2)

    # 部署软件包
    dest = '/var/www/html/nsd1910'
    deploy_dir = '/var/www/deploy'
    deploy(pkg_fname, deploy_dir, dest)

    # 更新本地版本文件
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)
