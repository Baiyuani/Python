from time import strftime
import hashlib
import tarfile
import os
import pickle

def _hash(fn):
    #计算hash值
    has = hashlib.md5()
    with open(fn, 'rb') as fobj:
        while 1:
            con = fobj.read(4096)
            if not con:
                break
            has.update(con)
    return has.hexdigest()

def full_backup(src, dest, md5file):
    # 对整个目录打包
    fn = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fn = os.path.join(dest, fn)

    #备份
    tar = tarfile.open(fn, 'w:gz')
    tar.add(src)
    tar.close()

    #计算md5值
    md5dic = {}
    for path, dir, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dic[key] = _hash(key)

    #将md5值写入file
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dic, fobj)

def incr_backup(src, dest, md5file):
    #增量备份
    fn = '%s_incr_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fn = os.path.join(dest, fn)

    #计算md5值
    md5dic = {}
    for path, dir, files in os.walk(src):
        for file in files:
           key = os.path.join(path, file)
           md5dic[key] = _hash(key)

    #取出旧md5值
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    tar = tarfile.open(fn, 'w:gz')
    for key in md5dic:
        if old_md5.get(key) != md5dic[key]:
            tar.add(key)
    tar.close()

    #更新md5值
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dic, fobj)

if __name__ == '__main__':
    dest = '/tmp/demo/backup'
    src = '/tmp/demo/security'
    md5file = '/tmp/demo/backup/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src, dest, md5file)
    else:
        incr_backup(src, dest, md5file)
