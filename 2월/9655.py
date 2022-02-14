
n = int(input())
winList = [0]
i = 0

while n != 0:
    i += 1
    if n //3 == 0:
        n -= 1
    else :
        n -= 3
    
    if i % 2 == 1:

        winList.append("SK") 
    else:
        winList.append("CY")

print(winList[-1])