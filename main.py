# Task 1 

# firstElem, step, listLen = list(map(int, (input().split())))

# Resultlist = []
# Resultlist.append(firstElem)

# for i in range(1, listLen):
#     Resultlist.append(Resultlist[i-1] + step)

# print(Resultlist)

# Task 2

import random

rangeStart, rangeFinish = list(map(int, (input().split())))
list_1 = []
result = []

for i in range(15):
    list_1.append(random.randint(-20,20))

print(list_1)

for i in range(len(list_1)):
    if list_1[i] >= rangeStart and list_1[i] < rangeFinish:
        result.append(i)

print(result)