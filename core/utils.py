import re, sys
from os import path
import subprocess


def trimLeading(str, startChar='0'):
    return re.sub("^%s+" % startChar, "", str)


class Bunch:
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __repr__(self):
        return '<%s>' % str('\n '.join('%s : %s' % (k, repr(v)) for (k, v) in self.__dict__.iteritems()))


def checkFile(filePath, descr, usageFn):
    if filePath == "":
        print("Please specify a %s" % descr)
        usageFn()
    elif not path.exists(filePath):
        print("%s does not exist, please correct" % filePath)
        sys.exit(2)


def memoize(fn):
    fbResults = {}

    def memoized(*args):
        if args in fbResults:
            return fbResults[args]
        else:
            result = fbResults[args] = fn(*args)
            return result

    return memoized


def runProcess(exe):
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while (p.poll() == None):  # returns None while subprocess is running
        time.sleep(0.05)
    stdouttxt = p.communicate()[0]
    return p.returncode, stdouttxt.decode('utf-8')


