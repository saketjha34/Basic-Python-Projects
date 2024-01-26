
def table(number):
    for i in range(1,11,1):
        z = number * i
        print(f"{number} * {int(i)} =",z)   

if __name__ == '__main__':
    number = int(input('Hey User Enter the number'))    
    table(number)