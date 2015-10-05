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
from os.path import exists, isfile, getsize, abspath

def info(filename):
   '''
   Imprime informações sobre o arquivo cujo nome foi fornecido.
   '''
   filename = abspath(filename)
   if exists(filename) and isfile(filename) and getsize(filename)>0:
      try:
         with open(filename) as objfile:
            content, line_count = '', 1
            for line in objfile:
               content += line
               line_count += 1
         return "%s : %d caractere(s), %d linha(s) e %d palavra(s)." \
                  %(filename, len(content), line_count, len(content.split()))
      except (UnicodeDecodeError, OSError):
         pass
   return None

def read(filename):
   filename = abspath(filename)
   if exists(filename) and isfile(filename) and getsize(filename)>0:
      try:
         readed = ''
         with open(filename) as f:
            for number,line in enumerate(f):
               readed+= "%d %s" %(number,line)
         return readed
      except (UnicodeDecodeError, OSError):
         pass
   return None

def write(filename, s):
   '''
   Cria um arquivo e escreve s dentro. Caso já exista um arquivo com o nome informado, o erro
   é impresso na tela.
   '''
   try:
      with open(filename, mode="x") as f:
         f.write(s)
   except (UnicodeDecodeError, OSError) as e:
      print(e)
