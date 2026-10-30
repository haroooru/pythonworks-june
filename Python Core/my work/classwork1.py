*#1Given a string
s="I am learning Python"

# find the length of the string
len(s)
print(s)
# find the reverse of the string
s[::-1]
# find the last character of the strings
s[-1]
#find the 13th character
s[12]
#print the characters from 2nd index to 15 th index
s[2:15]
#combines the string s with word "programming"
print(s+" programming")
# #2.Given a listp0
l=['Guitar','Piano','Violin','Drums','Flute']
# Add a new item 'Veena' to the list
l.append("veena")
print(l)
# #3Declare a list of 5 food items
food = ["pizza","burger","shawarma","bonda","vada"]
#     #Add new fooditem to the list
food.append("dosa")
print(food)

#     #change the second food item
food[1]="idli"

#     #print the updated list
print(food)
#     #print the last food item
print(food[-1])
#     #print the number of food items
print(len(food))

# #4.Given a string s="python is a programming language"
s="python is a programming language"
# #Remove the first 10 characters and print the remaining
print(s[10:])
# #print the last 5 characters
print(s[-5:])
#5.l=[10,56,23,67,19,70]
l=[10,56,23,67,19,70]
#interchange 2nd index and 5th index numbers
l[2],l[5]=l[5],l[2]
print(l)

#6iven a set
# s={10,20,30,40}
s={10,20,30,40}
# Add a new number 50 to the set
s.add(50)
print(s)