#!/usr/bin/env python3.4
import util
import sys

def usage():
   usage = '''Usage: printASCII.py [start stop]
   start: int range 32-254.
   stop : int range 33-255.'''
   print(usage)
   sys.exit(-1)

def show_ascii(start, end):
   ord_list, chr_list = [],[]
   for i in range(start, end+1):
      ord_list.append(util.align(i,4))
      chr_list.append(util.align(chr(i),4))
   up, down, alltext = 'chr:','ord:',''
   for i,_ in enumerate(ord_list):
      if i!=0 and i%16==0:
         alltext += "\n %s \n %s \n" %(up, down)
         up, down = 'chr:','ord:'
      up += chr_list[i]
      down += ord_list[i]
   alltext += "\n %s \n %s \n" %(up, down)
   return alltext

def show_all_ascii():
   return show_ascii(32, 255)

if __name__ == "__main__":
   if len(sys.argv)>=3:
      for s in sys.argv[1:3]:
         if not s.isdigit():
            usage()
      print(show_ascii(int(sys.argv[1]), int(sys.argv[2])))
   else:
       print(show_all_ascii())
