#!/usr/bin/env python3.4
#
#  reg.py
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
#  2015/10/19 19:17:45
#
#  ---
#
def gen_cpf(stop=1):
   '''Gerador de CPF'''
   from random import randint
   if not isinstance(stop, int) or stop<1:
      return None
   for i in range(stop):
      cpf = "{:09d}".format(randint(0,999999999))
      count, summ, flag = 0, 0, 10
      while flag <= 11:
         summ = 0
         for n in range(flag, 1, -1):
            summ += int(cpf[count])*n
            count += 1
         remainder = summ % 11
         cpf = "{}{}".format(cpf,'0') if remainder<2 else "{}{}".format(cpf,11-remainder)
         flag += 1
         count = 0
      yield cpf

def gen_cnpj(stop=1):
   '''Gerador de CPNJ'''
   from random import randint
   if not isinstance(stop, int) or stop<1:
      return None
   for i in range(stop):
      cnpj = "{:08d}{}".format(randint(0,99999999),'0001')
      count, summ, flag = 0, 0, 5
      while flag <= 6:
         summ = 0
         for n in range(flag, 1, -1):
            summ += int(cnpj[count])*n
            count += 1
         for n in range(9, 1, -1):
            summ += int(cnpj[count])*n
            count += 1
         remainder = summ % 11
         cnpj = "{}{}".format(cnpj,'0') if remainder<2 else "{}{}".format(cnpj,11-remainder)
         flag += 1
         count = 0
      yield cnpj

def random():
   '''Randomiza registro (CNPJ/CPF)'''
   from random import choice
   return choice((next(gen_cpf()),next(gen_cnpj())))

def raw(reg):
   "Remove caracteres especiais de cpf e cnpj"
   for sym in './-':
      reg = reg.replace(sym,'')
   return reg

def format(reg):
   "Formata CPF/CNPJ"
   if len(reg)==11:
      return "{}.{}.{}-{}".format(reg[:3],
                                  reg[3:6],
                                  reg[6:9],
                                  reg[9:11])
   else:
      return "{}.{}.{}/{}-{}".format(reg[:2],
                                     reg[2:5],
                                     reg[5:8],
                                     reg[8:12],
                                     reg[12:14])
def zcut(reg):
   '''
   Retira os zeros a esquerda de uma string maior que 14.
   Caso algum caracter não seja 0, a mesma string fornecida é retornada.
   '''
   size = len(reg)
   if size>14 and reg[0]=='0':
      START = slice(size-14)
      END = slice(size-14,size)
      prefix, rest = reg[START], reg[END]
      if prefix.count('0') == len(prefix):
         return rest
   return reg

def valid(reg):
   '''Retorna True se o registro reg for um CPF/CNPJ válido.'''
   def _is_cnpj(cnpj):
      '''Função interna que valida o cnpj.'''
      count, summ, flag = 0, 0, 5
      while flag <= 6:
         summ = 0
         for n in range(flag, 1, -1):
            summ += int(cnpj[count])*n
            count += 1
         for n in range(9, 1, -1):
            summ += int(cnpj[count])*n
            count += 1
         remainder = summ % 11
         if remainder < 2:
            if cnpj[flag+7] != '0': return False
         elif 11-remainder != int(cnpj[flag+7]): return False
         count = 0
         flag += 1
      else: return True
   def _is_cpf(cpf):
      '''Função interna que valida o cpf.'''
      head,*body,tail = cpf
      if head==tail and body.count(head)==9: return False
      count, summ, flag = 0, 0, 10
      while flag <= 11:
         summ = 0
         for n in range(flag, 1, -1):
            summ += int(cpf[count])*n
            count += 1
         remainder = summ % 11
         if remainder < 2:
            if cpf[flag-1]!='0': return False
         elif 11-remainder != int(cpf[flag-1]): return False
         count = 0
         flag += 1
      else: return True

   if not isinstance(reg, str):
      return False
   elif not reg.isdigit():
      return False
   size = len(reg)
   if size==11:
      return _is_cpf(reg)
   elif size==14:
      return _is_cnpj(reg)
   elif size>14:
      return _is_cnpj(zcut(reg))
   return False
