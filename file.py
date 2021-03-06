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
import csv
import time

def rem_empty_lines(fn):
    ''' Remove linhas vazias de um arquivo e salva o conteúdo modificado'''
#    start = time.time()
    try:
        with open(fn, mode='r+') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if line != '\n':
                    f.write(line)
            f.truncate()
    except Exception as e:
        print(e)
#    finally:
#        print(time.time() - start)

def split(fn, nbytes):
   '''
   Exercicio 4.1 - Python para desenvolvedores.
   Divide o arquivo fn em arquivos de tamanho igual a nbytes.
   Uma divisão de um arquivo nomeado 'arq' ficará da seguinte maneira:
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
         with open("{}_{:03d}".format(fn,parts), 'wb') as fout:
            fout.write(out.encode('utf8'))
         parts += 1
   except Exception as e:
      print(e)

def join(new, ls):
   '''
   Exercício 4.2 - Python para desenvolvedores
   Junta os arquivos da lista 'ls' em um único arquivo 'new'.
   '''
   try:
      out = [chunk for chunk in gen_chunks(ls,mode='rb')]
      with open(new,'wb') as fout:
         fout.writelines(out)
   except Exception as e:
      print(e)

def gen_lines(ls, mode='rt'):
   '''
   Gerador de linhas de uma lista de arquivos
   O usuário fornece uma lista 'ls' com o nome dos arquivos.
   Em seguida é gerada cada linha de cada arquivo em ordem.
   '''
   for filename in ls:
      with open(filename, mode) as f:
         for line in f:
            yield line

def gen_chunks(ls, mode='rt'):
   '''
   Gerador de arquivos
   O usuário fornece uma lista 'ls' com o nome dos arquivos.
   Em seguida é lido cada arquivo com uma única operação f.read(),
   o que difere de f.readline() que lê linha por vez.
   '''
   for filename in ls:
      with open(filename, mode) as f:
         yield f.read()

def csv_list_gen(fn):
   '''Lê um arquivo csv e retorna seu conteúdo em forma de lista'''
   try:
      with open(fn) as f:
         csv_reader = csv.reader(f)
         headers = next(csv_reader)
         for row in csv_reader:
            yield row
   except Exception as e:
      print(e)

def csv_dict_gen(fn):
   '''Lê um arquivo csv e retorna seu conteúdo em forma de dicionário'''
   try:
      with open(fn) as f:
         csv_reader = csv.DictReader(f)
         for row in csv_reader:
            yield row
   except Exception as e:
      print(e)

def info(filename):
   '''Exibe informações sobre o arquivo fornecido'''
   try:
      content = next(gen_chunks([filename]))
      return "{}: {} char(s), {} linha(s) e {} palavra(s)"\
            .format(filename,
                    len(content),
                    content.count("\n"),
                    len(content.split()))
   except Exception as e:
      print(e)

#def rem_dup_lines(fn):
    #''' Remove linhas vazias de um arquivo e salva o conteúdo modificado'''
    #start = time.time()
    #try:
        #with open(fn) as f:
            #content = list(filter(bool, f.read().split('\n')))
        #with open(fn, mode='w+') as f:
            #for line in content:
                #f.write(line)
                #f.write('\n')
    #except Exception as e:
        #print(e)
    #finally:
        #print(time.time() - start)


#def csv_tuple_deprecated(fn):
   #'''
   #Exercicio 3 - Python para desenvolvedores
   #Lê um arquivo csv e retorna seu conteúdo em tupla. Linhas vazias serão eliminadas.
   #A função retorna uma expressão geradora. Em um objeto gerador cada item é gerado somente quando
   #é necessário (não se cria uma lista antes, a lista é criada on the fly a cada iteração) o que
   #permite economizar memória.'''
   #try:
      #with open(fn) as f:
         #for line in f:
            #line = line.rstrip()
            #if line:
               #yield tuple(line.split(','))
   #except Exception as e:
      #print(e)

#def csv_dict_deprecated(fn):
   #'''
   #Lê um arquivo csv e retorna um gerador de dicionários das linhas.
   #A função zip junta dois campos de duas estruturas de dados diferentes
   #em uma única.
   #'''
   #try:
      #with open(fn) as f:
         #header = f.readline().rstrip()
         #for line in f:
            #line = line.rstrip()
            #if line:
               #yield dict(zip(header.split(','),line.split(',')))
   #except Exception as e:
      #print(e)

#def info(filename):
   #'''Exibe informações sobre o arquivo fornecido'''
   #try:
      #with open(filename) as f:
         #text = f.read()
      #out = "{}: {} char(s), {} linha(s) e {} palavra(s)"\
            #.format(filename,
                    #len(text),
                    #text.count("\n"),
                    #len(text.split())
                    #)
      #return out
   #except Exception as e:
      #print(e)

#def split_text(fn, nbytes):
   #'''
   #Exercicio 4 - Python para desenvolvedores.
   #Divide o arquivo fn em nbytes e grava em novos arquivos. Se o arquivo for arq, será gravado
   #arq_001, arq_002, etc..'''
   #try:
      #with open(fn) as f:
         #count=1
         #stream = f.read(nbytes)
         #while stream:
            #with open("{}_{:03d}".format(fn,count), 'wt') as fout:
               #fout.write(stream)
            #stream = f.read(nbytes)
            #count+=1
   #except Exception as e:
      #print(e)

#def join_text(new, ls):
   #'''
   #Exercício 4 - Python para desenvolvedores - metodo sem concatenação de strings
   #Juntar os arquivos da lista fnlist em um unico arquivo outname e gravar no disco.
   #'''
   #try:
      #out = [chunk for chunk in gen_chunks(ls)]
      #with open(new,'wt') as fout:
         #fout.writelines(out)
   #except Exception as e:
      #print(e)

#def join(new, ls):
   #'''
   #Exercício 4 - Python para desenvolvedores - metodo sem concatenação de strings
   #Juntar os arquivos da lista fnlist em um unico arquivo outname e gravar no disco.
   #'''
   #try:
      #out = []
      #for fn in ls:
         #with open(fn,'rb') as f:
            #out.append(f.read())
      #with open(new,'wb') as fout:
         #fout.writelines(out)
   #except Exception as e:
      #print(e)

#def gen_dict(fn):
   #'''Lê um arquivo csv e retorna um gerador de dicionários das linhas.'''
   #try:
      #with open(fn) as f:
         #text = map(str.rstrip, f.readlines())
   #except Exception as e:
      #print(e)
      #return None
   #else:
      #header, *data = filter(bool, text)
      #return (dict(zip(header.split(','),record.split(','))) for record in data if record)

#def deprecated_read_csv(fn):
   #'''Lê um arquivo csv e retorna uma lista de dicionários das linhas.'''
   #try:
      #with open(fn) as f:
         #header, *data = [ line.rstrip().split(',') for line in f if line]
   #except (IOError,UnicodeDecodeError) as e:
      #print(e)
   #else:
      #return [ dict(zip(header,record)) for record in data ]

#def deprecated_csv_to_dict(fn):
   #'''
   #Primeiramente o conteúdo do arquivo lido é dividido entre a primeira posição (o header com nome
   #de todos os campos) e os dados. Nesse processo as funções rstrip() e split(',') cuidam de tirar
   #os caracteres fim de linha e dividir a string (separador ',') e trasformar em lista.

   #Neste momento os dados estão da seguinte forma:

   #header -> ['nome','cadastro', ....]
   #data   -> [['Antonio Sergio','10008121205', ...], ['Goncalves Jr.','84421541241', ...], ...]

   #O próximo passoo é criar um dicionário que a chave seja um campo principal ('cadastro' no
   #meu caso) e o valor seja a representação do registro em forma de dicionário. A variável datalist
   #receberá uma lista de dicionários de cada registro. A função zip trata de combinar o nome dos
   #campos com os valores.

   #datalist -> [ {'nome':'Antonio Sergio','cadastro':'10008121205',...},
                 #{'nome':'Goncalves Jr.' ,'cadastro':'84421541241',...},
                #... ]

   #Finalmente é retornado outro dicionário no seguinte formato:
   #{ '10008121205': {'nome':'Antonio Sergio', 'cadastro':'10008121205', ....},
     #'84421541241': {'nome':'Goncalves Jr.' , 'cadastro':'84421541241', ....},
      #... }

   #'''
   #try:
      #with open(fn) as f:
         #header, *data = [ line.rstrip().split(',') for line in f if line]
   #except (OSError,UnicodeDecodeError) as e:
      #print(e)
   #else:
      #datalist = [ dict(zip(header,record)) for record in data ]
      #return { rec['cadastro']:rec for rec in datalist }

#def gen_tuple(fn):
   #'''
   #Exercicio 3 - Python para desenvolvedores
   #Lê um arquivo csv e retorna seu conteúdo em tupla. Linhas vazias serão eliminadas.
   #A função retorna uma expressão geradora. Em um objeto gerador cada item é gerado somente quando
   #é necessário (não se cria uma lista antes, a lista é criada on the fly a cada iteração) o que
   #permite economizar memória.'''
   #try:
      #with open(fn) as f:
         #text = map(str.rstrip, f.readlines())
   #except Exception as e:
      #print(e)
      #return None
   #else:
      #return (tuple(line.split(',')) for line in text if line)
