grading_system_prompt = input("Press \"yes\" For Grading System OR Press no To Continue Without it : ")

if grading_system_prompt == "yes":
    print(''' 
       
    Percentage >= 95          A+ \n
    Percentage < 95 & >= 90   A \n
    Percentage < 90 & >= 80   B+\n
    Percentage < 80 & >= 70   B\n
    Percentage < 70 & >= 60   C\n
    Percentage < 60 & >= 50   D\n
    Percentage < 50 & >= 40   E\n
    Percentage < 40 & >= 35   F\n
    Percentage < 35        FAIL\n
                             
    ''')

else:
    pass    

percentage = float(input("Enter Your Percentange: "))

if percentage >= 95 :
    print("You Got A+ Grade")
elif percentage < 95 and percentage >= 90:
    print("You Got A Grade ") 
elif percentage < 90 and percentage >= 80:
    print("You Got B+ Grade ") 
elif percentage < 80 and percentage >= 70:
    print("You Got B Grade ") 
elif percentage < 70 and percentage >= 60:
    print("You Got C Grade ")
elif percentage < 60 and percentage >= 50:
    print("You Got D Grade ")
elif percentage < 50 and percentage >= 40:
    print("You Got E Grade ")
elif percentage < 40 and percentage >= 35:
    print("You Got F Grade ")
else:
    print("You Have Failed!!")    
