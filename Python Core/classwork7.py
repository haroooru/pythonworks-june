# # # Q1.Define a function that takes 2 numbers and returns their product
# def prod(a, b):
#     return a * b
# prod(2,3)

# # Q2.Define a function that takes a string and returns number of vowels

# def count_vowels(s):
#     v = "aeiouAEIOU"
#     c = 0
#     for i in s:
#         if i in v:
#             c += 1
#     return c
#
# print(count_vowels("hariii"))


# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle

# def area(l, b):
#     a= l * b
#     print(a)
#
# area(2,3)
#
# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]
# #
# def even_list(l):
#     new = []
#     for i in l:
#         if i % 2 == 0:
#             new.append(i)
#     print(new)
#
# even_list(l)

# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
# def SumDigits(Lst):
#     new = []
#     for i in Lst:
#         sum = 0
#         for j in str(i):
#             sum = sum + int(j)
#         new.append(sum)
#     return new
#
#
# print(SumDigits(l))
