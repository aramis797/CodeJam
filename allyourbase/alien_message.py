def get_base(inp):
	temp=[]
	temp.append(inp[0])
	for i in range(1,len(inp)):
		if inp[i] not in temp:
			temp.append(inp[i])
		else:
			continue
	return temp
def get_digits(inp,base):
	dic=dict()
	dic[inp[0]]=1
	temp1=[]
	temp1.append(inp[0])
	count=1
	loc=0
	for i in range(1,len(inp)):
		while(count<=base and(inp[i] not in temp1)):
			dic[inp[i]]=loc
			if(loc==0):
				loc+=2
			else:
				loc+=1
			count+=1
			temp1.append(inp[i])
	return dic
def get_outlist(inp,dic):
	outlist=[]
	for i in range(len(inp)):
		outlist.append(dic[inp[i]])
	return outlist
def get_seconds(outlist,base):
	sec=0
	po=len(outlist)-1
	for i in range(len(outlist)):
		sec+=(outlist[i]*pow(base,po))
		po-=1
	return sec
inp = raw_input("Enter your criptic message:-")
temp= get_base(inp)
base=len(temp)
print base
print temp
dic =  get_digits(inp,base)
print dic
outlist= get_outlist(inp,dic)
print outlist
seconds=get_seconds(outlist,base)
print seconds