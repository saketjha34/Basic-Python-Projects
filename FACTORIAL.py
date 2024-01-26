
def factorial(number):
    const = 1
    while not number >= 0:
        number = int(input("Hey User Please  Enter a Valid Number : "))    
    else:
        for number in range(1,number+1):
            const = const*number    
        print(f"{number}! = ",const)


## Recursion Program

# def factorial(number):
#     if number == 0:
#         return 1
#     else:
#         return number * factorial(number -1)


number = int(input("Hey User Enter The Number : "))

