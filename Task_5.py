#1. Write a program in Python to allow the error of syntax to be handled using exception handling.
#HINT: Use SyntaxError
def SyntaxError():
    uname = input('Enter Data')
    if uname != 2:
        raise SystemError('There is error in you Syntax')
    else:
        print('Looks fine')

# 2. Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.
from sys import argv
def ReadFileUsingArgv():
    presentFile = 'README.md'
    try:
        inpurFileName = input('Enter file Name: ')
        if inpurFileName != presentFile:
            raise Exception('Invalid file name')
        else:
            nop,fn =argv
            print('Print program:' , nop)
            print('File name', fn)
            a_File = open(fn,'r')
            lines = a_File.readlines()
            for line in lines:
                print(line)
            a_File.close()
    except Exception as e:
        print(e)

'''a_File = open(presentFile,'r')
            lines = a_File.readlines()
            for line in lines:
                print(line)'''
#3. Write a program to handle an error if the user entered a number more than four digits it should
#return “The length is too short/long !!! Please provide only four digits”

def ErrorHandle_3():
    useInput = int(input('Enter 4 Digit Number: '))
    if len(str(useInput)) > 4:
        raise Exception ('The length is too short/long !!! Please provide only four digits')
    else:
        print('Digit is less than 4')

# 4. Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.
def BackendPage():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    repassword = input('Enter your password to confirm: ')
    count = 0
    if password != repassword:
        while count !=2:
            repassword = input('Enter your password again to confirm: ')
            count = count +1
        if count == 2:
            print('You have crossed your limit.')
    else:
        print('You username and password are created')
# Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:
def ReadFileFromDoc():
    with open('docx.txt',"r") as doc:
        lines = doc.readlines()
        for line in lines:
            if len(line) % 2 ==0:
                print(line,len(line),end="\n")





if __name__=='__main__':
    SyntaxError()
    # ReadFileUsingArgv()
    # ErrorHandle_3()
    # BackendPage()
    # ReadFileFromDoc()
