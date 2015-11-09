#!/usr/bin/env python3.4
#
#  util.py
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
#  2015/08/24 20:10:45
#
#  ---
#
def flatten(it):
   '''
   flatten(it) -> list
   Recebe uma lista de várias dimensões e retorna uma de dimensão única.
   '''
   if isinstance(it, list):
      ls=[]
      for item in it:
         ls = ls + flatten(item)
      return ls
   else:
      return [it]

def statistics(dic):
   '''Retorna a média, soma, variação de um dicionário com valores númericos.'''
   if not isinstance(dic, dict) or len(dic) in (0,1):
      return None
   summ = sum(dic.values())
   rate = summ / len(dic)
   variance = max(dic.values())-min(dic.values())
   return summ, rate, variance

#def rgb_list():
   #rgb = []
   #for r in range(254):
      #for g in range(254):
         #for b in range(254):
            #rgb.append((r,g,b))
   #return rgb

#def rgb_gen():
   #for r in range(254):
      #for g in range(254):
         #for b in range(254):
            #yield r,g,b

#def test_rgb():
   #from time import time
   #start = time()
   #rgb = rgb_list()
   #print(time() - start)
   #start = time()
   #rgb = []
   #for color in rgb_gen(): pass
   #print(time() - start)
