#eulerProbelm4 - palindrome.py
testlist = [];
for counter in range(999, 100, -1):
	for counter2 in range(999, 100, -1):
		if counter2 > counter:
			continue;
		p = counter*counter2
		s = str(p)[::-1]
		s = int(s);
		if p == s:
			testlist.append(p);
print(max(testlist));			