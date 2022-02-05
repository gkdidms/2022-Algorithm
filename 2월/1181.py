
num = int(input())
stringArray = [0] * num
for i in range(num) :
    stringArray[i] = input()
stringArray = list(set(stringArray))
stringArray.sort()
stringArray.sort(key=len)
for i in stringArray :
    print(i)




'''
파이썬 문법 정리
리스트 임의로 할당하기 [0] * num
중복제거 set()
정렬 sort()
입력받기 input()
무조건 함수() 형식으로 감싸주기.
'''