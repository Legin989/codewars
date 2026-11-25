def max_multiple(divisor, bound):
	n = bound
	while True:
		if (n % divisor) == 0:
			break
		else:
			n -= 1
	return n
print(max_multiple(2, 5))