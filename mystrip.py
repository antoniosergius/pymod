#!/usr/bin/env python3.4
import mystr
import sys

def get_line():
   lineIn=input()
   if len(lineIn)<2:
      print("Error: Input length must be greater than 2.")
   else:
      print(mystr.mystrip(lineIn))

while True:
   try:
      get_line()
   except EOFError as err:
      sys.exit(0)


