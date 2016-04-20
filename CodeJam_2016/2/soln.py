from sys import stdin
def solution(cakes):
	if len(cakes) == 0:
		return 0
	elif len(cakes) == 1:
		if cakes[0] == '-':
			return 1
		else:
			return 0
	if '-' not in cakes:
		return 0

for _t in range(1,int(stdin.next().strip())+1):
	cakes = list(stdin.next().strip())
	cakes.reverse()
	while cakes and cakes[0] == '+':
		cakes.remove('+')
	cakes.reverse()
	print len(cakes),cakes,solution(cakes)
	#print solution(cakes)
	#print "Case #"+str(_t)+":",