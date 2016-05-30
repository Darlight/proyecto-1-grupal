#Problema 4
def prob_4(n,palabra):
	len(palabra)
	izquierda = (n-len(palabra))//2
	derecha = n -(izquierda + len(palabra))
	return ("*"*izquierda+palabra+"*"*derecha)
