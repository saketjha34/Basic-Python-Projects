database_usernames = ["saket","suvarnajha01","madhuri","shubham",]
database_passwords = ["saket23","suvarna123","madhuri54","Shubham@124"]
main = True
username_input = input(f"Hey User Enter Your Username : ")
while main:
    if not username_input in database_usernames:
        username_input = input(f"Hey User Re-Enter Your Username : ")
    else:
        main = False    
else:
    submain = True 
    password_input = input(f"Hey  {username_input} Enter  Your Password : ")
    while submain:
        if not password_input in database_passwords:
            password_input = input(f"Hey {username_input} Re-Enter Your password : ")
        else:
            submain = False  
    else:
        print("--------------------")
        print(f"Logined Successfully as Username : {username_input} & Password : **********")
        print("--------------------")
        querry_1 = input(f"Hey {username_input} do you want to add/remove entries type(y/n)")
        if querry_1.lower() == "y":
            new_username_input = input(f"Hey {username_input} Enter The New Username : ")
            new_user_added = database_usernames.append(new_username_input)
            new_password_input = input(f"Hey {username_input} Enter The New Password : ")
            new_user_password_added = database_passwords.append(new_password_input)
            print(" Done Successfully !")
            for username in database_usernames:
                print(username)
        else:
            print("Thanks")    
            

