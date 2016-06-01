def prob_13(n):
	res=0
	i=1
	while i<=n+1:
		if n%i==0:
			res=res+i
		i=i+1
	return res