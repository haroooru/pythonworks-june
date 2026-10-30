# r -read
# w- write
# a mode - append mode - operation starts at end of file content
from re import search

# r+
# w+   read+ write


# a+ - append plus read

# non file operation - image / texts
#
# rb - read binary
# wb
# ab
# wb+
# rb+
# ab+



#
# operation start  point starts at beggining
# for read but at end at a - append
#


# f = open('k.txt','a')
# f.write("python")
#
# f.close()
#
# #python appears at last
# #write a program to read the content from one text file
# #and appends it into another txt file
#
# f = open("p.txt", "r")
# content = f.read()
# f1 = open("k.txt","a")
# f1.write(content)

#
# f = open("k.txt","a+") #append + read
#
#
# f.write("python") #append
# content = f.read() #read
# print(content)

#nothing prints - why - becase point is at end and
#it needs to come to beggining so

# so we use seek() - change the file pointer position
# and tell() function - returns the current file pointer position

# f=open("k.txt","a+")
# print("current position",f.tell())
# f.write("python")
# print("current position",f.tell())
#
# content=f.read()
#
# print("content",content)
# f.close()
#
# # now seek
#
# f=open("k.txt","a+")
# print("current position",f.tell())
# f.write("python")
# print("current position",f.tell())
#
# f.seek(0) #bring file position to beginning
# print("current position",f.tell())
# content=f.read()

#
# file operations
#
# read
# write
# append
# search
# delete


# to delete

# import os  # build in module for system related functionalities
# os.remove(filename)  #mkdir , emdir,rename , getcwd, chewd()

# import os
# os.remove("k.txt")





