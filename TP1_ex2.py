#TrabalhoPratico_exercicio2

import math

def distancia(P1x1, P1y1, P2x2, P2y2):
	d = math.sqrt(math.pow((P1x1-P2x2),2) + math.pow((P1y1-P2y2),2))
	print "distancia = %f" %d

Lista = []
Q = True
while Q:
	print "digite ponto P(x,y) (exemplo: 1,2):"
	Ponto = raw_input().split(",")
	Lista.append((int(Ponto[0]), int(Ponto[1])))
	print "continua? (s/n)"
	Sair = raw_input()
	if Sair == "n":
		Q = False

print Lista

dmaior = 0

for item1 in xrange(0, len(Lista)-2):
	for item2 in xrange(1,len(Lista)-1):
		d = distancia(item1[0], item1[1], item2[0],item2[1])
		if d > dmaior:
			dmaior = d

print dmaior








# print distancia(P1x1, P1y1, P2x2, P2y2)


# # -*- coding: utf-8 -*-

# from math import sqrt
# from math import pow

# t1 = (0,0)
# t2 = (1,1)
# t3 = (2,2)
# dm = 0
# lista = [t1, t2, t3]

# def distancia( t1, t2 ):
#    "This function return the distance between two points"
#    d = sqrt( pow(t1[0] - t2[0], 2) + pow(( t1[1] - t2[1] ), 2) )
#    return d

# for x in xrange(0,len(lista)-1):
# 	for y in xrange(1,len(lista)):
# 		d = distancia(lista[x], lista[y])
# 		if d > dm:
# 		  dm = d
# 		print x, y


# print "================================="
# print "Resultado final e: ", dm
# print "FIM"