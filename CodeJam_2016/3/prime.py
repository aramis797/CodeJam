def Primes(N):
	A=[0];loop=0;out = []
	for i in xrange(N):
		A.append(1)
	for j in range(2,N/2+1):
		for k in range(2,N/j+1):
			loop += 1
			A[j*k] = 0
	for i in xrange(2,N+1):
		if A[i]:
			out.append(i)
	return out
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
print Primes()