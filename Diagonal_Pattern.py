'''
Enter Number : 6
*
 *
  *
   *
    *
     *
'''
def pattern(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                print('*' , end = '')
            else:
                print( ' ' , end = '')
        print()
if __name__ == "__main__":
    n = int(input('Enter Number : '))
    pattern(n)






