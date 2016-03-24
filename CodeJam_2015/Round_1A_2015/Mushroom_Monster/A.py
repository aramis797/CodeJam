from sys import stdin
for _t in xrange(1,int(stdin.next().strip())+1):
	N = int(stdin.next().strip())
	M = [int(x) for x in stdin.next().split()]
	out1=0;out2=0
	for i in xrange(1,N):
		if M[i] < M[i-1]:
			out1 += M[i-1]-M[i]
	#to get rateof eating for 10 secs
	for i in xrange(N-2,-1,-1):
		if M[i] == M[i+1] and M[i] != 0 and M[i+1] != 0:
			rate = 0
			break
		else:
			rate = M[i],M[i]-M[i+1]
			break
	if rate ==0:
		out2 = 0
	else:
		for i in xrange(N-1):
			if M[i] > rate:
				out2 += rate
			else:
				out2 += M[i]
	print "Case #"+str(_t)+":",out1,out2