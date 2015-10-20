#!/usr/bin/env python3.4
#
#  matrix.py
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
#  2015/09/30 12:27:50
#
#  ---
#

def msum(*matrices):
   '''Soma matrizes de duas dimensões'''
   head, *tail = matrices
   for matrix in tail:
      for x,row in enumerate(matrix):
         for y,col in enumerate(row):
            head[x][y] += col
   return head

def sort(lst, pos=0, reverse=False):
   '''
   Exercício - Python para desenvolvedores
   Recebe uma lista de dupla dimensão (matriz) e ordena pela posição especificada
   no argumento pos. Se for omitido a list será ordenada com base no primeiro item
   (pos 0).
   '''
   if not isinstance(lst,list) or not lst or pos>len(lst[0])-1:
      return None
   def _key(x):
      return x[pos]
   lst.sort(key=_key, reverse=reverse)
   return lst

