# Task 1 

firstElem, step, listLen = list(map(int, (input().split())))

Resultlist = []
Resultlist.append(firstElem)

for i in range(1, listLen):
    Resultlist.append(Resultlist[i-1] + step)

print(Resultlist)