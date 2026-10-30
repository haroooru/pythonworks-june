# # Write lines into a file
# f=open("k.txt","w")
# content=['python\n','java\n','php\n']
# f.writelines(content)
# f.close()
#
# # Read entire file (string)
# f=open("k.txt","r")
# s=f.read()
# print(s)
# f.close()
#
# # Read lines as list
# f=open("k.txt","r")
# s=f.readlines()
# print(s)
# f.close()
#
# # Count number of lines
# f=open("k.txt","r")
# lines=f.readlines()
# print("Number of lines =",len(lines))
# f.close()
#
# # Count number of words
# f=open("k.txt","r")
# s=f.read()
# print(len(s.split()))
# f.close()
#
# # Update second line
# f=open("k.txt","r")
# lines=f.readlines()
# f.close()
# lines[1]="new line\n"
# f=open("k.txt","w")
# f.writelines(lines)
# f.close()
#
# # Display last 5 lines
# f=open("k.txt","r")
# s=f.readlines()
# print(s[-5:])
# f.close()
#
# # Search for a word
# f=open("k.txt","r")
# s=f.read()
# if "python" in s:
#     print("found")
# else:
#     print("not found")
# f.close()
#
# # Count letters, digits, spaces
# f=open("k.txt","r")
# s=f.read()
# letters=digits=spaces=0
# for ch in s:
#     if ch.isalpha():
#         letters+=1
#     elif ch.isdigit():
#         digits+=1
#     elif ch.isspace():
#         spaces+=1
# print("Letters =",letters)
# print("Digits =",digits)
# print("Spaces =",spaces)
# f.close()
#
# f1=open("k.txt","r")
#
# content=f1.read()
#
# f2=open("p.txt","a")
#
# f2.write(content)
#
# f1.close()
# f2.close()















f1=open("k.txt","r")

content=f1.read()

f2=open("p.txt","a")

f2.write(content)

f1.close()
f2.close()