# Create file
f = open("sample.txt", "w")
f.write("Hello\n")
f.write("Python\n")
f.write("Welcome\n")
f.write("Good Morning\n")
f.write("Thank You")
f.close()

# Read file
f = open("sample.txt", "r")
lines = f.readlines()
print("Number of lines =", len(lines))
f.close()



f = open("sample.txt", "r")
lines = f.readlines()
print("Number of lines =", len(lines))
f.close()




f = open("sample.txt", "r")
words = f.read().split()
print("Number of words =", len(words))
f.close()




f = open("sample.txt", "r")
lines = f.readlines()

for line in lines[-5:]:
    print(line, end="")

f.close()



word = input("Enter word: ")

f = open("sample.txt", "r")
data = f.read()

if word in data:
    print("Found")
else:
    print("Not Found")

f.close()



f = open("sample.txt", "r")
data = f.read()

letters = 0
digits = 0
spaces = 0

for ch in data:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1

print("Letters =", letters)
print("Digits =", digits)
print("Spaces =", spaces)

f.close()


f = open("sample.txt", "r")
lines = f.readlines()
f.close()

lines[1] = "Python is very easy\n"

f = open("sample.txt", "w")
f.writelines(lines)
f.close()

f = open("sample.txt", "r")
print(f.read())
f.close()



#_________________________________________________________________________________________________
# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed the exam.
# Write a Python program to:
# Read the names from both files.
# Find the students who did not pass.
# Write their names to a new file named failed_students.txt, one name per line.

f1=open("totalstudents.txt","w")
f1.write("Anu\n")
f1.write("Rahul\n")
f1.write("Meera\n")
f1.write("Arun\n")
f1.close()

f2=open("passedstudents.txt","w")
f2.write("Anu\n")
f2.write("Meera\n")
f2.close()

f1=open("totalstudents.txt","r")
f2=open("passedstudents.txt","r")
totalstudents=f1.readlines()
passedstudents=f2.readlines()
print(totalstudents)
print(passedstudents)
f1.close()
f2.close()

f3=open("failed_students.txt","w")
for students in totalstudents:
    if students not in passedstudents:
        f3.write(students)
f3.close()
#_________________________________________________________________________________________________
# Two files, swiggy.txt and zomato.txt, contain the names of food items ordered from each platform.
# Write a Python program to read words from swiggy.txt and zomato.txt,
# combine them, and count how many times each word appears.
# Store the result in a dictionary and print it.

f1=open("swiggy.txt","w")
f1.write("Pizza Burger Pizza")
f1.close()

f2=open("zomato.txt","w")
f2.write("Burger Dosa Pizza")
f2.close()

f1=open("swiggy.txt","r")
f2=open("zomato.txt","r")
swiggy=f1.read().split()
zomato=f2.read().split()
f1.close()
f2.close()

items=swiggy+zomato
d={}

for item in items:
    if item in d:
        d[item]=d[item]+1
    else:
        d[item]=1

print(d)

#_________________________________________________________________________________________________
# A file marks.txt contains the names and marks of students as shown below:
# Anu 80
# Rahul 65
# Meera 90
# Arun 70
# Write a Python program to read the file and write the names of students
# who scored more than 75 marks into a file named names.txt.

f1=open("marks.txt","w")
f1.write("Anu 80\n")
f1.write("Rahul 65\n")
f1.write("Meera 90\n")
f1.write("Arun 70\n")
f1.close()

f1=open("marks.txt","r")
f2=open("names.txt","w")

for k in f1:
    data=k.split()
    name=data[0]
    marks=int(data[1])

    if(marks>75):
        f2.write(name+"\n")

f1.close()
f2.close()
