#Euclid_Problem3.py
#calculate the largest prime factor
import math
test = 235616693;
i=2;
j=0;
#function to check if it's prime number.
def primecheck(primechecknumber):
	limit = int(math.sqrt(primechecknumber))
	for i in xrange(2, limit+1):
		if(primechecknumber%i==0):
			return False;
	return True;
if(primecheck(test)==True):
	print(test);
else:	
	for i in xrange(2, int(math.sqrt(test))):
		if(test%i==0):
			if(primecheck(i)==True):
				j=i;
			else:
				continue;
	print(j);

			
