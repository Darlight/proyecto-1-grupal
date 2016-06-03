def prob_10(a,b,c):
	equi ="Es Equiletaro"
	isos = "Es Isosceles "
	esc = "Es Escaleno"
	
	if a[0] == b[0] and b[0] == c[0] and a[1] == b[1] and b[1] == c[1]:
		return equi
	elif a == b or a == b or b == c:
		return isos
	elif a != b or a != c or b != c:
		return esc



a = (2,2)
b = (2,2)
c =	(2,2)