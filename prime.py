#!/usr/bin/env python3.4
#
#  prime.py
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
#  2015/10/20 10:35:50
#
#  ---
#
import itertools
import random

def is_prime(n):
   '''Verifica se o número n inteiro REAL é primo. Inicialmente -1,0 e 1 são considerados
   não primos e |2|, primo. Em seguida gera-se uma lista iniciando de 3 até raiz quadrada
   de |n|. Os pares não são incluídos na lista, pois são números compostos.'''
   if n in (-1, 0, 1): return False
   n=abs(n)
   if n == 2 : return True
   if not n%2: return False
   for num in range(3,int(n**0.5+1),2):
      if not n%num: return False
   return True

def gen(start, stop=None):
   '''Gerador de números primos naturais'''
   if not stop:
      start,stop = 0,start
   if start<2: yield 2
   start += 0 if start%2 else 1
   for n in range(start,stop+1,2):
      if is_prime(n):
         yield n

def count():
   '''
   Gerador infinito de números primos
   Pode ser combinado com expressão geradora da seguinte maneira
   para, por exemplo, descobrir os primeiros 200 números primos:

   generator = ( i for i in prime.count() )
   for i in range(200):
      print(next(generator))
   '''
   for num in itertools.count():
      if is_prime(num):
         yield num

def randrange(start, stop=None):
   '''
   Retorna um número aleatório no intervalo de [start,stop].
   Se stop for omitido, start=0 e stop=start
   '''
   if not stop:
      start,stop = 0,start
   while True:
      choice = random.randint(start,stop)
      if is_prime(choice):
         return choice

#def gen(stop):
   #'''Gerador de números primos naturais'''
   #if not isinstance(stop,int) or stop<=1:
      #return None
   #if stop>=2:
      #yield 2
   #for n in range(3,stop+1,2):
      #if is_prime(n):
         #yield n
