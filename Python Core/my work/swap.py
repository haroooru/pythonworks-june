# a = 3
# b = 5
#
# a,b=b,a
# print(a)
# print(b)


#slice operation

# s = "hello world"
# print(s[0:5])
# print(s[6:])
# print(s[::-1])

# s = "python coding is easy and fun"
# print(len(s))
# print(s[::-1])
# print(s[0])
# print(s[-1])
# print(s[2:11])
# print(s[12])
# print(s[5])

# print(11+10)
# print("11"+"10")
# print("hello"+"world")
#
# s ="hello"
# print(s*3)
#
# print("12"*3)
# print(12*3)
#
#
# s = [10, 20, 30]
# s[0]=100
# print(s)
#
# # error example
#
# # s=(10,20,30)
# # s[0]=100
# # print(s)
#
# s.append(40)
# print(s)

num = int(input("enter a number"))
s = str(num)
sum=0
for i in s:
    sum=sum+int(i)
print(sum)