import math
welcomemsg = input("Hey User Welcome to this Program Type \"enter\" to continue : ")

prompt = '''
Choose The Coresponding  Number From The Following Options to Calculate  Area/Volume OF Figures: \n
1.Area of Square
2.Perimter of Square
3.Area of Rectangle
4.Perimeter of Rectangle
5.Volume of Cube
6.Lateral Surface Area of Cube
7.Area Of Circle
8.Cicumference Of Circle
'''

while True:    
    if welcomemsg == "enter" or welcomemsg == "Enter" or welcomemsg == "enter":
        print(prompt)
        break
    else:
        welcomemsg2 = input("Hey User You Have entered a invalid input Please Press \"enter\" to continue the program: ")
        print(prompt)
        break
    
    

selectedoption = int(input("Please Select Any Option : "))


if selectedoption == 1 :
    lengtharsquare = int(input("Enter The Value Of Side Length : "))
    print("The Area Of Square is : ",  lengtharsquare*lengtharsquare)
elif selectedoption == 2 :
    lengthprsquare = int(input("Enter   Side Length : "))
    print("The Perimeter Of Square is : ",  4*lengthprsquare)
elif selectedoption == 3 :
    lengtharrectangle = int(input("Enter  Length : "))
    breadtharrectangle = int(input("Enter Breadth : "))
    print("The Area Of Rectangle is : ", lengtharrectangle*breadtharrectangle )
elif selectedoption == 4 :
    lengthprrectangle = int(input("Enter  Length : "))
    breadthprrectangle = int(input("Enter Breadth : "))
    print("The Perimeter Of Rectangle is : ", 2*(lengthprrectangle + breadthprrectangle) )
elif selectedoption == 5 :
    lengthvolcube = int(input("Enter The  Side Length : "))
    print("The Volume Of Cube is : ",  lengthvolcube*lengthvolcube*lengthvolcube)    
elif selectedoption == 6 :
    lengthlatcube = int(input("Enter The  Side Length : "))
    print("The Lateral SUrface Area Of Cube is : ",  6*lengthlatcube)
elif selectedoption == 7 :
    radiusarcircle = int(input("Enter The  Radius : "))
    print("The Area Of Circle is : ",  math.ceil(math.pi*radiusarcircle*radiusarcircle))
elif selectedoption == 8 :
    radiuscrcircle = int(input("Enter The  Radius : "))
    print("The Cicumference Of Circle is : ",  math.ceil(2*math.pi*radiuscrcircle))





