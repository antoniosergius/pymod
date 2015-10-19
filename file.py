#!/usr/bin/env python3.4
#
#  file.py
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
#  2015/10/05 11:23:19
#
#  ---
#
import fileinput

def split(fn, nbytes):
   '''
   Exercicio 4 - Python para desenvolvedores.
   Divide o arquivo fn em nbytes e grava em novos arquivos. Se o arquivo for arq, será gravado
   arq_001, arq_002, etc..
   '''
   try:
      with open(fn,'rb') as f:
         _bytes = bytearray(f.read())
      parts = 1
      while _bytes:
         LIMIT = slice(0,nbytes)
         out = _bytes[LIMIT].decode('utf8')
         del _bytes[LIMIT]
         with open("{}_{:03d}".format(fn,parts), mode='wb') as fout:
            fout.write(out.encode('utf8'))
         parts += 1
   except Exception as e:
      print(e)

def gen_files(files):
   for f in files:
      with open(f,'rt') as fin:
         for line in fin:
            yield line

def join(new, ls):
   '''
   Exercício 4 - Python para desenvolvedores - metodo sem concatenação de strings
   Juntar os arquivos da lista fnlist em um unico arquivo outname e gravar no disco.
   '''
   try:
      out = []
      for fn in ls:
         with open(fn,'rb') as f:
            out.append(f.read())
      with open(new,'wb') as fout:
         fout.writelines(out)
   except Exception as e:
      print(e)

def split_text(fn, nbytes):
   '''
   Exercicio 4 - Python para desenvolvedores.
   Divide o arquivo fn em nbytes e grava em novos arquivos. Se o arquivo for arq, será gravado
   arq_001, arq_002, etc..'''
   try:
      with open(fn) as f:
         count=1
         stream = f.read(nbytes)
         while stream:
            with open("{}_{:03d}".format(fn,count), 'wt') as fout:
               fout.write(stream)
            stream = f.read(nbytes)
            count+=1
   except Exception as e:
      print(e)

def join_text(new, ls):
   '''
   Exercício 4 - Python para desenvolvedores
   Juntar os arquivos da lista fnlist em um unico arquivo outname e gravar no disco.
   '''
   try:
      for fn in ls:
         out = []
         with open(fn) as f:
            out.append(f.read())
      with open(new,'wt') as fout:
         fout.writelines(out)
   except Exception as e:
      print(e)

#def join_text(outname, fnlist):
   #'''
   #Exercício 4 - Python para desenvolvedores
   #Juntar os arquivos da lista fnlist em um unico arquivo outname e gravar no disco.
   #'''
   #try:
      #for fn in fnlist:
         #text = ''
         #with open(fn) as f:
            #text+=f.read()
      #with open(outname, mode='wt') as outfile:
         #outfile.write(text)
   #except Exception as e:
      #print(e)

def gen_tuple(fn):
   '''
   Exercicio 3 - Python para desenvolvedores
   Lê um arquivo csv e retorna seu conteúdo em tupla. Linhas vazias serão eliminadas.
   A função retorna uma expressão geradora. Em um objeto gerador cada item é gerado somente quando
   é necessário (não se cria uma lista antes, a lista é criada on the fly a cada iteração) o que
   permite economizar memória.'''
   try:
      with open(fn) as f:
         text = map(str.rstrip, f.readlines())
   except Exception as e:
      print(e)
      return None
   else:
      return (tuple(line.split(',')) for line in text if line)

def gen_dict(fn):
   '''Lê um arquivo csv e retorna um gerador de dicionários das linhas.'''
   try:
      with open(fn) as f:
         text = map(str.rstrip, f.readlines())
   except Exception as e:
      print(e)
      return None
   else:
      header, *data = filter(bool, text)
      return (dict(zip(header.split(','),record.split(','))) for record in data if record)

def info(fn):
   '''Exibe informações sobre o arquivo fornecido'''
   try:
      with open(fn) as f:
         text = f.read()
      return "%s : %d char(s), %d linha(s) e %d palavra(s)." \
              %(fn, len(text), text.count("\n"), len(text.split()))
   except Exception as e:
      print(e)

def deprecated_read_csv(fn):
   '''Lê um arquivo csv e retorna uma lista de dicionários das linhas.'''
   try:
      with open(fn) as f:
         header, *data = [ line.rstrip().split(',') for line in f if line]
   except (IOError,UnicodeDecodeError) as e:
      print(e)
   else:
      return [ dict(zip(header,record)) for record in data ]
def deprecated_csv_to_dict(fn):
   '''
   Primeiramente o conteúdo do arquivo lido é dividido entre a primeira posição (o header com nome
   de todos os campos) e os dados. Nesse processo as funções rstrip() e split(',') cuidam de tirar
   os caracteres fim de linha e dividir a string (separador ',') e trasformar em lista.

   Neste momento os dados estão da seguinte forma:

   header -> ['nome','cadastro', ....]
   data   -> [['Antonio Sergio','10008121205', ...], ['Goncalves Jr.','84421541241', ...], ...]

   O próximo passoo é criar um dicionário que a chave seja um campo principal ('cadastro' no
   meu caso) e o valor seja a representação do registro em forma de dicionário. A variável datalist
   receberá uma lista de dicionários de cada registro. A função zip trata de combinar o nome dos
   campos com os valores.

   datalist -> [ {'nome':'Antonio Sergio','cadastro':'10008121205',...},
                 {'nome':'Goncalves Jr.' ,'cadastro':'84421541241',...},
                ... ]

   Finalmente é retornado outro dicionário no seguinte formato:
   { '10008121205': {'nome':'Antonio Sergio', 'cadastro':'10008121205', ....},
     '84421541241': {'nome':'Goncalves Jr.' , 'cadastro':'84421541241', ....},
      ... }

   '''
   try:
      with open(fn) as f:
         header, *data = [ line.rstrip().split(',') for line in f if line]
   except (OSError,UnicodeDecodeError) as e:
      print(e)
   else:
      datalist = [ dict(zip(header,record)) for record in data ]
      return { rec['cadastro']:rec for rec in datalist }


