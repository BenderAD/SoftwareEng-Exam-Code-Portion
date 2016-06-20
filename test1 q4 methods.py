# Methods for Question 4 of Programming Languages Test 1
# Alex Bender

def averageListNum(numList):
    listSum = 0

    i = 0
    while i < len(numList)-1:

        listSum += numList[i]

        i+= 1
        
    print(listSum / len(numList))
    return listSum / len(numList)

def reverseList(varlist):
    i = len(varlist)-1

    while i >= 0:

        print(varlist[i])

        i -= 1


list1 = [24, 255, 3.1, 4,234, 99]
list2 = ["heart", "broken", "a", "mend"]
averageListNum([1,2,3,4,5])
print()
averageListNum(list1)
print()
reverseList(["a", "b", "c", "d"])
print()
reverseList(list2)
