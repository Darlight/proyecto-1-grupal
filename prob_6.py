def prob_6(list1):
	for orden in range(len(list1)-1,0,-1):
		for descendencia in range(orden):
				if list1[descendencia] > list1[descendencia + 1]:
					mayor = list1[descendencia]
					list1[descendencia] = list1[descendencia + 1]
					list1[descendencia + 1] = mayor
	return list1

list1 = [66,123,423,4523,665,73,133,34,21,234]
print(prob_6(list1))


