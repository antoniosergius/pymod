#!/usr/bin/env python3.4

'''
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.


util.py é um conjunto de funções úteis no dia a dia.
Autor: Antônio Sérgio Garcia Ferreira
Data: 24 Ago 2015
'''
import re

def align(text, width):
   '''
   Alinha a str text com espaços de acordo com o tamanho definido em width.
   '''
   blanks = width - len(str(text))
   right = blanks//2
   left = right+blanks%2
   return "%s %s %s" %(left*"-", text, right*"-")

def alignc(text, width, char):
   '''
   Alinha a str text com espaços de acordo com o tamanho definido em width.
   '''
   blanks = width - len(str(text))
   right = blanks//2
   left = right+blanks%2
   return "%s %s %s" %(left*char, text, right*char)

def printASCII():
   '''
   Imprime a tabela ASCII a partir do número 32
   '''
   printRangeASCII(32, 255)

def printRangeASCII(start, end):
   '''
   Imprime um intervalo da tabela ASCII a partir do número 32 até 255.
   start é o valor inicial e end é o valor final do intervalo.
   '''
   ordList, chrList = [],[]
   for i in range(start, end+1):
      ordList.append(align(i,4))
      chrList.append(align(chr(i),4))

   textUp, textDown, fullTxt = 'chr:','ord:',''
   for i in range(len(ordList)):
      if i!=0 and i%16==0:
         fullTxt += '\n'+textUp+'\n'+textDown+'\n'
         textUp, textDown = 'chr:','ord:'
      textUp += chrList[i]
      textDown += ordList[i]
   fullTxt += '\n'+textUp+'\n'+textDown+'\n'
   print(fullTxt)


def mystrip(s):
   '''
   mystrip(s) -> str

   Retira o primeiro e último caracter da string.
   '''
   return s[1:len(s)-1]

def oneTriangle(n):
   '''
   Imprime um triângulo com vários caracteres '1'.
   n representa o número de linhas do triangulo.
   '''
   for i in range(n, 0, -1):
      print('1'*i)

def adder(expr):
   '''
   adder(expr) -> (int,float)

   Recebe uma expressão no formato n+n. n pode ser int ou float.
   Retorna o resultado da expressão fornecida.
   '''
   oper = expr.index("+")
   pref = int(expr[0:oper])
   suf = int(expr[oper+1:len(expr)])
   return pref + suf

def subsCount(sub, s):
   '''
   subsCount(sub, string) -> int

   Conta a quantidade de substring sub que string contém.
   '''
   if not sub:
         return 0
   try:
      i = 0
      repeated = 0;
      while i < len(s):
         if s[i:i+len(sub)] == sub:
             repeated += 1
         i += 1
      return repeated
   except:
      return -1

def timeAfter(time, plus):
   '''
   timeAfter(time,plus) -> str

   time deve ser str no formato hh:mm
   plus é a quantidade de minutos a adicionar no horário fornecido
   Retorna novo horário no formato hh:mm
   '''
   time = time.partition(":")
   hour = int(time[0])
   minute = int(time[2]) + plus
   if minute>60:
      hour += minute//60
      minute = minute%60
   if hour >= 24:
      if hour == 24:
         hour = 0
      else:
         hour = hour%24
   return "%02d:%02d" % (hour, minute)

def lower(char):
   '''
   lower(char) -> str

   Raise TypeError se char não for do tipo str

   Retorna a versão minúscula do caracter informado.
   Caso o caracter não seja alfabético, o mesmo fornecido é retornado.
   '''
   if not isinstance(char, str):
      raise TypeError("Invalid types.")
   ordi = ord(char)
   if ordi>=65 and ordi<=90:
      return chr(ordi+32)
   else:
      return char

def ispalindrome(string):
   '''
   ispalindrome(string) -> bool

   Verifica se a string é palíndrome, ou seja, possui o mesmo formato
   se for invertida. Por exemplo: ana, adida, 00a00, iiisssiii
   '''
   if string[0] != string[-1]:
      return False
   for i in range(1, len(string)-2):
      if string[i] != string[-(i+1)]:
         return False
   return True

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

def tempconv(temp, unit):
   '''
   tempconv(temp, unit) -> float

   Raises TypeError se temp não for float ou int.
   Raises ValueError se unit não for 'f' de fahrenheit ou 'c' de celsius.

   Converte temperaturas de uma unidade para outra. Se for fornecido 'c'
   a temperatura será convertida para fahrenheit. Se for fornecido 'f' para
   unit, a função entende que o valor fornecido é em fahrenheit e converte
   para celsius.
   '''
   if not isinstance(temp, (float,int)):
      raise TypeError("Error: Invalid type. Temperature must be float or int.")
   if not isinstance(unit, str):
      raise TypeError("Error: Invalid type. Unit must be str.")
   unit = unit.lower()
   if unit == 'c':
      return temp * 9/5 + 32 #returna em fahrenheit
   elif unit == 'f':
      return (temp-32) * 5/9 #returna em celsius
   else:
      raise ValueError("Error: Invalid format. Unit must be str 'c' ou 'f'")


def isvalidcpf(cpf):
   '''
   isvalidcpf(cpf) -> bool

   Faz o cálculo dos dois últimos digitos(verificadores) do cpf.
   Retorna False se todos os digitos forem iguais.
   Retorna True se os digitos verificadores forem igual ao fornecido.
   Retorna False se os digitos forem diferentes.
   '''
   if cpf.count(cpf[0]) == 11:
      return False
   flag = 10
   count = summ = 0
   while flag <= 11:
      summ = 0
      for i in range(flag, 1, -1):
         summ += int(cpf[count]) * i
         count += 1
      remainder = summ % 11
      if remainder < 2 and cpf[flag-1] != '0':
         return False
      elif 11-remainder != int(cpf[flag-1]):
         return False
      count = 0
      flag += 1
   return True

def isvalidcnpj(cnpj):
   '''
   isvalidcnpj(cnpj) -> bool

   Faz o cálculo dos dois últimos digitos(verificadores) do cnpj.
   Retorna True se os digitos verificadores forem igual ao fornecido.
   Retorna False se os digitos forem diferentes.
   '''
   flag = 5
   count = summ = 0
   while flag <= 6:
      summ = 0
      for i in range(flag, 1, -1):
         summ += int(cnpj[count]) * i
         count += 1
      for i in range(9, 1, -1):
         summ += int(cnpj[count]) * i
         count += 1
      remainder = summ % 11
      if remainder < 2 and cnpj[flag+7] != '0':
         return False
      elif 11-remainder != int(cnpj[flag+7]):
         return False
      count = 0
      flag += 1
   return True

def isregvalid(reg):
   '''
   isregvalid(reg) -> bool

   Verifica se a str reg (CPF/CNPJ) é valido. reg deve conter apenas
   números e ser do tamanho 11 ou 14. Caso nenhuma das especificações
   citadas for verdadeira, o retorno será False. Após passar nos testes,
   se o valor for 11, reg será considerado cpf; se for 14, reg será
   considerado cnpj. Em seguida é feito os cálculos através das funções
   isvalidcpf(reg) ou isvalidcnpj(reg). Se o cálculo validar o registro,
   o retorno será True. Caso os digitos verificadores não estiverem
   corretos, o retorno será False.
   '''
   if not isinstance(reg, str):
      return False
   size = len(reg)
   if size==11 or size==14:
      expr = "^\d{"+str(size)+"}$"
      regex = re.compile(expr)
      if not regex.match(reg):
         return False
      if size==11:
         return isvalidcpf(reg)
      else:
         return isvalidcnpj(reg)
   else:
      return False


