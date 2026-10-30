# # # 1. function to display a message "Hello Your name"
# # def fun1():
# #     print("Hello Your name")
# #
# # fun1()
# #
# #
# # # 2. function to print the factorial of a number
# # def fun2():
# #     n = 5
# #     f = 1
# #     for i in range(1, n+1):
# #         f = f * i
# #     print("Factorial:", f)
# #
# # fun2()
# #
# #
# # # 3. function to find the number of occurrence of a particular character in a string
# # def fun3():
# #     s = "banana"
# #     ch = "a"
# #     c = 0
# #     for i in s:
# #         if i == ch:
# #             c += 1
# #     print("Occurrences:", c)
# #
# # fun3()
# #
# #
# # # 4. function to print the sum of elements in a list
# # def fun4():
# #     l = [89, 45, 67, 12]
# #     s = 0
# #     for i in l:
# #         s = s + i
# #     print("Sum:", s)
# #
# # fun4()
#
#
# # def func4():
# #     i = int(input("enter a number"))
# #     for j in range(2, i):
# #         if i % j == 0:
# #             print("not prime")
# #             break
# #     else:
# #         print("prime")
# # func4()
#
# def simple_intrest(p,n,r):
#     si = p*n*r/100
#     print(si)
#
# simple_intrest(1,2,3)
#
#
# def product3():
#     a = int(input("enter first number"))
#     b = int(input("enter second number"))
#     c = int(input("enter third number"))
#     print(a * b * c)
#
#
# def count_char():
#     s = input("enter a string")
#     ch = input("enter a character")
#     cnt = 0
#     for i in s:
#         if i == ch:
#             cnt = cnt + 1
#     print(cnt)
#
# # You want a function that takes a list and returns a new list
# # with only the unique elements, in the same order they first appeared
# def uniq_list():
#     l = [12, 34, 78, 12, 67, 34, 90, 23]
#     new = []
#     for i in l:
#         if i not in new:
#             new.append(i)
#     print(new)
#
#  # You need a function that takes two lists and prints the common elements.
# def common_list():
#     list1 = [12, 34, 56, 78, 90]
#     list2 = [90, 34, 11, 57, 45]
#     for i in list1:
#         if i in list2:
#             print(i)
# #arbituary type - two types position and keyword
# def fun(*args):
#     print(args)
#
# fun(23, 67)
# fun(1, 2, 3, 4)
# fun(10, 20, 30, 40, 50)
#
# # Example using *args → handles variable number of positional arguments
# # All values passed will be collected into a tuple
#
# def fun(*args):
#     print(args)   # prints the tuple directly
#
# fun(23, 67)       # two values → (23, 67)
# fun(1, 2, 3, 4)   # four values → (1, 2, 3, 4)
# fun(10, 20, 30, 40, 50)  # five values → (10, 20, 30, 40, 50)
#
#
# # Example using **kwargs → handles variable number of keyword arguments
# # All values passed will be collected into a dictionary (key:value pairs)
#
# def fun(**kwargs):
#     print(kwargs)   # prints the dictionary directly
#
# fun(name="arun", age=23)
# # output → {'name': 'arun', 'age': 23}
#
# fun(name="amal", age=24, place="ekm")
# # output → {'name': 'amal', 'age': 24, 'place': 'ekm'}
#
# fun(name="anu", age=25, course="python")
# # output → {'name': 'anu', 'age': 25, 'course': 'python'}
#
# # Function that accepts any number of numbers
# # Using *args → packs all inputs into a tuple
# # Then we loop through and add them up
#
# def sum_all(*args):
#     total = 0
#     for i in args:        # go through each number
#         total += i        # add it to total
#     return total          # finally return the sum
#
#
# # Example calls
# print(sum_all(10, 20, 30))          # 60
# print(sum_all(5, 15, 25, 35, 45))   # 125
# print(sum_all(100))                 # 100
#
# def sum(*args):          # *args collects all numbers into a tuple
#     total = 0
#     for i in args:       # loop through each number
#         total += i       # add it to total
#     return total         # return the final sum
#
# # Example calls
# print(sum(23, 67, 89, 12))      # 191
# print(sum(1, 2, 3, 4, 5))       # 15
# # ------------------------------
# # Built-in Functions (Numbers)
# # ------------------------------
#
# # int(), float(), complex(), type()
# # Convert values into integer, float, complex types
# # type() → tells the datatype
# x = int("10")        # 10
# y = float("3.14")    # 3.14
# z = complex(2, 3)    # (2+3j)
# print(type(x))       # <class 'int'>
#
# # abs() → absolute value (removes sign)
# print(abs(-25))      # 25
#
# # pow(a, b) → a raised to power b
# print(pow(2, 3))     # 8
#
# # max(sequence), min(sequence) → largest / smallest
# nums = [12, 45, 7, 89]
# print(max(nums))     # 89
# print(min(nums))     # 7
#
# # sum(sequence) → adds all elements
# print(sum(nums))     # 153
#
# # divmod(a, b) → returns (quotient, remainder)
# print(divmod(17, 5)) # (3, 2)
#
#
# # ------------------------------
# # Math Module Functions
# # ------------------------------
# import math
#
# # math.sqrt() → square root
# print(math.sqrt(16))     # 4.0
#
# # math.factorial() → factorial of number
# print(math.factorial(5)) # 120
#
# # math.isqrt() → integer square root (no decimals)
# print(math.isqrt(20))    # 4
#
# # math.floor() → round down
# print(math.floor(3.9))   # 3
#
# # math.ceil() → round up
# print(math.ceil(3.1))    # 4
#
# # math.lcm() → least common multiple
# print(math.lcm(12, 18))  # 36
#
# # math.gcd() → greatest common divisor
# print(math.gcd(12, 18))  # 6
#
#
# # ------------------------------
# # Random Module Functions
# # ------------------------------
# import random
#
# # random.random() → float between 0 and 1
# print(random.random())
#
# # random.randint(a, b) → random integer between a and b (inclusive)
# print(random.randint(1, 10))
#
# # random.randrange(start, stop, step) → random number in range
# print(random.randrange(1, 20, 2))  # odd numbers between 1 and 20
#
# # random.choice(sequence) → random element from list/tuple/string
# names = ["arun", "amal", "anu"]
# print(random.choice(names))
#
#
# # abs(x) → absolute value (removes sign)
# print(abs(-100))       # 100
#
# # pow(a, b) → a raised to the power b
# print(pow(5, 3))       # 125
# print(5 ** 3)          # 125  (same as pow)
#
# # max(sequence) → largest element
# print(max((34, 67, 12, 78, 90)))   # 90
#
# # min(sequence) → smallest element
# print(min((34, 67, 12, 78, 90)))   # 12
#
# # sum(sequence) → adds all elements
# print(sum((34, 67, 12, 78, 90)))   # 281
#
# # round(number, ndigits) → rounds to given decimal places
# print(round(3.456, 2))             # 3.46
# print(round(3.452, 2))             # 3.45
# print(round(3.45212345666, 2))     # 3.45
#
#
# import math
#
# # Square root (returns float)
# print(math.sqrt(81))       # 9.0
#
# # Integer square root (no decimals)
# print(math.isqrt(81))      # 9
#
# # Factorial
# print(math.factorial(5))   # 120
#
# # Floor → round down
# print(math.floor(5.678))   # 5
#
# # Ceil → round up
# print(math.ceil(5.678))    # 6
#
# # Least common multiple
# print(math.lcm(1, 2, 3))   # 6
#
# # Greatest common divisor
# print(math.gcd(3, 6, 9))   # 3
#
#
# import random
#
# # randrange(start, stop, step) → random number in range with step
# print(random.randrange(100, 999, 3))   # e.g. 799
# print(random.randrange(100, 999, 3))   # e.g. 556
#
# # randint(a, b) → random integer between a and b (inclusive)
# print(random.randint(10000, 99999))    # e.g. 68649
# print(random.randint(10000, 99999))    # e.g. 57685
# print(random.randint(10000, 99999))    # e.g. 82702
#
# # choice(sequence) → random element from list/tuple/string
# print(random.choice([4, 7, 9, 1, 2]))  # e.g. 7
# print(random.choice([4, 7, 9, 1, 2]))  # e.g. 2
# print(random.choice([4, 7, 9, 1, 2]))  # e.g. 4
# print(random.choice([4, 7, 9, 1, 2]))  # e.g. 2
#



s = "hello world"
print(s.split())        # ['hello', 'world']
print(s.capitalize())   # Hello world
print(s.upper())        # HELLO WORLD
print(s.index('l'))     # 2
print(s.find('l'))      # 2
print(s.count('l'))     # 3

s = "hello"
print(s.strip())          # 'hello'

s = "   hello   "
print(s.strip())          # 'hello'

s = "#####hello#####"
print(s.strip())          # '#####hello#####'

# Correct usage with characters
print(s.strip('#'))       # 'hello'
# Wrong spelling of variable name (will throw error)
# print(seperator.join(sequence))   # NameError

print("-".join("hello"))            # h-e-l-l-o

print(",".join(["red", "green", "blue"]))   # red,green,blue

# Trying to join integers will throw error
# print("-".join([1, 2, 3, 4]))     # TypeError: expected str, got int
s = "hello"
print(s.isalpha())   # True → only alphabets
print(s.isdigit())   # False → not only digits

s = "1234h"
print(s.isdigit())   # False → contains a letter



s = "hello world"
print(s.replace("world", "python"))   # hello python

s = "hello sdfghj hello fghjkl"
print(s.replace("hello", "hi"))       # hi sdfghj hi fghjkl


l = [10, 20, 30, 40, 50, 10]

print(l.index(20))    # 1 → position of first 20
print(l.count(10))    # 2 → number of times 10 appears

l.append(60)
print(l)              # [10, 20, 30, 40, 50, 10, 60]

l.extend([70, 80, 90])
print(l)              # [10, 20, 30, 40, 50, 10, 60, 70, 80, 90]

l.remove(90)
print(l)              # [10, 20, 30, 40, 50, 10, 60, 70, 80]

l.remove(20)
print(l)              # [10, 30, 40, 50, 10, 60, 70, 80]


l = [10, 20, 30, 40]

l.insert(1, 70)
print(l)   # [10, 70, 20, 30, 40]

l = [11, 89, 45, 34, 23, 70]
l.reverse()
print(l)   # [70, 23, 34, 45, 89, 11]

l.sort()
print(l)   # [11, 23, 34, 45, 70, 89]

l = [67, 90, 12, 98.23]
l.sort(reverse=True)
print(l)   # [98.23, 90, 67, 12]


# Write a program to find the position of a character in a string
s = "hello world"
print(s.index('l'))   # position of first 'l'


# Write a program to find the count of character in a string
s = "hello world"
print(s.count('l'))   # count of 'l'


# Create a random 5 digit otp number and print otp number
import random
otp = random.randint(10000, 99999)
print("OTP:", otp)


# Create a list of 5 random 3 digit numbers
import random
l = []
for i in range(5):
    l.append(random.randint(100, 999))
print(l)


# Create a dictionary where keys are words and values are length of each word
s = "python coding is easy and fun"
words = s.split()
d = {}
for w in words:
    d[w] = len(w)
print(d)


# Create a dictionary where keys are each character and values are number of occurrence
s = "hello world"
d = {}
for ch in s:                 # iterate string itself
    d[ch] = s.count(ch)      # use count function
print(d)


# Write a program to find the number of digits, letters, and spaces in a string
s = "sdfghjk3456789  dffghjkl345678"
digits = 0
letters = 0
spaces = 0
for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():       # same way vowels were checked
        letters += 1
    elif ch == ' ':
        spaces += 1
print("Digits:", digits)
print("Letters:", letters)
print("Spaces:", spaces)


# Given a list l=[['amal',23,30000],['arun',25,50000],['anu',24,40000]]
l = [['amal',23,30000],['arun',25,50000],['anu',24,40000]]
salaries = []
for i in l:
    salaries.append(i[2])
print("Salaries:", salaries)
print("Max salary:", max(salaries))
print("Min salary:", min(salaries))


# Given a dictionary d={'arun':34,'amal':45,'anu':40,'kiran':25,'manu':30}
d = {'arun':34,'amal':45,'anu':40,'kiran':25,'manu':30}
new = []
for name in d:
    if d[name] >= 40:
        new.append(name)
print(new)


# Given two lists find common elements
l1 = [11,27,34,45,56]
l2 = [27,34,86,91]
common = []
for i in l1:
    if i in l2:
        common.append(i)
print(common)


# Given l=[23,45,67,12,90,56] find second largest and second smallest
l = [23,45,67,12,90,56]
l.sort()
print("Second smallest:", l[1])
print("Second largest:", l[-2])


# 1. Write a program to find the position of a character in a string
s = "hello world"
print(s.index('l'))   # 2


# 2. Write a program to find the count of character in a string
s = "hello world"
print(s.count('l'))   # 3


# 3. Create a random 5 digit otp number and print otp number
import random
otp = random.randint(10000, 99999)
print("OTP:", otp)


# 4. Create a list of 5 random 3 digit numbers
import random
l = []
for i in range(5):
    l.append(random.randint(100, 999))
print(l)


# 5. Create a dictionary where keys are words and values are length of each word from the string
s = "python coding is easy and fun"
words = s.split()
d = {}
for w in words:
    d[w] = len(w)
print(d)   # {'python':6,'coding':6,'is':2,'easy':4,'and':3,'fun':3}


# 6. Create a dictionary where keys are each character and values are number of occurrence of each character
s = "hello world"
d = {}
for ch in s:                 # iterate string itself
    d[ch] = s.count(ch)      # use count function
print(d)


# 7. Write a program to find the number of digits, letters, and spaces in a string
s = "sdfghjk3456789  dffghjkl345678"
digits = 0
letters = 0
spaces = 0
for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():       # same way vowels were checked
        letters += 1
    elif ch == ' ':
        spaces += 1
print("Digits:", digits)
print("Letters:", letters)
print("Spaces:", spaces)


# 8. Given a list l=[['amal',23,30000],['arun',25,50000],['anu',24,40000]]
#     create a list of salaries
#     find the maximum salary
#     find minimum salary
l = [['amal',23,30000],['arun',25,50000],['anu',24,40000]]
salaries = []
for i in l:
    salaries.append(i[2])
print("Salaries:", salaries)
print("Max salary:", max(salaries))
print("Min salary:", min(salaries))


# 9. Given a dictionary d={'arun':34,'amal':45,'anu':40,'kiran':25,'manu':30}
#     create a new list of students whose mark>=40
d = {'arun':34,'amal':45,'anu':40,'kiran':25,'manu':30}
new = []
for name in d:
    if d[name] >= 40:
        new.append(name)
print(new)


# 10. Given two lists
# l1=[11,27,34,45,56]
# l2=[27,34,86,91]
# Find Common elements
l1 = [11,27,34,45,56]
l2 = [27,34,86,91]
common = []
for i in l1:
    if i in l2:
        common.append(i)
print(common)


# 11. Given l=[23,45,67,12,90,56]
# find second largest number
# find second smallest number
l = [23,45,67,12,90,56]
l.sort()
print("Second smallest:", l[1])
print("Second largest:", l[-2])










#Lambda Function

#square of a number
sq = lambda x: x**2

print(sq(4))
# square of a number
sq = lambda x: x**2
print(sq(4))   # 16

# square root of a number
root = lambda x: x**0.5
print(root(9))   # 3.0

# length of a string
s = lambda a: len(a)
print(s("hello"))   # 5

# name attribute of a dictionary
getname = lambda a: a['name']
print(getname({'name':'Priya','age':22}))   # Priya

# first character of a string
first = lambda a: a[0]
print(first("Python"))   # P

# last element of a list
last = lambda x: x[-1]
print(last([10,20,30,40]))   # 40

# sum of 2 numbers
add2 = lambda x,y: x+y
print(add2(5,7))   # 12

# sum of 3 numbers
add3 = lambda x,y,z: x+y+z
print(add3(2,3,4))   # 9

# product of 4 numbers
p = lambda a,b,c,d: a*b*c*d
print(p(4,5,6,7))   # 840




# name attribute of a dictionary
s = lambda a: a['name']
print(s({"name":"arun","age":18}))   # arun

# first character of a string
s = lambda a: a[0]
print(s("hello"))   # h

# last element of a list
s = lambda x: x[-1]
print(s([1,2,3,4]))   # 4

# sum of 2 numbers
s = lambda x, y: x + y
print(s(3, 4))   # 7

# sum of 3 numbers
s = lambda x, y, z: x + y + z
print(s(3, 4, 5))   # 12

# product of 4 numbers
p = lambda a, b, c, d: a * b * c * d
print(p(4, 5, 6, 7))   # 840



# create a new list with squares of each number
# map(function, sequence)

l = [1, 2, 3, 4]

print(list(map(lambda x: x**2, l)))    # [1, 4, 9, 16]
print(set(map(lambda x: x**2, l)))     # {16, 1, 4, 9}
print(tuple(map(lambda x: x**2, l)))   # (1, 4, 9, 16)





# create a new list of cubes
l = [1, 2, 3, 4]
print(list(map(lambda x: x**3, l)))     # [1, 8, 27, 64]

# create a new list of square roots
l = [25, 36, 81, 100]
print(list(map(lambda x: x**0.5, l)))   # [5.0, 6.0, 9.0, 10.0]

# create a new list of lengths
colors = ['red','green','blue','yellow','black']
print(list(map(lambda x: len(x), colors)))   # [3, 5, 4, 6, 5]

# create a new list of first characters
print(list(map(lambda x: x[0], colors)))     # ['r', 'g', 'b', 'y', 'b']

# create a new list of last elements
print(list(map(lambda x: x[-1], colors)))    # ['d', 'n', 'e', 'w', 'k']


# create a new list of cubes
l = [1,2,3,4]
print(list(map(lambda x: x**3, l)))   # [1, 8, 27, 64]

# create a new list of square roots
l = [25,36,81,100]
print(list(map(lambda x: x**0.5, l)))   # [5.0, 6.0, 9.0, 10.0]

# create a new list of lengths
colors = ['red','green','blue','yellow','black']
print(list(map(lambda x: len(x), colors)))   # [3, 5, 4, 6, 5]

# create a new list of first characters
print(list(map(lambda x: x[0], colors)))   # ['r', 'g', 'b', 'y', 'b']

# create a new list of last characters
print(list(map(lambda x: x[-1], colors)))   # ['d', 'n', 'e', 'w', 'k']

# create a new list of reverse of each element
print(list(map(lambda x: x[::-1], colors)))   # ['der', 'neerg', 'eulb', 'wolleY', 'kcalb']

# Given a list l=[23,78,12,56] Add 10 to each element
l = [23,78,12,56]
print(list(map(lambda x: x+10, l)))   # [33, 88, 22, 66]

# given a list of dictionaries create a new list of emails
l = [
    {'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}
]
print(list(map(lambda x: x['email'], l)))
# ['arun@gmail.com', 'amal@gmail.com', 'anu@gmail.com']

