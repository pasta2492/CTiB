"""Ch3: Sieve of Eratosthenes"""
def eratosthenes(n):
	candidates = list(range(2, n + 1))
	primes = []

	while candidates != []:
		p = candidates.pop(0)

		for i in range(0, len(candidates)-2):
			if candidates[i] % p == 0:
				candidates.remove(candidates[i])
		primes.append(p)

	return primes
