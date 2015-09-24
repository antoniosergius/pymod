#!/usr/bin/env python3.4
import sys
import re

def usage():
   msg = '''Usage: timeafter.py hour addition\n
       hour : hh:mm format.
       addition: minute(s) to add.\n'''
   print(msg)
   sys.exit(-1)

def timeAfter(hour, minutes, addition):
   minutes += addition
   if minutes>60:
      hour += minutes//60
      minutes %= 60
   if hour==24:
      hour = 0
   elif hour > 24:
      hour %= 24
   return "%02d:%02d" %(hour, minutes)

if __name__ == '__main__':
   if len(sys.argv) != 3:
      usage()
   hour, addition = sys.argv[1], sys.argv[2]
   if not re.compile("\d{0,1}\d:\d\d").match(hour):
      print("Error: Invalid time format (hh:mm).")
   elif not re.compile("\d+").match(addition):
      print("Error: Invalid minute format.")
   else:
      horary = hour.partition(":")
      hour, minutes, addition = int(horary[0]), int(horary[2]), int(addition)
      if hour>=24 or minutes>=60:
         print("Error: Invalid time.")
      else:
         print(timeAfter(hour,minutes, addition))
