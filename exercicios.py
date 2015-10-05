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
         print("'%s': %d caractere(s), %d linha(s) e %d palavra(s)." %(name, chars, lines, words))
   except IOError:
      print("Arquivo não encontrado!")

def read_file(name):
   readed = ''
   with open(name,"r") as file:
      for number,line in enumerate(file):
         readed+= "%d %s" %(number,line)
   return readed

def write_file(filename, s):
   with open(filename, "w") as f:
      f.write(s)


if __name__=="__main__":
   for f in pathlib.Path('.').iterdir():
      if not f.is_dir():
         file_info(str(f))
