# read entire file content as single string

f=open("k.txt","r")   #open file in read mode

content=f.read()      #returns file content as string
print(content)

f.close()
