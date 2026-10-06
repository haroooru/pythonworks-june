# theres different type of files eg. text json file csv
from platform import java_ver
from pprint import pformat

# suntaxxx open('file name' , 'accessmode')

#file write operation , so it writes to text file from python,

f = open('k.txt', 'w')

# if its running well create a new text file so now to write, if already exist its content erases

# syntaxxx f.write(string)

f.write('hello')
# f.close()

# if you comment above and run again it erases from txt file

#for paragraph

sample_paragraph = """Excited to share that I have been promoted from Clinical 
Application Specialist to Territory Manager – Karnataka at Beats Medical Systems. 

Grateful to the entire team, especially Kurian Alapatt and Manikandan Surendran 
for their trust, support, and guidance throughout my journey. Looking forward to
taking on this new responsibility, contributing to business growth, strengthening
customer relationships, and supporting the adoption of advanced medical 
technologies across Karnataka.

Excited for the journey ahead!\n"""

f.write(sample_paragraph )



#for list

# syntaxx f.writelines(list )

content = ["python\n","java\n","pdf\n"]
f.writelines(content)


#now its READ operation

#file should already exist for read files or else file not found error occurs
#read has READ and READLINES
# for STRING and LIST
#
# f = open("k.txt","r")
#
# # read()
# # readlines()
#
# content = f.read()
# print(content)
#
# content = f.readlines()
# print(content)
#
# f.close()
#
#
# print()
# print()
#
#
# #read a text file and display number of lines in it
#
# f= open("k.txt","r")
# content = f.readlines()
# print(content)
# print(len(content))
#
# #read a text file and display number of words in it
#
# f= open("k.txt","r")
# content = f.read()
# print(content.split())
# print(len(content.split()))
#



#update second line

f = open("k.txt","r")
content = f.readlines()
content[1]="new line\n"

f=open("k.txt","w")
f.writelines(content)
f.close()

#display the last line

f = open("k.txt","r")
c = f.readlines()
print(c[-5:])


#search up a particular word

f = open("k.txt","r")
content = f.read()
word = input("enter a word")
if word in content:
    print(word,"found")
else:
    print("not found")

#find number of letter, digits and space in file

# find number of letters, digits and spaces in file

f = open("k.txt","r")
content = f.read()

l_count = 0
s_count = 0
d_count = 0

for ch in content:
    if ch.isalpha():
        l_count += 1
    elif ch.isdigit():
        d_count += 1
    elif ch.isspace():
        s_count += 1

print("Letters =", l_count)
print("Digits =", d_count)
print("Spaces =", s_count)

f.close()

#revers

# pfp
# java
# python
c= ["python\n","java\n","pfp\n"]
p =open("p.txt","w")
p.writelines(c)
p.close()

p =open("p.txt","r")
content = p.readlines()
content.reverse()
print(content)
p.close()

p =open("p.txt","w")
p.writelines(content)
p.close()

# or

# read back
p = open("p.txt","r")
content = p.readlines()
p.close()

# reversed copy using slicing
rev = content[::-1]

print(rev)   # shows ['pfp\n', 'java\n', 'python\n']

# write reversed copy back
p = open("p.txt","w")
p.writelines(rev)
p.close()




# 54321
# 4321
# 321
# 21
# 1

for i in range (1,6):
    for j in range(5,i-1,-1):
        print(j,end =" ")
    print()


# file called total students names of all students in class
#passed students txt contains only passed students
# write the name of failed childs into new txt file

# total students file
f_total = open("total.txt","w")
f_total.writelines(["Asha\n","Ravi\n","Meera\n","Kiran\n","Anu\n"])
f_total.close()

# passed students file
f_passed = open("passed.txt","w")
f_passed.writelines(["Asha\n","Meera\n","Anu\n"])
f_passed.close()




# failed students list using readlines/writelines

# read all students
f_total = open("total.txt","r")
total = f_total.readlines()
# f_total.close()

# read passed students
f_passed = open("passed.txt","r")
passed = f_passed.readlines()
# f_passed.close()

# find failed students
failed = []
for name in total:
    if name not in passed:
        failed.append(name)

# write failed students into new file
f_failed = open("failed.txt","w")
f_failed.writelines(failed)
f_failed.close()



print("Failed students written to failed.txt")

#
# two txt file swiggy  ,zomato has list list of foods combine them and combine
# them and count number of each food item create dictionary


# combine swiggy and zomato into one file and count



# read swiggy
f1 = open("swiggy.txt","r")
swiggy = f1.readlines()
f1.close()

# read zomato
f2 = open("zomato.txt","r")
zomato = f2.readlines()
f2.close()

# write combined into new file
f3 = open("combined.txt","w")
f3.writelines(swiggy + zomato)
f3.close()

# read combined back
f3 = open("combined.txt","r")
all_foods = f3.readlines()
f3.close()

# count dictionary
food_count = {}
for item in all_foods:
    item = item.strip()   # clean newline
    if item in food_count:
        food_count[item] += 1
    else:
        food_count[item] = 1

print(food_count)

#a file contain names and marks of  students like rahul 20 next line miya 40
# like that write a code to make file of students who  scored more than 70
# now read the file
f = open("students.txt","r")
lines = f.readlines()
f.close()

# filter students with marks > 70
passed = []
for line in lines:
    name, mark = line.split()   # split into name and mark
    mark = int(mark)            # convert mark to number
    if mark > 70:
        passed.append(line)     # keep the whole line

# write passed students into new file
f = open("passed.txt","w")
f.writelines(passed)
f.close()

# or

# read file
f = open("students.txt","r")
s = f.readlines()
f.close()

# write passed students
f2 = open("passed.txt","w")

for line in s:
    parts = line.split()      # ['Rahul','20']
    name = parts[0]
    mark = int(parts[1])
    if mark > 70:
        f2.write(name + "\n")

f2.close()
