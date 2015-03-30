#TrabalhoPratico_exercicio3

import math

def coordenadapolares(x, y):
	r = math.sqrt(math.pow(x,2) + math.pow(y,2))
	if r == 0:
		print "coordenadas polares (%d " %r %",qualquer angulo)"
	else:
		cosseno = math.acos(x/r)
		seno = math.asin(y/r)
		print cosseno
		print seno
		#print "coordenadas polares (%d " %r "%s,%f" %cosseno "%s)"

print "digite x"
x = int(raw_input())

print "digite y"
y = int(raw_input())

print coordenadapolares(x, y)