from sys import stdin
for _t in range(1,int(stdin.next().strip())+1):
	D = {'abc':'2','def':'3','ghi':'4','jkl':'5','mno':'6','pqrs':'7','tuv':'8','wxyz':'9'}
	D1 = {' ':'0'}
	for (i,j) in D.items():
		for (k,l) in enumerate(i):
			D1[l] = (k+1) * j
	line = stdin.next()[:-1]
	out = D1[line[0]]
	print "Case #"+str(_t)+":",
	if len(line) > 1:
		for char in line[1:]:
			if out[-1] == D1[char][0]:
				out += ' '
			out += D1[char]
	print out