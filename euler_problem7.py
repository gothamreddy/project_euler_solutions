import math
def primecheck(primechecknumber):
	limit = int(math.sqrt(primechecknumber));
	for i in xrange(2, limit+1):
		if(primechecknumber%i==0):
			return False;
	return True;

i = 1;
p = 3;

while i < 10001:
	if(primecheck(p) == True):
		currentPrime = p;
		i += 1;
		p += 2;
	else:
		p += 2;

print(currentPrime)
