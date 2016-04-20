import random
def FermatPrimalityTest(number):
    ''' if number != 1 '''
    if (number > 1):
        ''' repeat the test few times '''
        for time in range(3):
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number)-1
            
            ''' Test if a^(n-1) = 1 mod n '''
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False
        
        return True
    else:
        ''' case number == 1 '''
        return False


print FermatPrimalityTest(99194853094755497)