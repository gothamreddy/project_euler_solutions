chainlenlist = []
count = 1
maxnum = 0
number = 0
for i in range(2,1000000):
    dispnum = i
    while(dispnum!=1):
        if(dispnum%2==0):
            dispnum = dispnum/2
            count += 1
        else:
            dispnum = 3*dispnum+1
            count += 1
    if(count>maxnum):
        maxnum = count
        number = i
    count = 1
print(number)

