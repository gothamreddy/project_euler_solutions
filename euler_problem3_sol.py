#Euclid_Problem3.py
#calculate the largest prime factor
import math
test = 3561669;
i=2;
j=0;
#function to check if it's prime number.
def primecheck(primechecknumber):
	limit = int(math.sqrt(primechecknumber))
	for i in xrange(2, limit+1):
		if(primechecknumber%i==0):
			return False;
	return True;
	
for i in xrange(2, test):
	if(test%i==0):
		if(primecheck(i)==True):
			j=i;
		else:
			continue;
print(j);

			
