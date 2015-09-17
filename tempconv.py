#!/usr/bin/env python3.4
import util
import sys
import re
    
def fexit(err, printmsg):
   if printmsg:
      print("\nUsage: tempconv.py temp c|f")
      print("     : temp : float number.")
      print("     : c|f: 'c'elsius or 'f'ahrenheit.\n")	
   else:
   print(err)
   sys.exit(-1)  

def usage():
   fexit("", True)

nargs = len(sys.argv)
if nargs != 3:
   usage()

arg1 = sys.argv[1]
regx = re.compile("^\d*[.]{0,1}\d+$")
if not regx.match(arg1):
   fexit("Error: Invalid format number.", False)

arg2 = sys.argv[2]
regx = re.compile("^c$|^f$")
if not regx.match(arg2):
   fexit("Error: Invalid unit (c|f).", False)

if arg2 == 'c':
   unit = 'f'
else:
   unit = 'c'

try:
   newtemp = util.tempconv(float(arg1), arg2)
   print(format(newtemp,'.2f'), chr(176)+unit)
except TypeError as typErr:
   print(typErr)
except ValueError as valueErr:
   print(valueErr)
finally:
   sys.exit(0)

