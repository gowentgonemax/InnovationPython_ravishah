'''1. Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
D is a variable whose values should be input to your program in a comma-separated sequence.'''
C = 50.
H = 30.
import math

d_value = list(map(int, input("Enter the value of D: ").split(",")))
for i in d_value:
    Q = math.sqrt((2*C*i)/H)
    print('Value of Q is:',Q)

'''2. Define a class named Shape and its subclass Square. The Square class has an init function which
takes length as argument. Both classes have an area function which can print the area of the shape
where Shape’s area is 0 by default.'''
print('*****Shape Question****')

class Shape:
    def Area(self):
        return 0
class Square(Shape):
    def __init__(self,length=0):
        self.length = length

    def Area(self):
        print(self.length*self.length)
ob = Square()
print('The area of square is: ',ob.Area())

'''3. Create a class to find three elements that sum to zero from a set of n real numbers
Input array: [-25,-10,-7,-3,2,4,8,10]
Expected output: [[-10,2,8],[-7,-3,10]]'''
print('*****Add sum****')

import itertools
class FindElements:
    def __init__(self,inputList):
        listSum =[]
        for subset in itertools.combinations(inputList,3):
            if sum(list(subset)) == 0:
                if list(subset) not in listSum:
                    listSum.append(list(subset))
        print(listSum)
givenInput = [-25,-10,-7,-3,2,4,8,10]
ob = FindElements(givenInput)

'''4. Create a Time class and initialize it with hours and minutes.
Create a method addTime which should take two Time objects and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Create another method displayTime which should print the time.
Also create a method displayMinute which should display the total minutes in the Time.
E.g.- (1 hr 2 min) should display 62 minute.'''
print('*****Time CLass****')

from datetime import timedelta
class Time:
    def __init__(self,hours,minute):
        self.hours = hours
        self.minute = minute

    def AddTime(self,t1,t2):
        print(t1,t2)

# t1 = [2,50]
# t2 = [1,20]
# obj = Time
# obj.AddTime(t1,t2)
'''5.
Write a Person class with an instance variable “age” and a constructor that takes an integer as a
parameter. The constructor must assign the integer value to the age variable after confirming the
argument passed is not negative; if a negative argument is passed then the constructor should set
age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance methods:
Sample Input for amIOld():
        -1
        4
        10
        16
        18
        64
        38'''
print('*****Age question****')
class Person:
    def __init__(self,age):
        if age < 0:
            print('Age is not valid,setting age to zero')
            self.age = 0
        else:
            self.age = age

    def yearPasses(self,value):
        print( 'Year passes',self.age+value)

    def amIOld(self):
        if 13 > self.age > 0:
            print('You are Young')
        elif 12 < self.age < 20:
            print('You are Teaanage')
        else:
            print('You are old')


obj = Person(-2)
obj.amIOld()
obj.yearPasses(2)
