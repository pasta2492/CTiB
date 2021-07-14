digits = {}

for i in range(0,10):
	digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'

def base16(n):
	b = 16
	lst = []
	result = n // b
	remainder = n % b
	lst.append(digits[remainder])
	while result != 0:
		n = result
		result = n // b
		remainder = n % b
		lst.append(digits[remainder])
	return lst[::-1]
