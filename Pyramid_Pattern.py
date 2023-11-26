
def pattern(n):
    for i in range(n):

        for j in range(i,n):
            print(' ' , end = '')

        for k in range(i+1):
            print('*' , end = '')

        for l in range(i):
            print('*' , end = '')
        print()
 
 
n = int(input('Enter Number'))
pattern(n)


