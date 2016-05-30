def prob_3(base,potencia):
	res=base
	for i in range (potencia-1):
		res=base*res
	return res