'''
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
'''
# n ---> rows
def diamond_pattern(n):

    for i in range(n):
        for j in range((n-1)-i):
            print(' ',end='')
        for k in range(i+1):
            print('*',end='')
        for l in range(i):
            print('*',end='')
        print()
    for i in range(n-1):
        for j in range(i+1):
            print(' ',end='')
        for k in range((n-1)-i):
            print('*',end='')
        for l in range((n-2)-i):
            print('*',end='')
        print()
     
if __name__ == '__main__':
    n = int(input("Enter Number of rows : "))
    diamond_pattern(n)
