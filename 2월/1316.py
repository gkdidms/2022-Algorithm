
strNum = int(float(input()))
groupWordCount = 0
for i in range(strNum) :
    word = list(input())
    wordList = [0]*len(word)
    flag = True
    if len(word) == 1:
        groupWordCount += 1
    else :

        for j in range(len(word) - 1):
            if word[j] != word[j+1]:
                for k in wordList:
                    if word[j] in str(k):
                        flag = False
                wordList[j] = word[j]

            if flag == False:
                break

            if j == len(word) - 2:
                for k in wordList:
                    if word[j+1] in str(k):
                        flag = False
                
                if flag == False:
                    break

                else :
                    groupWordCount += 1

print(groupWordCount)