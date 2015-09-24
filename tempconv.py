#!/usr/bin/env python3.4
import util
import sys
import re

def convert_temperature(temp):
   '''
   convert_temperature(temp) -> str

   Converte temperaturas de uma unidade para outra.
   A temperatura deve ser fornecida com C ou F no final.
   '''
   unit = temp[-1]
   temp = float(temp[:-1])
   result = ''
   if unit=='C':
      result = "%.2f%s" %(temp*9/5+32, 'F')
   else:
      result = "%.2f%s" %((temp-32)*5/9, 'C')
   return result

def usage():
   usage='''Usage: tempconv.py temp
       temp : string - final position F or C (Celsius of Fahrenheit).'''
   print(usage)
   sys.exit(-1)

if __name__ == '__main__':
   if len(sys.argv) != 2:
      usage()
   temperature = sys.argv[1].upper()
   if re.compile("^\d*[.]{0,1}\d*[C|F]{1}$").match(temperature):
      print(convert_temperature(temperature))
   else:
      usage()


