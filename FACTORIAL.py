

number = int(input("Hey User Enter The Number : "))
const = 1
while not number >= 0:
    number = int(input("Hey User Please  Enter a Valid Number : "))    
else:
    for number in range(1,number+1):
        const = const*number    
    print(f"{number}! = ",const)

    