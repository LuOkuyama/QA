#TrabalhoPratico_exercicio4

import math

def triangulo(A, B, C):
	if C < A + B:
		print "eh um quadrado"
		area = (A * B)/2
		print area
	else:
		print "nao eh um quadrado"
		print A 
		print B
		print C

print "digite cateto A"
A = int(raw_input())

print "digite cateto B"
B = int(raw_input())

print "digite hipotenuza C"
C = int(raw_input())

print triangulo(A, B, C)