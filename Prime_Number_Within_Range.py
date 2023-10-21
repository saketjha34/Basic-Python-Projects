

startinput = int(input("Enter Starting point : "))
finalinput = int(input("Enter final point : "))

for i in range(startinput,finalinput+1,1):
    for j in range(2,i,1):
        if i % j == 0:
            break
    else:
        print("Prime Numbers are",i, end = " ")



