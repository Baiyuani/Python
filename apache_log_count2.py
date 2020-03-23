import re

class CountPatt:
    def count_pattern(self, fname, patt):
        result = {}  #用于保存结果
        cpatt = re.compile(patt)
        with open(fname) as fobj:
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
    example = CountPatt()
    result1 = example.count_pattern(logfile, ip)
    result2 = example.count_pattern(logfile, br)
    print(result1)
    print(result2)