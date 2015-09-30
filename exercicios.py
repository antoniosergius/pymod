#!/usr/bin/env python3.4
#
#  2015/09/25 13:43:29
#
def mysort(lst, pos=0, reverse=False):
   '''
   mysort(lst, pos=0, reverse=False) -> list

   Recebe uma lista de dupla dimensão (matriz) e ordena pela posição especificada
   no argumento pos. Se for omitido a list será ordenada com base no primeiro item
   (pos 0).
   '''
   if not isinstance(lst,list) or not list or pos>len(lst[0])-1:
      return None
   def _key(x):
      return x[pos]
   lst.sort(key=_key, reverse=reverse)
   return lst

