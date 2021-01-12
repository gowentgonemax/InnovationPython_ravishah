print('2.Create a list of thousand numbers using range and xrange and see the difference between each other')
p = '''
for i in range(1000):
    print(i)
    
for i in xrange(1000):
    print(i)
Traceback (most recent call last):
  File "C:/Users/Ravi/Desktop/Coding/MobileDevelopment/Task_ET.py", line 5, in <module>
    for i in xrange(1000):
NameError: name 'xrange' is not defined
'''
print(p)
print('3. How Tuple is beneficial as compared to the list?')
print('Tuple is immutable which helps to be key for dictionary unlike List. Tuples reserved less memory than Lists. '
      'Tuple size are fixed but in Lists size can be reduce or increase.')
print("")
print('4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number '
      'which is divisible by 3 and is a multiple of 2.')
for i in range(1,100):
    if i%3 == 0 and i%2==0:
        print(i)

print('5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string '
      'with their index.')
inv = []
vowel = ['a','e','i','o','u']
givenString = 'Fox jumped over the wall has died'
givenString = givenString[::-1]
for i in givenString:
    if i in vowel:
        print(i,end='')

print('6.Write a program in Python to iterate through the string “hello my name is abcde” and print the string which '
      'is having an even length.')
myString = "hello my name is abcde"
fileteredString = ''
myList = myString.split(' ')
print('The filtered String is: ')
for i in myList:
    if len(i)%2 == 0:
        print(i,end=' ')
        
# 7. Write a program in python to print the pair of numbers whose sum is equal to the result
# number that is let's say 8.
# x=[1,2,3,4,5,6,7,8,9,-1]
import itertools
x=[1,2,3,4,5,6,7,8,9,-1]
print('The pair of number to 8')
for subset in itertools.combinations(x,2):
    if sum(list(subset)) == 8:
        print(subset)

# 8. Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list
# Ask user to enter a number in the range of 1,50 and make sure if the entered number is
# even, append it to the even_list and if the entered number is odd append it to the odd_list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you enter all the 5 elements, calculate the sum of the list and return the
# maximum of the list.

evenList = []
oddList = []
while len(evenList) !=5 or len(oddList) != 5:
    userInput = int(input('Enter a number in range 1-50:'))
    if userInput%2== 0:
        evenList.append(userInput)
        print(evenList)
        evenSum = sum(evenList)

    else:
        oddList.append(userInput)
        print(oddList)
        oddSum = sum(oddList)
print(evenList,oddList)


# 9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
# Sample input: 12abcbacbaba344ab
# Expected output: a=5 b=5 c=2
# NOTE: Make sure to avoid counting the occurrence of numeric values in the string.
import re
from collections import Counter
word1 = '12abcbacbaba344ab'
for i in word1:
    if i.isdigit():
        new = word1.replace(i,'')
        word1 = new
p = Counter(word1)
p =dict(p)
for k,v in p.items():
    print(k,'=',v)

