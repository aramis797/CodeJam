from sys import stdin
T = int(stdin.next())
for _t in xrange(1,T+1):
	num_red=0
	num_blue=0
	answer=0
	N,K,B,T=tuple([int(x) for x in stdin.next().strip().split()])
	X=[int(x) for x in stdin.next().strip().split()]
	V=[int(x) for x in stdin.next().strip().split()]
	for i in range(N):
		if num_red == K:
			break
		if ((X[i]+ T*V[i]) < B):
			num_blue+=1
		else:
			num_red+=1
			answer+=num_blue
	if num_red >= K:
		print answer
	else:
		print "IMPOSSIBLE"