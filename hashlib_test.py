import hashlib
import sys
def _hash(fn):
    has = hashlib.md5()
    with open(fn, 'rb') as fobj:
        while 1:
            con = fobj.read(4096)
            if not con:
                break
            has.update(con)
    return has.hexdigest()

if __name__ == '__main__':
    print('%s  %s' % (_hash(sys.argv[1]), sys.argv[1]))
