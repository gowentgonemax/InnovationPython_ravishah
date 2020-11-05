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

    print('The final result is: ',result)

if __name__ == "__main__":
    #DecisionMaking1()
    DecisionMaking2()
