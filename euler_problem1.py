#Euclid Problem 1
import math
j=0;
for x in xrange(0,1000,1):
	if (x%3 == 0 or x%5==0):
		j += x;
print(j);
	