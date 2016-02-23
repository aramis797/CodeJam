from sys import stdin
T9R = {'2':'abc','3':'def', '4': 'ghi', '5':'jkl', '6':'mno','7':'pqrs', '8':'tuv', '9':'wxyz','0':' '}
T9={}
for k,v in T9R.items():
	for i,c in enumerate(v):
		T9[c]=k*(i+1)
T=int(stdin.next())
for t in range(T):
	M=stdin.next().strip('\n')
	KP=T9[M[0]]
	for c in M[1:]:
		kp=T9[c]
		if(kp[0] == KP[-1]):
			KP+=' '
		KP+=kp
	print 'Case #%d: %s' %(t+1,KP)
