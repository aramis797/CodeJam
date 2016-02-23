from sys import stdin
for _t in range(1,int(stdin.next().strip())+1):
	inp = [x for x in stdin.next().split()]
	print "Case #"+str(_t)+":",
	for word in inp[::-1]:
		print word,
	print