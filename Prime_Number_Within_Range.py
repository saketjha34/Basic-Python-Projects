

lower_limit = int(input("Enter Lower Limit : "))
upper_limit = int(input("Enter upper Limit : "))
print(f"Prime Numbers in range {lower_limit} , {upper_limit} are : ")

for i in range(lower_limit,upper_limit+1,1):
    n = 0 
    for j in range(2,i,1):
        if i % j == 0:
            n = 1
            break
    if n == 0:
        print(i , end = " ")



