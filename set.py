#set

num1 = {1,2,3,4,5,5,6}
num2 = set([4,5,6])
num2.add(7)
num1.remove(6)
print(num2)
print(7 not in num1)


#orginal

num1 = {1,2,3,4,5,5,6}
num2 = set([4,5,6])

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)