

def people(moneyPeople) :
    if len(peopleArray) == 1:
        return 0
    
    maxPeople = peopleArray[1:num]
    while (True) :
        maxPeople.sort(reverse=True)
        flag = True

        if maxPeople[0] >= peopleArray[0] :
            maxPeople[0] = maxPeople[0] -1
            peopleArray[0] = peopleArray[0] + 1
            moneyPeople = moneyPeople + 1
            flag = False

        if flag :
            return moneyPeople


num = int(input())
peopleArray = [0] * num
dasom = 0

for i in range(num) :
    peopleArray[i] = int(input())
        
moneyPeople = people(0)
print(moneyPeople)
    

