# #int
# x=10
#
# #complex
# x=10.30
#
# #complex
# x = 1+10j
#
# #string
# x= "hello world"
#
# #list
# x =["hii",100, 20.4]
#
# #tuple
# x =(1,2,3,"blahh")
#
# #set
# x={1,3,5,"hello"}

# d = {"name":"hari","place":"ekm","age":23}
# print(d["name"])
# print(d["place"])
# print(d["age"])
# d["course"]="python"
# print(d["course"])
#
# print(d)
# d["age"]=101
# print(d)
#
# print(d.items())
# print(d.values())

#1.Given a list

# l=[12,45,23,67]
# #print second element
# print(l[1])
# #2.Given a list
# l=[['arun',30],['amal',24],['anu',12]]

# #print second element
# print(l[1])
# #print the second name
# print(l[1][0])
#
# #3.Given a list
# d={101:['arun',23,'ekm'], 102:['amal',25,'tvm']}
#
# #print the second element
# print(d[102])
# #print the second name
# print(d[102][0])
#
# https://classroom.google.com/c/ODU1MjE0MzYzMDM3

#program to display a number


# #with conditions
# if num<100:
#     print(num+100)
#
# if (num%2==0):
#     print("lalalalala")
#
# if (num<10):
#     print("smallll")

#
# num = input("enter a number")

# if num>0:
#     print(num,"is positive")

# if (num%3==0 and num%5==0):
#     print(num)

# if ("n" in num):
#     print(num, "has n in it")

# if (num[0]=="n"):
#     print(num, "has n in first")

# if ("land" in num):
#     print(num,"has land")
# else:
#     print("theres no land in it")

# num = int(input("enter a number"))
# if (num%2==0):
#     print(num,"is even")
# else:
#     print(num,"is odd")

# #Write a program to check whether two entered numbers are equal or not

# num1=int(input("enter number 1"))
# num2=int(input("enter number 2"))
# if (num1==num2):
#     print(num1,"and",num2,"are equal")

# #Write a program to check whether two entered words are equal or not

# wrd1=input("enter word 1")
# wrd2= input("enter word 2")
# if (wrd1==wrd2):
#     print(wrd1,"and",wrd2,"are equal")

# #Write a program to find the maximum of two numbers

# num1=int(input("enter number 1"))
# num2=int(input("enter number 2"))
# if (num1>num2):
#     print(num1)
# else:
#     print(num2)

# #write a program to check whether the entered character is vowel or not



# vowel = "AEIOUaeiou"
# character = input("enter a character")
#
# if character in vowel:
#     print(character, "is vowel")
# else:
#     print(character, "is not vowel")

# #Write a program to check whether the entered country name contains word 'land'

# country = input("enter country")
# if ("land" in country ):
#     print(country,"has land in it")
# else:
#     print("no land in given country")

# #write a program to check whether the entered number is 3 digit or not

# num = int(input("enter a number"))
# num = str(num)
# if (len(num)==3):
#     print(num,"is 3 digit")
# else:
#     print("not 3 digit")

#write a program to check whether the entered string is  palindromde or not

# word = input("Enter a word ")
# if (word== word[::-1]):
#     print(word,"is a palindromde")
# else:
#     print("not palindromde")

#Write a program to check whether a number is present in given list

# l=[23,67,12,90]
# num = int(input("enter a number"))
# if (num in l ):
#     print(num,"present in given list")
# else:
#     print("not present")

#Write a program to check whether a key is prsent in a dictionary or not

# d={101:'Arun',102:'Amal',103:'Anu'}
# key = int(input("enter the key "))
# if (key in d):
#     print(key,"is there in dict")
# else:
#     print(key,"not in dict")

#Write a program to check whether the given pasword is strong/weak(if length lessthan 8 weak)

# password = input("enter your password")
# if (len(password)<8) :
#     print("weak pass")
# else:
#     print("strong pass")

# num1 = int(input("enter  num 1"))
# num2 = int(input("enter  num 2"))
# num3 = int(input("enter  num 3"))
#
# if (num1>num2 and num1>num3):
#     print("num1 wins")
# elif (num2>num1 and num2>num3):
#     print("num2 wins")
# else:
#     print("num3 wins")







# # #write a program to check whether an entered number is 2 digit/3 digit/4 digit
# num = int(input("enter a num"))
# num = str(num)
# if (len(num)==2):
#     print("two digits")
# elif (len(num)==3):
#     print("three digits")
# elif (len(num)==4):
#     print("four digits")
# else:
#     print("invalid")

# #Write a basic calculator program to perform Arithmetic Operations (+,-,*,/)
# num1 = int(input("enter num1"))
# num2 = int(input("enter num2"))
# op=input("enter operator")
# if op=="+":
#     print(num1+num2)
# elif op=="-":
#     print(num1-num2)
# elif op=="*":
#     print(num1*num2)
# elif op=="/":
#     print(num1/num2)
# else:
#     print("invalid")


# #Write a program to print the number of days in a month
# month = input("enter month")
# l1 =["january","march","may","july","september","november"]
# l2=["april","june","augest","october","december"]
# l3 =["february"]
# if (month in l1 ):
#     print("31 days")
# elif(month in l2):
#     print("30 days")
# elif(month in l3):
#     print("28 days")
# else:
#     print("invalid")


#write a program to print the grade of a student based on entered score
# grade = int(input("enter grade"))
#
# if grade>=91 and grade<=100:
#     print("grade A")
# # 81-90    Grade B
# elif grade>=81 and grade<=90:
#     print("grade B")
# # 71-80    Grade C
# elif grade>=71 and grade<=80:
#     print("grade C")
# # 61-70    Grade D
# elif grade>=61 and grade<=70:
#     print("grade D")
# # Below 61 Grade E
# elif grade<=60:
#     print("grade E")
# else:
#     print("invalid")

#check weather number is positive even/odd or negative even/odd

# num = int(input("Enter a num"))
# if num>0:
#     print("positive")
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# if num<0:
#     print("negative")
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")

#check divisibility

# num = int(input("enter a num"))
#
# if num%2==0:
#     print("divisible by 2")
#     if num%3==0:
#         print("divisible by 2 and 3 ")
#     elif num%3!=0:
#         print("divisible by 2 but not by 3")
#
#
# elif num%2!=0:
#     print("not divisible by 2")
#     if num%3==0:
#         print("not divisible by 2 but divisible by 3 ")
#     elif num%3!=0:
#         print("not divisible by 2 and  3")
#
#
# else:
#     print("invalid")


