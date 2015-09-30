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
   '''
   adder(expr) -> (int,float)

   Recebe uma expressão no formato n+n. n pode ser int ou float.
   Retorna o resultado da expressão fornecida.
   '''
   oper = expr.index("+")
   pref = float(expr[:oper])
   suf = float(expr[oper+1:])
   return pref+suf

def isprime(n):
   '''
   isprime(n) -> bool

   Verifica se o número é primo. O método utilizado é o seguinte: inicialmente
   é considerado -1,0,1 como não primos e o módulo de dois como primo. Em seguida é feita
   uma lista começando de 3 até a raiz quadrada do módulo do número fornecido, sem
   os pares que são compostos. O dois é inserido para para saber se n é par.

   '''
   if type(n)!=int or n in {-1, 0, 1}: return False
   if abs(n)==2: return True
   divisors = list(range(3,int(abs(n)**0.5+1),2))
   divisors.insert(0, 2)
   count = 0
   for num in divisors:
      if abs(n)%num==0:
         count+=1
   return count==0
