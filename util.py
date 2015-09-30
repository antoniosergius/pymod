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

def flatten_list(lst):
   '''
   flatten_list(lst) -> list

   Recebe uma lista de duas dimensões e retorna uma de dimensão única.
   A técnica usada é conhecida como list comprehension
   '''
   if type(lst)!=list or not lst:
      return -1
   else:
      return [num for elem in lst for num in elem]

def dict_statistics(dic):
   '''
   dict_statistics(dic)

   Imprime a média, soma, variância e o desvio padrão de um dicionário com
   valores númericos.
   '''
   if type(dic)!=dict or len(dic) in (0,1):
      return -1
   summ = 0.0
   for value in dic.values():
      summ += value
   rate = summ / len(dic)
   variance = 0.0
   for value in dic.values():
      variance += (value - rate)**2
   statistics='''
      Rate = %.2f
      Summ = %.2f
      Data Variance    = %.2f
      Stand. Deviation = %.2f
   ''' %(rate, summ, variance/(len(dic)-1), variance**0.5)
   print(statistics)

def is_valid_cpf(cpf):
   '''
   is_valid_cpf(cpf) -> bool

   Faz o cálculo dos dois últimos digitos(verificadores) do cpf.
   Retorna False se todos os digitos forem iguais.
   Retorna True se os digitos verificadores forem igual ao fornecido.
   Retorna False se os digitos forem diferentes.
   '''
   if cpf[0]==cpf[-1] and cpf.count(cpf[0])==11:
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

def is_valid_cnpj(cnpj):
   '''
   is_valid_cnpj(cnpj) -> bool

   Faz o cálculo dos dois últimos digitos(verificadores) do cnpj.
   Retorna True se os digitos verificadores forem igual ao fornecido.
   Retorna False se os digitos forem diferentes.
   '''
   flag = 5
   count, summ = 0, 0
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

def is_valid_registry(reg):
   '''
   is_valid_registry(reg) -> bool

   Verifica se a str reg (CPF/CNPJ) é valido. reg deve conter apenas
   números e ser do tamanho 11 ou 14. Caso nenhuma das especificações
   citadas for verdadeira, o retorno será False. Após passar nos testes,
   se o valor for 11, reg será considerado cpf; se for 14, reg será
   considerado cnpj. Em seguida é feito os cálculos através das funções
   is_valid_cpf(reg) ou is_valid_cnpj(reg). Se o cálculo validar o registro,
   o retorno será True. Caso os digitos verificadores não estiverem
   corretos, o retorno será False.
   '''
   if not isinstance(reg, str):
      return False
   sset = {11,14}
   size = len(reg)
   if size in sset:
      if not re.compile("^\d{%d}$" %size).match(reg):
         return False
      else:
         return is_valid_cpf(reg) if size==11 else is_valid_cnpj(reg)
   else:
      return False
