
value = input()
numList = [0]*10

for i in range(len(value)):
    num = int(value[i])
    if num == 6 or num == 9:
        if numList[6] <= numList[9]:
            numList[6] += 1
        else:
            numList[9] += 1
    else:
        numList[num] += 1


    
printNum = max(numList)
print(printNum)
