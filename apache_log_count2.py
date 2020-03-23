import re

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_pattern(self, patt):
        result = {}  #用于保存结果
        cpatt = re.compile(patt)
        with open(self.fname) as fobj:
            for i in fobj:
                m = cpatt.search(i)
                if m:   #任何非空对象都为真
                    key = m.group()
                    result[key] = result.get(key, 0) + 1
        return result

if __name__ == '__main__':
    logfile = 'access_log'
    ip = '^\d+(\.\d+){3}'
    br = 'Chrome|Firefox|MSIE'
    oss = 'Windows|Linux'
    example = CountPatt(logfile)
    result1 = example.count_pattern(ip)
    result2 = example.count_pattern(br)
    result3 = example.count_pattern(oss)
    print(result1)
    print(result2)
    print(result3)
