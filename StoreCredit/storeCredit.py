from sys import stdin
for _t in xrange(1,int(stdin.next().strip())+1):
	C = int(stdin.next().strip())
	L = int(stdin.next().strip())
	items_price_list = [int(x) for x in stdin.next().split()]
	temp = sorted(items_price_list)
	left = 0;right = L-1
	(i,j)=(0,0)
	while(True):
		S = temp[left] + temp[right]
		if(S == C):
			(i,j) = (left,right)
			break
		elif(S < C):
			left += 1
		else:
			right -=1
	(i,j) = (items_price_list.index(temp[i]),items_price_list.index(temp[j]))
	if i == j:
		i += 1
		j += 2
	elif i < j:
		(i,j) = (i+1,j+1)
	else:
		(i,j) = (j+1,i+1)
	print "Case #"+str(_t)+":",i,j