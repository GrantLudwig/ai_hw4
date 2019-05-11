#hw4.py v1.0
#Grant Ludwig
#5/17/19

import sys

def readFile(fileName):
    for line in open(fileName):
        line = line.rstrip()

#driver code
fileName = sys.argv[1]
