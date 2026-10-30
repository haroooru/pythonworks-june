#write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese
#
weight = float(input("enter weight in kg"))
height = float(input("enter height in meter"))

bmi = weight/(height**2)

print("BMI =", bmi)

if (bmi<=18.4):
    print("Underweight")
elif (bmi>=18.5 and bmi<=24.9):
    print("Normal")
elif (bmi>=25.0 and bmi<=39.9):
    print("Overweight")
else:
    print("Obese")

# # A toy vendor supplies three types of toys:
#
# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.
#
# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
#
# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,
#
# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.
#
# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.
#
# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

code = int(input("enter product code"))
amount = float(input("enter order amount"))

if (code==1):
    if (amount>1000):
        amount = amount-(amount*10/100)
    print(" total =", amount)

elif (code==2):
    if (amount>100):
        amount = amount-(amount*5/100)
    print("total =", amount)

elif (code==3):
    if (amount>500):
        amount = amount-(amount*10/100)
    print("total =", amount)

else:
    print("Invalid ")

#3 FIZZBUZZ PRoblem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number
#
num = int(input("enter a number"))

if (num%3==0 and num%5==0):
    print("FizzBuzz")
elif (num%3==0):
    print("Fizz")
elif (num%5==0):
    print("Buzz")
else:
    print(num)

num = 0
while (num <= 1000):
    print(num)
    num+=5










# Q1. Write a Python program to print numbers from 1 to 100 using a while loop.

# num = 1
# while(num <= 100 and num%1==0):
#     print(num)
#     num=num+1


# Q2. Write a Python program to find the sum of numbers from 1 to 10 using a while loop.

sum = 0
num = 1
while num <= 10:
    sum += num
    num = num + 1

print(sum)


# Q3. Write a Python program to display the multiplication table of a given number using a while loop.

# num = int(input("Enter a number"))
# i = 1
# while(i <= 10):
#     print(num, "x", i, "=", num * i)
#     i = i + 1


# Q4. Write a Python program to print all numbers divisible by 5 from 1 to 100 and count them.

# count = 0
# i = 1
# while(i <= 100):
#     if(i % 5 == 0):
#         print(i)
#         count = count + 1
#     i = i + 1
# print(count, "is count")


# Q5. Write a Python program to print all numbers divisible by 3 from 1 to 50 and count them.

# count = 0
# num = 1
# while(num <= 50):
#     if num % 3 == 0:
#         print(num)
#         count += 1
#     num += 1
# print(count)


# Q6. Write a Python program to find the sum of all even numbers from 0 to 20.

# sum = 0
# num = 0
# while num <= 20:
#     if num % 2 == 0:
#         sum += num
#     num = num + 1
# print(sum)


# Q7. Write a Python program to find the sum of all three-digit numbers.

# sum = 0
# num = 100
# while num <= 999:
#     sum += num
#     num = num + 1
# print(sum)


# Q8. Write a Python program to find the product of all odd numbers from 1 to 20.

product = 1
num = 1
while num <= 20:
    if num % 2 != 0:
        product *= num
    num += 1
print(product)


# Q9. Write a Python program to print the numbers between 200 and 300 that are divisible by both 3 and 7. Also count them.

# count = 0
# i = 200
# while(i <= 300):
#     if(i % 7 == 0 and i % 3 == 0):
#         print(i)
#         count = count + 1
#     i = i + 1
# print(count, "is count")


# Q10. Write a Python program to print all three-digit numbers containing the digit 3 and count them.

# count = 0
# i = 100
# while(i <= 999):
#     if("3" in str(i)):
#         print(i)
#         count = count + 1
#     i = i + 1
# print(count, "is count")


# Q11. Write a Python program to count the palindrome numbers between 1 and 1000.

count = 0
num = 1

while(num <= 1000):
    if str(num) == str(num)[::-1]:
        count += 1
    num += 1

# print(count)


# Q12. Write a Python program to find the product of all numbers between 0 and 50 that contain the digit 3.

# product = 1
# num = 0
# while num <= 50:
#     if '3' in str(num):
#         product *= num
#     num += 1
# print(product)







........................................................................................................................




# s="hello world"
# for i in s:
#     print(i)
#
# colours = ["red", "green", "blue"]
# for i in colours:
#     print(i)
#
# s={10,20,30}
#
# for i in s:
#     print(i)




d = {"a":10,"b":20,"c":30}

for i in d.values():
    print(i)



l =[12,34,56,45,89,16,69,33]
sum = 0
for i in l:
    sum = sum+i
print(sum)
#
# count = 0
# for i in l:
#     count+=1
# print(count)
#
# count = 0
# for i in l:
#     if i%2==0:
#      count+=1
# print(count)
#
# product = 1
# for i in l:
#     product*=i
# print(product)
#
# for i in l:
#     square = i**2
#     print(square)
#





#
# for i in range (1,11):
#     print(i)
#
# #Range
#
# # 1,2,3,4,5
# for i in range (1,6):
#     print(i)
#
# #1,3,5,7,9,11
#
# for i in range (1,12,2):
#     print(i)
#
# #2,4,6,8,10
# for i in range (2,11,2):
#     print(i)
#
# #100,200,300,400,500
# for i in range (100,501,100):
#     print(i)
# #5,4,3,2,1
# for i in range (5,0,-1):
#     print(i)
#
# #3,6,9,12,15,18,21
# for i in range (3,22,3):
#     print(i)
#
# #1,4,9,16,25,36
# for i in range (1,7):
#     print(i*i)
#
# #print all 3 digit numbers(100-999)
#
# for i in range(100,1000):
#     print(i)
#
# #print all numbers divisible by 3 in the range 100-200
# for i in range(100,201):
#     if i%3==0:
#         print(i)
#
# #1,8,27,64,125
#
# for i in range(1, 6):
#     print(i**3)
#
n=12345
for i in str(n):
    print(i)
#
l =[1,2,3,4,5]
sum = 0
for i in l:
    sum=sum+i
#
#

#
s="hello"
rev=""
for i in s:
    rev = i+rev
print(rev)
#
num = int(input("enter a number"))
s = str(num)
rev=""
for i in s:
    rev=i+rev
print(rev)

# # Given a list
# l = [1, 2, 3, 4]
#
# # Print squares of each number
# for i in l:
#     print(i**2)
#
# # Create a new list with squares of each element
new = []
for i in l:
    new.append(i**2)
#
# print(new)  # Output: [1, 4, 9, 16]
#
new = set()
for i in l:
    new.add(i**2)
#
# print(new)
#
# new = set()
# for i in l:
#     new.add(i**2)
#
# print(new)


# create a dictionary where keys are numbers and values are squares of each number
# Example: {1:1, 2:4, 3:9, 4:16}

#create a dictionary where keys are numbers and values are squares
d={1:1,2:4,3:9,4:16}

l = [1, 2, 3, 4]   # define the list of numbers
new = {}
for i in l:
    new[i] = i**2
#
# print(new)
# s="hello"
# for i in s:
#     if i == 'l':
#         break
#     print(i)
#
# for i in s:
#     if i == 'l':
#         continue
#     print(i)


# colors = ['red','green','blue','yellow','black','orange']
#
# # print each color
# for c in colors:
#     print(c)
#































#
# # print the first color that contains letter 'n'
# for c in colors:
#     if 'n' in c:
#         print(c)
#         break
#
# # print all colors except those that contain letter 'n'
for c in colors:
    if 'n' in c:
        continue
    print(c)

# # Given a list
# colors = ['red','green','blue','yellow','black','orange']
#
# # print each color
# for c in colors:
#     print(c)
#
# # print the first color starting with 'b'
for c in colors:
    if c[0] == 'b':   # check first letter
        print(c)
        break
#
# # print all colors except color starting with 'b'
for c in colors:
    if c[0] == 'b':   # skip if first letter is b
        continue
    print(c)
#
# # print the first color that contains letter 'n'
# for c in colors:
#     if 'n' in c:      # check if 'n' is inside the word
#         print(c)
#         break
#
# # print all colors except those that contain letter 'n'
# for c in colors:
#     if 'n' in c:      # skip if 'n' is inside the word
#         continue
#     print(c)
#
#     colors = ['red', 'green', 'blue', 'yellow', 'black', 'orange']
#
#     # print each color
#     for c in colors:
#         print(c)
#
#     # print the first color starting with 'b'
#     for c in colors:
#         if c[0] == 'b':  # check first letter directly
#             print(c)
#             break
#
#     # print all colors except color starting with 'b'
#     for c in colors:
#         if c[0] == 'b':
#             continue
#         print(c)
#
#     # print the first color that contains letter 'n'

    for c in colors:
        found = False
        for ch in c:
            if ch == 'n':
                print(c)
                found = True
                break
        if found:
            break
#
#     # print all colors except those that contain letter 'n'
    for c in colors:
        skip = False
        for ch in c:
            if ch == 'n':
                skip = True
                break
        if skip:
            continue
        print(c)
# # Given a list l=[1,2,3,4] create a new list with squares of each element
# l = [1,2,3,4]
# new_list = []
# for i in l:
#     new_list.append(i**2)
# print(new_list)
#
#
# # Given a list l=[12,67,59,23] create a list with elements whose value is greater than 50
# l = [12,67,59,23]
# new_list = []
# for i in l:
#     if i > 50:
#         new_list.append(i)
# print(new_list)
#
# # create a new set with elements whose value is greater than 50
# new_set = set()
# for i in l:
#     if i > 50:
#         new_set.add(i)
# print(new_set)
#
#
# # Given a list l=[1,2,3,4] create a new dictionary where keys are numbers and values are squares of each number
# l = [1,2,3,4]
# new_dict = {}
# for i in l:
#     new_dict[i] = i**2
# print(new_dict)
#












#
# for i in range(1,5):
#     for j in range(1,5):
#         print(i)


# 1111
# 2222
# 3333
# 4444

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end="")
#     print()
#
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end="")
#     print()
#
#
# for i in range(1,5):
#     for j in range(1,5):
#         print("A",end="")
#     print()
#
# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end="")
#     print()
#
# # 1
# # 22
# # 333
# # 4444
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


# *
# **
# ***
# ****
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(0,5):
#     for j in range(0,5):
#         if i==j:
#             print(1,end="")
#         else:
#             print(0,end="")
#     print()

# for i in range(1,5):
#      for j in range(5,i,-1):
#          print("*",end="")
#      print()

# ****
# ***
# **
# *


# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


# 1
# 23
# 456
# 78910


# k=1
# for i in range(1,5):
#
#     for j in range(1,i+1):
#         print(k,end="")
#         k=k+1
#     print()


# k=2
# for i in range(1,5):
#
#     for j in range(1,i+1):
#         print(k,end="")
#         k=k+2
#     print()
#
# k=1
# for i in range(1,4):
#
#     for j in range(1,i+1):
#         print(k,end="")
#         k=k+2
#     print()

# for i in range(5,0,-1): i = 5
#      for j in range(0,i):
#          print(i,end="")
#      print()

# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()
#
# 1
# 10
# 101
# 1010

# Print alternating 1 and 0 pattern
# for i in range(1, 5):          # rows
#     for j in range(1, i+1):    # columns
#         if j % 2 == 1:         # odd position → 1
#             print(1, end="")
#         else:                  # even position → 0
#             print(0, end="")
#     print()
# 1
# 10
# 101
# 1010

# k = ord("A")
# for i in range(1,5):
#     for j in range(0,i):
#         print(chr(k),end="")
#     k=k+1
#     print()
# # A
# # BB
# # CCC
# # DDDD
#
# # l = [12,34,56,78,13,87,5]
# # #print all prime numbers
# # new=[]
# # for i in l:
# #     print(i)
#
# # l = [12,34,56,78,13,87,5]
# # #print all prime numbers
# # new=[]
# # for i in l:
# #     for j in range(2,i):
# #         if i%j==0:
# #             break# if you want t print anything put print("not prime")
# #     else:
# #         print(i)
# #print all prime numbers from 1,100
# for i in range(2,101):
#     for j in range (2,i):
#         if i%j==0:
#             break
#     else:
#             print(i  ,end=" ")
#
# # # Pattern 1
# # 1
# # 4 9
# # 16 25 36
# # 49 64 81 100
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k*k,end=" ")
#         k=k+1
#     print()
#
# # # Pattern 2
# # 1
# # 3 3 3
# # 5 5 5 5 5
# k=1
# for i in range(1,4):
#     for j in range(1,2*i):
#         print(k,end=" ")
#     k=k+2
#     print()
#
# # # Pattern 3
# # 1
# # 1 4 1
# # 1 4 1 4 1
# for i in range(1,4):
#     for j in range(1,2*i):
#         if j%2==1:
#             print(1,end=" ")
#         else:
#             print(4,end=" ")
#     print()
#
# # # Pattern 4
# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()
#
# # # Pattern 3 (even first)
# # A
# # A 1 A
# # A 1 A 1 A
# for i in range(1,4):
#     for j in range(1,2*i):
#         if j%2==0:      # even position → A
#             print("A",end=" ")
#         else:           # odd position → 1
#             print(1,end=" ")
#     print()

# # Right aligned star triangle
# k=3
# for i in range(1,5):
#     for p in range(1,k+1):   # print spaces first
#         print(" ",end="")
#     k=k-1
#     for j in range(1,i+1):   # then print stars
#         print("*",end="")
#     print()
#
# k = 3 * 2   # k = 6
#
# for i in range(1, 5):          # 4 rows
#     for p in range(1, k + 1):  # print spaces first
#         print(" ", end=" ")
#     k = k - 2                  # reduce spaces by 2 each row
#
#     for j in range(1, i + 1):  # then print stars
#         print("*", end="       ")
#     print()



# k = 0   # start with no spaces
#
# for i in range(1, 5):          # 4 rows
#     for p in range(1, k + 1):  # print spaces first
#         print(" ", end=" ")
#     k = k + 2                  # increase spaces by 2 each row
#
#     for j in range(1, i + 1):  # then print stars
#         print("*", end="   ")
#     print()


k = 3 * 2
for i in range(1, 5):
    for p in range(1, k + 1):
        print("", end=" ")
    k = k - 2
    for j in range(1, i + 1):
        print('5', end=" ")
    print()
#
#       5
#     5   5
#   5   5   5
# 5   5   5   5

k = 0
for i in range(4, 0, -1):
    for p in range(1, k + 1):
        print("", end=" ")
    k = k + 2
    for j in range(1, i + 1):
        print("*", end="   ")
    print()
#
# *   *   *   *
#   *   *   *
#     *   *
#       *

# List comprehension examples

l = [1, 2, 3, 4]

# square each element
new_list = [i**2 for i in l]
print(new_list)   # [1, 4, 9, 16]

# replace each element with 5
new = [5 for i in l]
print(new)        # [5, 5, 5, 5]

# Given list
l = [12, 45, 34, 67, 90]

# new list with even values
even_list = [i for i in l if i % 2 == 0]
print(even_list)   # [12, 34, 90]

# new list with values greater than 50
greater_50 = [i for i in l if i > 50]
print(greater_50)  # [67, 90]


# Given list of colors
colors = ['red','green','blue','orange']

# new list with first letters
first_letters = [c[0] for c in colors]
print(first_letters)   # ['r','g','b','o']
# Given a list
l = [12, 45, 34, 67, 90]

# create a new list with even values
even_list = [i for i in l if i % 2 == 0]
print(even_list)   # [12, 34, 90]

# create a new list with values greater than 50
greater_50 = [i for i in l if i > 50]
print(greater_50)  # [67, 90]


# Given a list of colors
colors = ['red','green','blue','orange']

# create a new list with first letter of each color
first_letters = [c[0] for c in colors]
print(first_letters)   # ['r','g','b','o']

# create a new list with length of each color
lengths = [len(c) for c in colors]
print(lengths)         # [3, 5, 4, 6]
