
def prime_number_range(lower_limit,upper_limit):
    if (lower_limit >0 ) and (upper_limit>0):
        for i in range(lower_limit,upper_limit+1,1):
            n = 0 
            if i ==1 :
                continue
            else:    
                for j in range(2,i,1):
                    if i % j == 0:
                        n = 1
                        break
                if n == 0:
                    print(i , end = " ")

    else:
        print('Error')

if __name__ == '__main__':
    lower_limit = int(input("Enter Lower Limit : "))
    upper_limit = int(input("Enter upper Limit : "))
    prime_number_range(lower_limit,upper_limit)

