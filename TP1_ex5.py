#TrabalhoPratico_exercicio5

import math

a = 6378160
E = 0,00669454185

def coordenadas(x, y, z):
	P = math.sqrt(x**2 - y**2)
	N = a/(math.sqrt(1-E))
	longitude = math.atan(y/x)
	latitude = 

print "digite x"
x = float(raw_input())

print "digite y"
y = float(raw_input())

print "digite z"
z = float(raw_input())

print coordenadas(x, y, z)