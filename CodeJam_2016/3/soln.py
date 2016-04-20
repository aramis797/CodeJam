from sys import stdin
from operator import add
import random
def isPrime(number):
    if (number > 1):
        for time in range(3):
            randomNumber = random.randint(2, number)-1
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False
        
        return True
    else:
        ''' case number == 1 '''
        return False
def isValid(A):
	for number in A:
		if isPrime(number):
			return False
	return True
# A = [55, 337, 1301, 3781, 9115, 19265, 36937, 65701, 110111]
# B = [51, 328, 1285, 3756, 9079, 19216, 36873, 65620, 110011]
for _t in range(1,int(stdin.next().strip())+1):
	N,J = (int(x) for x in stdin.next().split())
	# print N,J
	coins = []
	#N = 4
	# for i in xrange(pow(2,N-1),pow(2,N)):
	# 	temp =  bin(i)[2:]
	# 	if temp.endswith('1'):
	# 		coins.append(temp)
	final = [];index = 0
	N = pow(2,N-1)
	factors = xrange(2,int(8589934593**0.5)+1)
	while len(final) < J:
		#print N,temp
		temp = bin(N)[2:]
		if temp.endswith('1'):
			coin = temp	
			values = []
			for base in xrange(2,11):
				values.append(int(coin,base))
			if isValid(values):
				outL = []
				#print values
				#factors = xrange(2,int(max(values)**0.5)+1)
				for num in values:
					for factor in factors:
						if num % factor == 0:
							outL.append(factor)
							break
					# outL.append(prime_factors(num)[0])
				final.append((coin,outL))
			N += 1
		else:
			N += 1
	print "Case #"+str(_t)+":"
	for i in final:
		print i[0],
		for j in i[1]:
			print j,
		print