#!/usr/bin/env python3.4
import util
import sys

POS_START=32
POS_STOP=255
RANGE_ERROR=-1

def usage():
    print("\nUsage: printASCII.py [stop]")
    print("       printASCII.py [start stop]\n")
    print("     : stop : int range 33-255.")
    print("     : start: int range 32-254.")
    print("     : use start only with stop arg.\n")
    sys.exit(-1)

def getAtt(boolExpr, intArg):
    if boolExpr:
        return intArg
    else:
        return RANGE_ERROR

def getStop(arg):
    stop=int(arg)
    expr = POS_START<=stop<= POS_STOP
    return getAtt(expr, stop)

def get2ArgsStop(arg):
    stop=int(arg)
    expr = POS_START+1<=stop<=POS_STOP
    return getAtt(expr, stop)

def get2ArgsStart(arg):
    start=int(arg)
    expr = POS_START<=start<=POS_STOP-1
    return getAtt(expr, start)

def runWithOneArg():
    try:
        stop=getStop(sys.argv[1])
        if stop==RANGE_ERROR:
            usage()
        else:
            util.printRangeASCII(POS_START, stop)
    except ValueError:
        usage()

def runWithTwoArgs():
    try:
        start=get2ArgsStart(sys.argv[1])
        stop=get2ArgsStop(sys.argv[2])
        if start!=RANGE_ERROR and stop!=RANGE_ERROR and start<stop:
            util.printRangeASCII(start, stop)
        else:
            usage()
    except ValueError:
        usage()

nargs=len(sys.argv)

if nargs==2:
    runWithOneArg()
elif nargs>=3:
    runWithTwoArgs()
else:
    util.printASCII()
sys.exit(0)


