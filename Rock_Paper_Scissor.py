import random

def checkwinner(computer_turn,user_turn):
    if user_turn == computer_turn:
        print("its an tie")
    elif user_turn == "paper" and computer_turn == "rock":
        print(f"You Won : {user_turn}")
    elif user_turn == "rock" and computer_turn == "scissor":
        print(f"You Won : {user_turn}")
    elif user_turn == "scissor" and computer_turn == "paper":
        print(f"You Won : {user_turn}")
    else:
        print("You Lose Computer Wins!")

computer_choice = ["rock","paper","scissor"]
computer_turn = random.choice(computer_choice)

mainloop = True
while mainloop:
    user_turn = input("Hey User Enter Your Choice (q to quit): ")
    if user_turn == "q" or user_turn == "Q":
        mainloop = False
        print("Thanks For Playing!")
    else:
        print("------------------------------")
        print(f"Your Choice : {user_turn}")
        print(f"computer Choice : {computer_turn}")
        print("------------------------------")
        checkwinner(computer_turn,user_turn)
    

    

