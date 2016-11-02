#euclid_problem2.py
#Calculate the sum of all even fibonacci numbers not greater than 4 million
import math
i = 0;
j = 1;
t = 0;
p = 0;
while i+j <= 4000000:
	t = i+j;
	i = j;
	j = t;
	if t%2 == 0:
		p += t;
		#print(t);
print(p);	
