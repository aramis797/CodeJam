from sys import stdin
T=int(stdin.next())
for _t in range(1,T+1):
	existed=['/']
	out=0
	M=stdin.next().strip('\n').split()
	for i in range(int(M[0])):
		temp=stdin.next().strip('\n').split('/')
		del temp[0]
		var=''
		for name in temp:
			var+='/'+name
			if(var not in existed):
				existed.append(var)
	for j in range(int(M[1])):
		temp=stdin.next().strip('\n').split('/')
		del temp[0]
		var=''
		for new in temp:
			var+='/'+new
			if(var not in existed):
				out+=1
				existed.append(var) 
	print "Case #%d: %d"%(_t,out)
