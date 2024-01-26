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
if __name__ == '__main__':

    for i in range(5):
        for j in range(5-i):
            print(" ", end="") 
        for  k in range(i+1): 
            print("*", end="")
        for l in range(i):
            print("*", end="")
        print()
    
    for m in range(4):
        for n in range(m+2):
            print(" ", end="")
        for o in range(4-m):
            print('*', end="")
        for p in range(3-m):
            print('*', end="")
        print()
            
    

