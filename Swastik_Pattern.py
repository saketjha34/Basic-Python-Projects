
def main():
    for i in range(4):
        for j in range(7):
            if (i in range(0,3) and j in range(1,3)) or (i in range(1,3) and j in range(4,7)):
                print(" " , end = '')
            else:
                print("*" , end = '')
        print() 
    for k in range(3):
        for l in range(7):
            if (k in range(0,2) and l in range(0,3)) or (k in range(0,3) and l in range(4,6)):
                print(" " , end = '')
            else:
                print("*" , end = '')
        print()

main()

