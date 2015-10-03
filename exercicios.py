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

def file_info(name):
   '''
   Imprime informações sobre o arquivo cujo nome foi fornecido.
   '''
   try:
      with open(name,'r') as file:
         text=''
         for line in file: text+=line
         chars=len(text)
         lines=len(text.split("\n"))
         words=len(text.split())
         print("O arquivo '%s' tem %d caractere(s), %d linhas e %d palavras."\
                %(name, chars, lines, words))
   except IOError:
      print("Arquivo não encontrado!")
