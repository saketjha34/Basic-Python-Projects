import math

def lcm(a,b):
    max_num = max(a,b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            break
        max_num +=1
    print(f"The LCM of ({a},{b}) is : " ,max_num)

def gcd(a,b):
    gcd = math.gcd(a,b)
    print(f"The HCF of ({a},{b}) is : " ,gcd)   


if __name__ == "__main__":
    mainloop = True
    num1 = int(input("Enter The First Number : "))
    num2 = int(input("Enter The Second Number : "))

    while mainloop:
        user_choice = ""
        while user_choice != "q":
            user_choice = input('''Hey User Type lcm/hcf for lcm or hcf of two numbers or q to quit or to play again type replay : ''').lower()       
            if user_choice == "lcm":
                lcm(num1,num2)
            elif user_choice == "hcf":
                gcd(num1,num2)
            elif user_choice == "replay":
                num1 = int(input("Enter The First Number : "))
                num2 = int(input("Enter The Second Number : "))
            else:
                mainloop = False
        else:
            print("Thanks!!")
