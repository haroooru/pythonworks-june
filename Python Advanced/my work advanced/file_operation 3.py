#MENU DRIVEN


# #revision
# # write a program to find max number in a list without max func
# #
# # hint = max = l[0]
#
# l =[23,34,56,78,56]
#
#
# max = l[0]
#
# for i in l:
#     if (i>max):
#         max = i
#
# print(max)
#same for min



# # MENU
#
# def f():
#     print("function hellooo")
#
# while(1):
#     print("1 option 1")
#     print("2 option 2")
#     print("3 exit ")
#
#     ch = int(input("Enter your choise "))
#     if ch ==1 :
#         print("hi")
#         f()
#
#     elif ch ==2:
#         print("helloo")
#
#     else:
#         exit()





#menu driven file operations


#
# def file_read():
#     file_name = input("enter file name")
#     f = open(file_name,"r")
#     content = f.read()
#     print(content)
#
#
# def file_write():
#     file_name = input("enter file name")
#     f = open(file_name, "w")
#     text = input("enter content to write")
#     f.write(text)
#     f.close()
#
#
# def file_append():
#     file_name = input("enter file name")
#     f = open(file_name,"a")
#     text = input("enter content to append")
#     f.write(text)
#     f.close()
#
#
# def file_search():
#     file_name = input("enter file name")
#     word = input("enter word to search")
#     f = open(file_name,"r")
#     content = f.read()
#     if word in content:
#         print("found")
#     else:
#         print("not found")
#     f.close()
#
#
#
# def file_remove():
#     import os
#     file_name = input("enter file name")
#     os.remove(file_name)
#     print("file removed")
#
#
#
#
# while(1):
#     print("""
#     1. file read
#     2. file write
#     3. file append
#     4. file search
#     5. file remove
#     6. exit""")
#
#     ch = int(input("enter your choice"))
#
#     if ch==1:
#         file_read()
#     if ch==2:
#         file_write()
#     if ch==3:
#         file_append()
#     if ch==4:
#         file_search()
#     if ch==5:
#         file_remove()
#     if ch==6:
#         exit()




# read and write jSON files

# download sample json file looks like disc
# import first
# import json
#
# read - json.load(filereference)
# write - json.dump(filereference , data)


#
# # for dict
# import json
# f= open("sample.json","r")
#
# content = json.load(f)
#
# print(content["students"][0])
#
# # for list
# import json
# f= open("sample2.json","r")
#
# content = json.load(f)
#
# print(content[0])

import json
data = [
    {"name":"arun","age": 20},
    {"name":"sasi","age": 21}
]

f= open("data.json" , "w")
json.dump(data, f)