def ReverseString():
    sampleString = 'abcd1234'
    print(sampleString[len(sampleString)::-1])

# 2.  Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
def CountUpperCareAndLowerCase(givenString):
    upperCount = 0
    lowerCount = 0
    for i in givenString:
        if ord(i) in range(65,91):
            upperCount = upperCount+1
        elif ord(i) in range(97,123):
            lowerCount = lowerCount+1
        else:
            pass
    print('Given String: ',givenString)
    print('Uppercase: ',upperCount)
    print('LowerCase: ',lowerCount)

def ReturnsUniqueList():
    givenList = [1,3,4,3,1,4,5,6,7,6,5,4,3]
    uniqueList = []
    for i in givenList:
        if i in uniqueList:
            pass
        else:
            uniqueList.append(i)
    print(uniqueList)


def HypehnSeperated():
    stop = False
    myList = []
    myString = '-'
    while stop != True:
        userInput = input('Please, Enter the data and \'Stop\' to Stop.: ')
        if userInput == 'stop':
            stop = True
            break
        myList.append(userInput)
        myString.join(myList)

    print(myString)


def UpperCase():
    givenString = 'Hello world Practice makes man perfect'

    userInput = input('Enter you Sentense: ')
    myString = userInput.split(' ')
    print(userInput)
    for i in myString:
        print(i.upper(),end=' ')

#Define a function that can receive two integral numbers in string form and compute their sum and
#print it in the console.

def SumOfStringInterger():
    num1 = input('Enter first number: ')
    num2 = input('Enter 2nd Number: ')
    sum = int(num1)+int(num2)
    print(sum)

if __name__ == '__main__':
    # ReverseString()
    # CountUpperCareAndLowerCase('-12Abcde')
    # ReturnsUniqueList()
    #HypehnSeperated()
    #UpperCase()
    SumOfStringInterger()
