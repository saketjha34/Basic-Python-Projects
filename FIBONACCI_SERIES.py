def fibonacci(number):
    a = 0
    b = 1
    print(a , end=' ')
    for i in range(0,number+1):  
        c = a+b
        a = b
        b = c
        print(c, end = " ")

if __name__ == '__main__':
    number = int(input('Hey User Enter The number : '))
    fibonacci(number)