'''Create three variables in a single line and assign values to them in such a manner that each one of
them belongs to a different data type.
E.g. :
a = 1,
b = 2.01,
c = 'string'
'''

def ThreeVariable():
    var1,var2,var3 = 1,2.01,"Ravi Shah"
    print('The three variable in one line: ',var1,var2,var3)


# 2. Create a variable of type complex and swap it with another variable of type integer.
def VariableTypeComplex():
    print('No idea about type complex.')
# 3. Swap two numbers using a third variable and do the same task without using any third variable.
def SwapUsingThirdVariable():
    var1 = 2
    var2 = 3
    print('--------Swaping using third variable---------')
    print('Before swaping: ',var1,var2)
    temp = var1
    var1 = var2
    var2 = temp
    print('After swaping: ',var1,var2)
    print('--------Swaping without using third variable---------')
    print('Before swaping: ',var1,var2)
    var1,var2 = var2,var1
    print('After swaping: ',var1,var2)
# 4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
# Version.
def UserInputInBothVersion():
    userInput = input('Enter your value: ')
    print('The value using python 3.x version',userInput)
    print('Dont know how to print 2.x version in 3.x verion environment')
# 5. Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# another variable called z. Add 30 to z and store the output in variable result and print result as the
# final output.

def UserInputThenSumIt():
    userInput1 = int(input('Enter the first number from (1-10): '))
    userInput2 = int(input('Enter the second number from (1-10)'))
    z = userInput1 + userInput2
    result = z+30
    print('The 1st number is',userInput1)
    print('The 2nd number is',userInput2)
    print('The Final output is: ',result)

# 6. Write a program to check the data type of the entered values.
# HINT: Printed output should say - The data type of the input value is : int/float/string/etc
def CheckDataType():
    var = 2

    print('The data type of var is: ',type(var))
# 7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
# UPPERCASE.
# (Refer: https://capitalizemytitle.com/camel-case/)
def Case():
    sampleCase = 'I love Python very much'
    lowerCamel = 'iLovePythonVeryMuch'
    upperCamel = 'ILovePythonVeryMuch'
    snakeCase = 'i_love_python_very_much'

    print('Sample Case : ',sampleCase)
    print('Lower Camel Case : ',lowerCamel)
    print('Upper Camel Case : ',upperCamel)
    print('Snake Case : ',snakeCase)
# 8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
# again. Will it change the value? If Yes then Why?
def DifferentDataType():
    a = 2
    a = "Ravi"
    print(a)
    print('First variable is assigned with Integer then to String. It holds the string value. Becasue, variable is defined by it\'s value')


if __name__ == "__main__":
    ThreeVariable()
    VariableTypeComplex()
    SwapUsingThirdVariable()
    UserInputInBothVersion()
    UserInputThenSumIt()
    CheckDataType()
    Case()
    DifferentDataType()
