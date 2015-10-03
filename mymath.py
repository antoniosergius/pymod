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
   if not isinstance(expr,str):
      return None
   oper = expr.find("+")
   if oper==-1:
      return None
   return float(expr[:oper])+float(expr[oper+1:])

def is_prime(n):
   '''
   isprime(n) -> bool

   Verifica se o número n REAL é primo. O método utilizado é o seguinte: inicialmente
   é considerado -1,0,1 como não primos e o módulo de dois como primo. Em seguida é feita
   uma lista começando de 3 até a raiz quadrada do módulo do número fornecido, sem
   os pares que são compostos. O número 2 (dois) é inserido para para saber se n é par.
   '''
   if not isinstance(n,int) or n in (-1, 0, 1):
      return False
   n=abs(n)
   if n==2:
      return True
   divisors = list(range(3,int(n**0.5+1),2))
   divisors.insert(0, 2)
   for num in divisors:
      if not n%num:
         return False
   else:
      return True