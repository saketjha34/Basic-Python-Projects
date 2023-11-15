# Exercise 8:  print  fibonacci series upto specified number
a = 0
b = 1
number = int(input('Hey User Enter The number : '))
print(a)
for i in range(0,number+1):  
    c = a+b
    a = b
    b = c
    print(c, end = " ")

