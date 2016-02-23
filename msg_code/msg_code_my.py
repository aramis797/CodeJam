import string
dict = {' ':0,'abc':2,'def':3,'ghi':4,'jkl':5,'mno':6,'pqrs':7,'tuv':8,'wxyz':9}
def get_pos(ch,msg,dict):
    p=[10,10]
    if ch==" ":
        p[0]=0
        p[1]=0
        return p
    else:
        sam = sorted(dict.keys())
        for i in range(len(sam)):
            for j in range(len(sam[i])):
                if(ch==sam[i][j]):
                    p[0]=i
                    p[1]=j
        return p
def get_for_digit(q):
    if q[0]==0:
        return 0
    else:
        temp=q[0]+1
        q[0]=(q[0]+1)*10
#        digits=sorted(dict.values())
        for i in range(q[1]):
            q[0]=(q[0]+temp)*10
#            q[0]=q[0]*10
        return q[0]/10
def get_out(msg):
    out=str(get_for_digit(get_pos(msg[0],msg,dict)))
    for i in range(1,len(msg)):
        if(get_pos(msg[i-1],msg,dict)[0]==get_pos(msg[i],msg,dict)[0]):
            out=out+" "+str(get_for_digit(get_pos(msg[i],msg,dict)))
        else:
            out=out+str(get_for_digit(get_pos(msg[i],msg,dict)))
    return out
print "Enter no. of test cases:-\t"
n=input()
ins={}
for i in range(n):
	print "Test Case: "+str(i+1)
	test=raw_input()
	print get_out(test)
#print get_digit(test[0],test,dict)
#for i in range(len(test)):

#for l in range(result[]):

#print dict['abc']
#for i in range(len(test)):
#0-" "
#2-abc
#3-def
#4-ghi
#5-jkl
#6-mno
#7-pqrs
#8-tuv
#9-wxyz
