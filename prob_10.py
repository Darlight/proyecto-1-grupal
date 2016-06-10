def prob_10(a,b,c):
	import math
	d1 = math.sqrt( (( (b[0] - a[0]) **2)) + ((b[1] - a[1]) **2) )
	d2 = math.sqrt( (( (c[0] - a[0]) **2)) + ((c[1] - a[1]) **2) )
	d3 = math.sqrt( (( (b[0] - c[0]) **2)) + ((b[1] - c[1]) **2) )

	equi ="Es Equiletaro"
	isos = "Es Isosceles "
	esc = "Es Escaleno"
	
	if d1 == d2 and d2 == d3 and d3 == d1:
		return equi
	elif d1 == d2 or d2 == d3 or d1 == d3:
		return isos
	elif d1 != d2 or d1 != d3 or d2 != d3:
		return esc