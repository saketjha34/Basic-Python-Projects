questions =  ["The term “Levant” often heard in the news roughly corresponds to which of the following regions?",
              "What Does the 2nd Law of Thermodynamics states?",
              "Which one of the following is used in preparing a natural mosquito repellent?",
              "Which Element Is The Most Abundant In Universe?",
              "Which of the following non-metalic element exists in liquid state at room temperature?"]

options = [["A.Region along the eastern Mediterranean shores ","B.Region along North African shores stretching from Egypt to Morocco ","C.Region along Persian Gulf and Horn of Africa ","D.The entire coastal Mediterranean Sea of areas"],
           ["A.ENTROPY of universe tends to maximum ","B.ENTROPY of system tends to maximum  ","C.ENTROPY of universe tends to minimum  ","D. ENTROPY of universe & system is conserved "],
           ["A.Congress grass ","B.Elephant grass ","C.Lemon grass ","D.Nut grass"],
           ["A.Nitrogen","B.Hydrogen ","C.Helium ","D.Krypton"],
           ["A.Mercury","B.Chlorine ","C.Cesium ","D.Bromine"]]

question_number = 0

correct_options = ["A","A","C","B","D"]

user_answer = []

score = 0


if __name__ == '__main__':
    mainloop = True
    while mainloop:
        print("Hey User Welcome To This Quiz Game")
        user_consent = input("Hey User Do You Want To Continue(y/n)")
        if user_consent.lower() == "y":                
            for question in questions:
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(question)
                for option in options[question_number]:
                    print(option)
                user_answer_input = input("Hey user Enter Your Answer(A,B,C,D) : ").upper()     
                user_answer.append(user_answer_input)   
                if user_answer_input == correct_options[question_number]:
                    score += 1
                    print('CORRECT!')
                else:
                    print("INCORRECT")   
                    # print(f"CORRECT OPTION IS {correct_options[question_number]}") 
                question_number += 1 
                print()
            print()    
            print("-------------------------------------------------------------------------")       
            print("User Your Answers : ",user_answer)
            # print("Correct Answers : ",correct_options)
            print("-------------------------------------------------------------------------")
            print()
            print(f"Your Score is {int(score)} out of {int(question_number)} ") 
            print("-------------------------------------------------------------------------")
            print()
            question_number = 0
            score = 0
            user_answer = []
        else:
            mainloop = False 
            print("Thanks User for playing the Quiz!") 
                

