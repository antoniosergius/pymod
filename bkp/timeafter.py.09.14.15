#!/usr/bin/env python3.4
import util
import sys
import re

def usage():
    print("\nUsage: timeafter.py time minutes")
    print("     : time : hh:mm format.")
    print("     : minutes: int value to add.\n")
    sys.exit(-1)
    
def failExit(err):
	print(err)
	sys.exit(-1)    
	
def matches(value, expr):
	regex = re.compile(expr)
	return regex.match(value)

if len(sys.argv) != 3:
	usage()

if not matches(sys.argv[1], "\d{0,1}\d:\d\d"):
	failExit("Error: Invalid time format (hh:mm).\n")

if not matches(sys.argv[2], "\d+"):
	failExit("Error: Invalid minute format.\n")
	
time = sys.argv[1]
minutes = int(sys.argv[2])

try:	
	print(util.timeAfter(time, minutes))
except TypeError as typErr:
	print(typErr)
except ValueError as valueErr:
	print(valueErr)
finally:
	sys.exit(0)

