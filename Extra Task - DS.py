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
