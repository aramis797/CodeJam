from sys import stdin
T=int(stdin.next())
for _t in range(1,T+1):
	F=[];S=[]
	r1=int(stdin.next())-1
	for i in range(4):
		F.append([int(x) for x in stdin.next().strip().split()])
	r2=int(stdin.next())-1
	for j in range(4):
		S.append([int(x) for x in stdin.next().strip().split()])
	count=0;res=0
	for i in F[r1]:
		for j in S[r2]:
			if(i==j):
				res=i
				count+=1
	if(count==0):
		print "Case #%d: %s"%(_t,"Volunteer cheated!")
	elif(count==1):
		print "Case #%d: %d"%(_t,res)
	else:
		print "Case #%d: %s"%(_t,"Bad magician!")