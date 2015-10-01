#!/usr/bin/env python3.4
import mystr
import sys

def usage():
   usage = '''Usage: printASCII.py [start stop]
   start: int >= 32.
   stop : int > start.'''
   print(usage)
   sys.exit(-1)

def show_ascii(start=32, end=255):
   if start < 32 or start > end:
      usage()
   ords, chrs = [],[]
   for i in range(start, end+1):
      ords.append(mystr.align(i,4))
      chrs.append(mystr.align(chr(i),4))
   up, down, table = 'chr:','ord:',''
   for i in range(len(ords)):
      if i and not i%16:
         table += "\n %s \n %s \n" %(up, down)
         up, down = 'chr:','ord:'
      up += chrs[i]
      down += ords[i]
   table += "\n %s \n %s \n" %(up, down)
   return table

if __name__ == "__main__":
   if len(sys.argv)>=3:
      for s in sys.argv[1:3]:
         if not s.isdigit():
            usage()
      print(show_ascii(int(sys.argv[1]), int(sys.argv[2])))
   else:
       print(show_ascii())
