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
import re

def replace(old, new, lst):
   '''
   Substitui old por new na lista lst.
   Raises TypeError se lst não for list.
   '''
   if not isinstance(lst, list):
      raise TypeError("Error: Invalid type. lst must be list.")
   for i, item in enumerate(lst):
      if item == old:
         lst.pop(i)
         lst.insert(i, new)
         break

def flatten_old(lst):
   '''
   flatten_list(lst) -> list

   Recebe uma lista de duas dimensões e retorna uma de dimensão única.
   A técnica usada é conhecida como list comprehension
   '''
   if type(lst)!=list or not lst:
      return -1
   else:
      return [num for elem in lst for num in elem]

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


def stat(dic):
   '''
   stat(dic)

   Imprime a média, soma, variância e o desvio padrão de um dicionário com
   valores númericos.
   '''
   if not isinstance(dic, dict) or len(dic) in (0,1):
      return None
   summ = sum(dic.values())
   rate = summ / len(dic)
   variance = max(dic.values())-min(dic.values())
   return summ, rate, variance

def is_cpf(cpf):
   '''
   is_valid_cpf(cpf) -> bool

   Faz o cálculo dos dois últimos digitos(verificadores) do cpf.
   Retorna False se todos os digitos forem iguais.
   Retorna True se os digitos verificadores forem igual ao fornecido.
   Retorna False se os digitos forem diferentes.
   '''
   if cpf[:2]==cpf[9:] and cpf.count(cpf[2:9])==7:
      return False
   flag = 10
   count, summ = 0, 0
   while flag <= 11:
      summ = 0
      for i in range(flag, 1, -1):
         summ += int(cpf[count]) * i
         count += 1
      remainder = summ % 11
      if remainder < 2:
         if cpf[flag-1]!='0': return False
      elif 11-remainder != int(cpf[flag-1]):
         return False
      count = 0
      flag += 1
   return True

def is_cnpj(cnpj):
   '''
   is_cnpj(cnpj) -> bool

   Faz o cálculo dos dois últimos digitos(verificadores) do cnpj.
   Retorna True se os digitos verificadores forem igual ao fornecido.
   Retorna False se os digitos forem diferentes.
   '''
   count, summ, flag = 0, 0, 5
   while flag <= 6:
      summ = 0
      for i in range(flag, 1, -1):
         summ += int(cnpj[count])*i
         count += 1
      for i in range(9, 1, -1):
         summ += int(cnpj[count])*i
         count += 1
      remainder = summ % 11
      if remainder < 2:
         if cnpj[flag+7] != '0': return False
      elif 11-remainder != int(cnpj[flag+7]):
         return False
      count = 0
      flag += 1
   return True

def is_cpf_cnpj(s):
   '''
   is_cpf_cnpj(s) -> bool

   Verifica se a str s (CPF/CNPJ) é valida. reg deve conter apenas
   números e ser do tamanho 11 ou 14. Caso nenhuma das especificações
   citadas for verdadeira, o retorno será False. Após passar nos testes,
   se o valor for 11, s será considerado cpf; se for 14, s será
   considerado cnpj. Em seguida é feito os cálculos através das funções
   is_cpf(s) ou is_cnpj(s). Se o cálculo validar o registro,
   o retorno será True. Caso os digitos verificadores não estiverem
   corretos, o retorno será False.
   '''
   if not isinstance(s, str):
      return False
   length, regex = len(s), re.compile("^\d{%d}$" %length)
   if length not in (11,14) or not regex.match(s):
      return False
   else:
      return is_cpf(s) if length==11 else is_cnpj(s)
