

n = int(input('Enter Number'))

for  i in range(n):

    for j in range(i,n):
        print(' ' , end = '')
    for k in range(i+1):
        print('*' , end = '')
    for k in range(i):
        print('*' , end = '')               
    print()

     
    

