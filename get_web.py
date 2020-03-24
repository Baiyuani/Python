import wget
import os
import re

def get_patt(fname, patt, charset=None):
    result = []
    cpatt = re.compile(patt)

    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                result.append(m.group())

    return result

if __name__ == '__main__':
    down_dir = '/tmp/163'
    fname = '/tmp/163/163.html'
    url163 = 'http://www.163.com'
    # 下载网易首页文件
    if not os.path.exists(down_dir):
        os.mkdir(down_dir)
    if not os.path.exists(fname):
        wget.download(url163, fname)

    # 在文件中取出所有图片的url
    img_patt = '(http|https)://[\w./_-]+\.(jpg|jpeg|png|gif)'
    img_list = get_patt(fname, img_patt, 'gbk')  # 网易使用gbk编码，不是默认的utf8

    # 下载
    for url in img_list:
        wget.download(url, down_dir)
