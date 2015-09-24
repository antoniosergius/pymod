#!/usr/bin/env python3.4
import util
import sys
import re

def convert_temperature(temp):
   '''
   tempconv(temp, unit) -> float

   Raises TypeError se temp não for float ou int.
   Raises ValueError se unit não for 'f' de fahrenheit ou 'c' de celsius.

   Converte temperaturas de uma unidade para outra. Se for fornecido 'c'
   a temperatura será convertida para fahrenheit. Se for fornecido 'f' para
   unit, a função entende que o valor fornecido é em fahrenheit e converte
   para celsius.
   '''
   temp = float(temp[:-1])
   unit = temp[-1].upper()
   return temp*9/5+32 if unit=='C' else (temp-32)*5/9

def usage():
   usage='''Usage: tempconv.py temp
      temp : string - final position F or C (Celsius of Fahrenheit).'''
   print(usage)
   sys.exit(-1)

if __name__ == '__main__':
   if len(sys.argv) != 2:
      usage()
   temperature = sys.argv[1].upper()
   if re.compile("^\d*[.]{0,1}[C|F]{1}$").match(temperature):
      print(convert_temperature(temperature))
   else
      usage()


