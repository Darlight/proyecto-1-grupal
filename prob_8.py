def prob_8(c):
	resultado = ""
	n = c
	for i in range(0, c):
		resultado += " " * (c - i - 1) + "* " * (i+1) + "\n"
		n = n - 1
	return resultado

