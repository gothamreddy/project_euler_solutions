import math

p = 0;
q=0;
for i in range(1,101,1):
	p += i;
p = math.pow(p,2);

for i in range(1,101,1):
	q += math.pow(i,2);

print(p-q);
