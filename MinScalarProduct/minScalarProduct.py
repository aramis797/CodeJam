from sys import stdin
for _t in range(1,int(stdin.next().strip())+1):
	n = int(stdin.next().strip())
	V1 = [int(x) for x in stdin.next().split()]
	V2 = [int(x) for x in stdin.next().split()]
	V1 = sorted(V1)
	V2 = sorted(V2,reverse=True)
	minProduct = 0
	for i in xrange(n):
		minProduct += V1[i] * V2[i]
	print "Case #"+str(_t)+":",minProduct