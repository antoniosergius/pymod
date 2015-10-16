#!/usr/bin/env python3.4
#
#  mymath.py
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
def adder(expr):
   '''Retorna o resultado da adição fornecida em str.'''
   if not isinstance(expr,str):
      return None
   oper = expr.find("+")
   if oper==-1:
      return None
   return float(expr[:oper])+float(expr[oper+1:])

def is_prime(n):
   '''Verifica se o número n inteiro REAL é primo. Inicialmente -1,0 e 1 são considerados
   não primos e |2|, primo. Em seguida gera-se uma lista iniciando de 3 até raiz quadrada
   de |n|. Os pares não são incluídos na lista, pois são números compostos.'''

   if not isinstance(n,int) or n in (-1, 0, 1):
      return False
   n=abs(n)
   if n==2:
      return True
   divisors = [2] + list(range(3,int(n**0.5+1),2))
   for num in divisors:
      if not n%num:
         return False
   return True

def gen_primes(stop):
   '''Gerador de números primos naturais'''

   if not isinstance(stop,int) or stop<=1:
      return None
   if stop>=2:
      yield 2
   for n in range(3,stop+1,2):
      if is_prime(n):
         yield n

def count_primes():
   '''Gerador infinito de números primos'''
   from itertools import count
   return (n for n in count() if is_prime(n))

def range_primes(start, stop):
   '''Gerador de números primos naturais'''
   if not isinstance(start, int) or not isinstance(stop,int) or stop<=start: #or start<0:
      return None
   if start<=2:
      start=2
      yield 2
   start += 0 if start%2 else 1
   for n in range(start,stop+1,2):
      if is_prime(n):
         yield n

def matrix_sum(*matrices):
   '''Soma matrizes de duas dimensões'''
   head, *tail = matrices
   for matrix in tail:
      for x,row in enumerate(matrix):
         for y,col in enumerate(row):
            head[x][y] += col
   return head

def sort_matrix(lst, pos=0, reverse=False):
   '''
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
