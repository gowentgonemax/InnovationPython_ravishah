#1. Create a list of 10 elements of four different data types like int, string, complex and float.


def CreateListOfMixedDataType():
    myList = [2,4.1,"Max",2+3j,'M',7000,2453.234,"mystring",1+2j,'Ravi',32.1]
    print(myList)


def StringSlicing():
    myString = 'Anoconda'
    print(myString[1:5])

def SumAndMultiple():
    givenList = [2,3,4,5,6,7]
    sum = 0
    multi = 1
    for i in givenList:
        sum = sum+i
        multi = multi*i
    print('Sum: ',sum)
    print('Multiply',multi)

def MinMax():
    givenList = [23,3,43,5,62,1]
    givenList.sort()
    print('Max:', max(givenList))
    print('Min',min(givenList))


#Create a new list which contains the specified numbers after removing the even numbers from a
#predefined list.
def RemovingEvenNumber():
    givenList = [2,33,4,22,13,45,66,36,56,32,33,90]
    newList = [x for x in givenList if x%2!=0]
    print(newList)

#6. Create a list of elements such that it contains the squares of the first and last 5 elements between
#1 and30 (both included).
def ListOfSquare():
    newList = []
    squareList = [x**2 for x in range(1,31)]
    newList.append(squareList[0])
    for i in squareList[len(squareList)-5:len(squareList)]:
        newList.append(i)
    print(newList)

#Write a program to replace the last element in a list with another list.
#Sample input: [1,3,5,7,9,10], [2,4,6,8]

def ReplaceWithNewList():
    givenList = [1,3,5,7,9,10]
    replacingList = [2,4,6,8]
    givenList[-1] = replacingList
    print(givenList)

#8. Create a new dictionary by concatenating the following two dictionaries:
#Sample input: a={1:10,2:20} b={3:30,4:40}
#Expected output: {1:10,2:20,3:30,4:40}
def DictionaryByConCat():
    a={1:10,2:20}
    b={3:30,4:40}
    output = {**a,**b}
    print(output)

#9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
#and n(both 1 and n included).
#Sample input: n=5
#Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}

def DictionalryContainsNumber():
    myDict = {x:x**2 for x in range(1,11)}
    print(myDict)

#10. Write a program which accepts a sequence of comma-separated numbers from console and
#generates a list and a tuple which contains every number in the form of string.
#Sample input: 34,67,55,33,12,98
#Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
def CreateListAndDict():
    myList = []
    myTouple = ()
    i = 0
    while i !=5:
        inputUser = input('Enter your number: ')
        myList.append(inputUser)
        myTouple = myTouple + (inputUser,)
        i +=1
    print(myTouple)
    print(myList)

if __name__ == "__main__":
    CreateListOfMixedDataType()
    StringSlicing()
    SumAndMultiple()
    MinMax()
    RemovingEvenNumber()
    ListOfSquare()
    ReplaceWithNewList()
    DictionaryByConCat()
    DictionalryContainsNumber()
    CreateListAndDict()
