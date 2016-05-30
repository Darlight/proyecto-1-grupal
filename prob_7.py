def prob_7():
	i=0
	lista=[]
	while i<1001:
		if i%4==0 or i%7==0:
			lista.append(i)
		i=i+1
	print(lista)
