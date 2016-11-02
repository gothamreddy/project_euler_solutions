'''import math
number = 17;
j = 2;
for x in xrange(2,number/2,1):
	if(number%x==0):
		while(j < math.sqrt(x)):
			if(x%j!=0):
				j += 1;
			else:
				break;
	else:
		continue;'''

'''def primecheck(primechecknumber):
	i=2;
	for i in range(2,int(math.sqrt(primechecknumber))):
		if(primechecknumber%i==0):
			return False;
	return True;'''

import math

def primecheck(primechecknumber):
	limit = int(math.sqrt(primechecknumber));
	for i in xrange(2, limit+1):
		if(primechecknumber%i==0):
			return False;
	return True;


if(primecheck(6)):
	print("yes! It's a prime!");
else:
	print("it's not a prime");
