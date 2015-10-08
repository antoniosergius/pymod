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
import sys
from os.path import exists, isfile, getsize, abspath

def info(filename):
   '''Exibe informações sobre o arquivo fornecido'''
   filename = abspath(filename)
   try:
      with open(filename) as f:
         text = f.read()
         return "%s : %d char(s), %d linha(s) e %d palavra(s)." \
                 %(filename, len(text), text.count("\n"), len(text.split()))
   except (UnicodeDecodeError, OSError) as e:
      print(e)

def read_lines(filename):
   '''Lê o arquivo fornecido e retorna uma lista com as linhas'''
   filename = abspath(filename)
   try:
      with open(filename) as f:
         return f.readlines()
   except (UnicodeDecodeError, OSError) as e:
      print(e)

def read(filename):
   '''Lê todas as linhas do arquivo em uma única strig e a retorna'''
   filename = abspath(filename)
   try:
      with open(filename) as f: return f.read()
   except (UnicodeDecodeError, OSError) as e:
      print(e)

def write(filename, s):
   '''Escreve s dentro do arquivo filename não existente.'''
   try:
      with open(filename, mode="x") as f: f.write(s)
   except (UnicodeDecodeError, OSError) as e:
     print(e)

def write_lines(filename, lines):
   '''Cria um arquivo e escreve a lista lines dentro.'''
   try:
      with open(filename, mode="w") as f:
         for line in lines: print(line, file=f)
   except (UnicodeDecodeError, OSError) as e:
     print(e)

def read_csv(filename):
   '''Lê um arquivo csv e retorna uma lista de tuplas das linhas.'''
   try:
      with open(filename) as f:
         data=[]
         for line in filter(bool, f):
            *fields, last = line.split(",")
            fields.append(last.rstrip())
            data.append(tuple(fields))
         return data
   except (IOError,UnicodeDecodeError) as e:
      print(e)

def csv_to_dict(fn):
   '''
   Primeiramente o conteúdo do arquivo lido é dividido entre a primeira posição (o header com nome
   de todos os campos) e os dados. Nesse processo as funções rstrip() e split(',') cuidam de tirar
   os caracteres fim de linha e dividir a string (separador ',') e trasformar em lista.

   Neste momento os dados estão da seguinte forma:
   header -> ['nome','cadastro', ....]
   data -> [['Antonio Sergio','10008121205', ...], ['Goncalves Jr.','84421541241', ...], ...]

   O próximo passoo é criar um dicionário que a chave seja um campo principal ('cadastro' no
   meu caso) e o valor seja a representação do registro em forma de dicionário. A variável datalist
   receberá uma lista de dicionários de cada registro. A função zip trata de combinar o nome dos
   campos com os valores.

   datalist -> [ {'nome':'Antonio Sergio','cadastro':'10008121205',...},
                 {'nome':'Goncalves Jr.' ,'cadastro':'84421541241',...},
                ... ]

   Finalmente é retornado outro dicionário no seguinte formato:
   { '10008121205': {'nome':'Antonio Sergio', 'cadastro':'10008121205', ....},
     '84421541241': {'nome':'Goncalves Jr.' , 'cadastro':'84421541241', ....},
      ... }

   '''
   try:
      with open(fn) as fn:
         header, *data = [each.split(',') for each in [ line.rstrip() for line in fn ]]
   except (IOError,UnicodeDecodeError) as e:
      sys.stderr.write(e)
      return []
   else:
      datalist=[dict(zip(header,rec)) for rec in data]
      return {rec['cadastro']:rec for rec in datalist}

