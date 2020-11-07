def DecisionMaking1():
   userInput = int(input('Enter the number to see result: '))
   if userInput%3 == 0 and userInput%5 == 0:
       print('ConsultAdd - Python Trainning')
   elif userInput%3 == 0:
       print('Consultadd')
   elif userInput%5 == 0:
       print('Python Trainning')

def DecisionMaking2():
    result = 0
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the 2nd number: '))
    print('1. Addition')
    print('2. Subtraction')
    print('3. Division' )
    print('4. Multiplication')
    print('5. Average')
    userInput = int(input('Enter the choice  for calculation: '))
    if userInput ==1 :
        result = result + (num1 + num2)
    elif userInput == 2:
        pass
        result = result + (num1 - num2)
    elif userInput == 3:
        result = result + (num1 / num2)
    elif userInput == 4:
        result = result + (num1 * num2)
    elif userInput == 5:
        num3 = int(input('Enter the third number: '))
        num4 = int(input('Enter the fourth number: '))
        result = result + (num1+num2+num3+num4)/4
    else:
        print('Invalid selection')
    print('The final result is: ',result)
    if result < 0:
        print('Negative')

def FlowChart():
    a,b,c = 10,20,30
    avg = (a+b+c)/3
    print('a,b,c')
    print(a,b,c)
    print('Average: ',avg)
    if avg > a and avg > b and avg > c:
        print('Average is higher than a,b,c')
    else:
        if avg > a and avg > b:
            print('Average is higher than a,b,c')
        else:
            if avg > a and avg > c:
                print('Average is higher than a,c')
            else:
                if avg > b and avg > c:
                    print('Average is higher than b,c')
                else:
                    if avg > a:
                        print('Average is higher than a')
                    else:
                        if avg > b:
                            print('Average is higher than b')
                        else:
                            if avg > c:
                                print('Average is just higher than C')

def BreakContinue():
    valid = True
    while valid:
        num = int(input('Enter your number: '))
        if num < 0:
            valid =  False
            print('You hvae entered negative number. So, It\'s Over')
            break
        else:
            print('Continue')
            continue

def DivisibleBySevenButNotByFive():
    for i in range(2000,3200):
        if i%7 ==0 and i%5 != 0 :
            print(i)
def ShowOutPut():
    x = 123
    # for i in x:
    #     print(i)
    print('x is an Integer which can\'t be iterate')
    i = 0
    while i< 5:
        print(i)
        i = i+1
        if i ==3:
            break
        else:
            print('Error')
    count = 0
    while True:
        print(count)
        count += 1
        if count >= 5:
            break

def PrintNumber():
    for i in range(1,6):
        if i != 3 and i!= 6:
            print(i)
def CountChar():
    s = 'consul72'
    numCounter = 0
    charCounter = 0
    for i in s:
        if ord(i) in range(97,122):
            charCounter +=1
        elif ord(i) in range(48,57):
            numCounter += 1
        else:
            print(i,'It is special character')
    print('The number of Char in given String is :',numCounter)
    print('The number of Digit in given String is :',charCounter)

def GuessLuckyNumber1():
    luckyNumber =10
    isFound = False
    while isFound != True:
        askUser = int(input('Please, Enter the lucky number: '))
        if askUser == luckyNumber:
            print('Congratulation!,You found the lucky number.')
            isFound =  True
        else:
            print('Try again.')
def GuessLuckyNumber2():
    luckyNumber = 10
    answer = 'yes'
    while answer !='no':
        print('1')
        askUser = int(input('Please, Enter the lucky number: '))
        if askUser == luckyNumber:
            print('2')
            print('Congratulation!,You found the lucky number.')
            print('3')
            break
        else:
            answer = input('Do you want to contine ?:')
            print('4')



def GuessTillFiveTimes():
   pass





if __name__ == "__main__":
    #DecisionMaking1()
    #DecisionMaking2()
    #FlowChart()
    #BreakContinue()
    #DivisibleBySevenButNotByFive()
    #ShowOutPut()
    #PrintNumber()
    #CountChar()
    #GuessLuckyNumber1()
    GuessLuckyNumber2()
    GuessTillFiveTimes()



