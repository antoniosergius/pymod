#!/bin/bash
#
#  mystr.py
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
#  2015/09/24 13:45:37
#
#  ---
#

def subs_count(sub, s):
   if not sub: return 0
   count=0
   for i,_ in enumerate(s):
      if s[i:i+len(sub)] == sub:
         count+=1;
   return count

def lower(text):
   '''
   lower(text) -> str

   Raise TypeError se text não for do tipo str

   Retorna a versão minúscula do texto informado.
   '''
   if not isinstance(text, str) or not text:
      return -1

   new = ''
   for i,ch in enumerate(text):
      position = ord(ch)
      new += chr(position+32) if 65<=position<=90 else ch
   return new


def is_palindrome(string):
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
