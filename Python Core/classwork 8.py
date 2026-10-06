




# Q.Write Python Programs Using map(), filter(), or reduce()
#
# 1.Capitalize all names in a list
# names = ['alin', 'arun', 'anu']
# names = ['alin', 'arun', 'anu']
# n=map(str.capitalize,names)
# print(list(n))



#
# 2.Append "@gmail.com" to a list of usernames
# users = ['user1', 'user2']
# users = ['user1', 'user2']
# emails=map(lambda x:x+"@gmail.com",users)
# print(list(emails))

# 3.Filter out all empty strings from a list
# words = ['hello', ' ', 'world', ' ', 'python']
# words = ['hello', ' ', 'world', ' ', 'python']
# f=filter(lambda x:x!=' ',words)
# print(list(f))


#
# 4.Filter names that start with the letter 'A'
# names = ['Anu', 'Neenu', 'Arun', 'Ravi']
# names = ['Anu', 'Neenu', 'Arun', 'Ravi']
# n=filter(lambda x:x[0]=='A',names)
# print(list(n))

#
# 5.Concatenate all strings in a list
# words = ['Python', 'is', 'fun']
# words = ['Python', 'is', 'fun']
# import functools
# result=functools.reduce(lambda x,y:x+" "+y,words)
# print(result)

#
# 6.Multiply all numbers in a list
# nums = [2, 3, 4]
# nums = [2, 3, 4]
# import functools
# prd=functools.reduce(lambda x, y:x*y,nums)
# print(prd)

#
# 7.Extract First Character of Each Word
# words = ["apple", "banana", "cherry"]
# words = ["apple", "banana", "cherry"]
# n=map(lambda x:x[0],words)
# print(list(n))


#
# 8.Add 10 to Each Number
# nums = [5, 10, 15]
# nums = [5, 10, 15]
# n=map(lambda x:x+10, nums)
# print(list(n))



# 9.Given a list
# l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
#     # #Sum of positive even numbers
# l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
# n=filter(lambda x:x>0 and x%2==0,l)
# sum_pos_even=sum(n)
# print(sum_pos_even)
#
#     # #Sum of Positive Odd numbers
# l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
# n=filter(lambda x:x>0 and x%2!=0,l)
# sum_pos_odd=sum(n)
# print(sum_pos_odd)
#
#     # #Sum of Negative  odd numbers
# l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
# n=filter(lambda x:x<0 and x%2!=0,l)
# sum_neg_odd=sum(n)
# print(sum_neg_odd)
#
#     # #Sum of Negatve Even numbers
# l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
# n=filter(lambda x:x<0 and x%2==0,l)
# sum_neg_even=sum(n)
# print(sum_neg_even)
#
#     # #Count of Positive numbers
# l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
# n=list(filter(lambda x:x>0,l))
# count=len(n)
# print(count)
#
#     # #Count of negative numbers
# l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
# n=list(filter(lambda x:x<0,l))
# count=len(n)
# print(count)
#
#
# 10.Given a list nums = ["1", "2", "3", "4"]
# Convert all Strings to Integers [1,2,3,4]
#
# nums = ["1", "2", "3", "4"]
# result = list(map(int, nums))
# print(result)
#
#
# 11.
# p= [{'name':'laptop','price':50000},
#     {'name':'phone','price':20000},
#     {'name':'watch','price':3000},
#     {'name':'Tablet','price':25000}]
#
# print list of product names in Uppercase
# p= [{'name':'laptop','price':50000},
#     {'name':'phone','price':20000},
#     {'name':'watch','price':3000},
#     {'name':'Tablet','price':25000}]
# upper=map(lambda x:x['name'].upper(),p)
# print(list(upper))
#

# print products with price greater than 10000
# p= [{'name':'laptop','price':50000},
#     {'name':'phone','price':20000},
#     {'name':'watch','price':3000},
#     {'name':'Tablet','price':25000}]
# price=filter(lambda x:x['price']>10000,p)
# print(list(price))
#



# Find the total price of all products
# p= [{'name':'laptop','price':50000},
#     {'name':'phone','price':20000},
#     {'name':'watch','price':3000},
#     {'name':'Tablet','price':25000}]
# import functools
# total = functools.reduce(lambda x, y: x + y['price'], p, 0)
# print(total)


l = [1,2,3,4,5]
print(list(filter(lamda x : x%2==0,l)))

f = ["apple","orange","grapes","pineapple","grapes"]

#given a list of numbers
l=[10,25,30,45,60,75,80]
#numbers divisible by 5 only
print(list(filter(lambda x: x%5==0,l)))
#output: [25, 30, 45, 60, 75]

#given a list of strings
s=['cat','elephant','dog','tiger','lion']
#strings starting with 'd'
print(list(filter(lambda x: x[0]=='d',s)))
#output: ['dog']

#given a list of numbers
l=[2,3,5,7,8,11,13,15,18]
#prime numbers only
print(list(filter(lambda x: all(x%i!=0 for i in range(2,int(x**0.5)+1)) and x>1,l)))
#output: [2, 3, 5, 7, 11, 13]
#Reduce
l=[1,2,3,4]
import functools

#sum of list
print(functools.reduce(lambda x,y: x+y, l))
#output: 10

#product of list
print(functools.reduce(lambda x,y: x*y, l))
#output: 24
