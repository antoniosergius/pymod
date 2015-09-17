#!/usr/bin/env python3.4
#
#  sparsemat.py
#  
#  Impressão de uma matriz esparsa utilizando estrutura de dicionário.
#  
#  Copyright 2015 Antônio Sérgio Garcia Ferreira <serginho@serginho-desktop>
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
def dictway():
	dim = 6, 12
	mat = {}

	mat[3,7] = 3
	mat[4,6] = 5
	mat[6,3] = 7
	mat[5,4] = 6
	mat[2,9] = 4
	mat[1,0] = 9
	print()

	for lin in range(dim[0]):
		for col in range(dim[1]):
		
			# metodo get(chave, valor) retorna o valor da chave no 
			# dicionário ou se a chave não existir, retorna o segundo 
			# argumento
		
			print(mat.get((lin,col), 0), end=' ')
		
			# no comando acima o primeiro argumento de get é uma tupla
			# que contem a linha e a coluna da matriz. Essas últimas 
			# são em conjunto a chave do dicionário mat; já o segundo 
			# argumento é o valor que irá ser retornado caso a chave 
			# fornecida não esteja no dicionário mat.
		print()
	print(end='\n\n')	

def stringway():
	matriz = '''0 0 0 0 0 0 0 0 0 0 0 0 
	9 0 0 0 0 0 0 0 0 0 0 0
	0 0 0 0 0 0 0 0 0 4 0 0
	0 0 0 0 0 0 0 3 0 0 0 0
	0 0 0 0 0 0 5 0 0 0 0 0 
	0 0 0 0 6 0 0 0 0 0 0 0'''
	
	mat = {}
	
	# Quebra a matriz em linhas
	for row, line in enumerate(matriz.splitlines()):

		# Quebra a linha em colunas
		for col, column in enumerate(line.split()):
			
			# Converte em inteiro a coluna
			column = int(column)
			
			# Se a coluna for diferente de zero (zero == False)
			if column: 
				mat[row, col] = column
	print(mat)
	print("Tamanho da matriz completa ", (row+1) * (col+1))
	print("Tamanho da matriz esparsa ", len(mat), end='\n\n')


dictway()
stringway()

