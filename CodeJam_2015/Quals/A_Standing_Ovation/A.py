from sys import stdin
for _t in range(1,int(stdin.next().strip())+1):
	S,N=(str(x) for x in stdin.next().split())
	S = int(S)
	ovation_count_till_now = int(N[0])
	out = 0
	for i in xrange(1,S+1):
		if ovation_count_till_now < i and int(N[i])>0:
			temp = i - ovation_count_till_now
			ovation_count_till_now += temp
			out += temp
			ovation_count_till_now += int(N[i])
		else:
			ovation_count_till_now += int(N[i])
	print "Case #"+str(_t)+":",out