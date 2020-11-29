'''1. Write a program in Python to find out the character in a string which is uppercase using list
comprehension.'''
def ComprenshiveList():
    givenString = "ILovePythonVeryMuch"
    myList = [x for x in givenString if ord(x) in range(65,91)]
    print(myList)

'''2. Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
HINT - Use Zip function also
Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}'''

def MappinginDict():
    students = ['Smit', 'Jaya', 'Rayyan']
    subjects = ['CSE', 'Networking', 'Operating System']
    myDict = {students[x]:subjects[x] for x in range(0,3)}
    print(myDict)

# 4. Write a program in Python using generators to reverse the string.
#
def InverseStringUsingGenerator(my_str):
        inputString = 'Consultadd Training'
        rev =''

        for i in range(len(inputString),-1,-1):
            yield i

def Generator(a,b):
     return(a/b)

def otherFuncForGenerator():
    
if __name__ == "__main__":
    # ComprenshiveList()
    # MappinginDict()
    InverseStringUsingGenerator('Consultadd Training')
    Generator()
