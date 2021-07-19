"""Ch3: Longest increasing substring exercise"""
# = [0,   1,  2,  3,  4,  5,  6,  7,  8]
x = [12, 45, 32, 65, 78, 23, 35, 45, 57]

"""
Exercise: Design an algorithm that finds the longest sub-sequence 
x[i:j] such that consecutive numbers are increasing, i.e. 
x[k] < x[k+1] for all k in range(i,j) (or one of the longest, 
if there are more than one with the same length).
"""

def longest(x):
	result = []

	for i in range(len(x)):
		tmp = [x[i]]
		k = i
		# while k != 8 then we can also evaluate x[k] <= x[k+1]
		while k != len(x) - 1 and x[k] <= x[k+1]:
			tmp.append(x[k + 1])
			k += 1
		if len(tmp) >= len(result):
			result = tmp
	return result

print(longest(x))
