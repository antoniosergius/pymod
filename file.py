#!/usr/bin/env python3.4
#
#  file.py
#
#  Copyright 2015 Antônio Sérgio Garcia Ferreira <antoniosergio@mail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  2015/10/05 11:23:19
#
#  ---
#
import os.path
def info(filename):
   '''
   Imprime informações sobre o arquivo cujo nome foi fornecido.
   '''

   try:
      with open(filename,'r') as file:
         text=''
         for line in file: text+=line
         chars=len(text)
         lines=len(text.split("\n"))
         words=len(text.split())
         print("'%s': %d caractere(s), %d linha(s) e %d palavra(s)." %(name, chars, lines, words))
   except IOError:
      print("Arquivo não encontrado!")

def read_file(name):
   readed = ''
   with open(name,"r") as file:
      for number,line in enumerate(file):
         readed+= "%d %s" %(number,line)
   return readed

def write_file(filename, s):
   with open(filename, "w") as f:
      f.write(s)
