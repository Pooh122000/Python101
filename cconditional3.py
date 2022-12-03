username = "Sneha"
pswd = "123456"

User = str(input("Enter the username \n"))
word = str(input("Enter the password \n"))

if(User == username and word == pswd):
    print("login")

else:
    print("Incorrect password")
    opt = input("Do yo want to reset the password \n 1.yes 2.no \n")

    if(opt == "yes"):
        new = str(input("Enter the new password \n"))
        confirm = str(input("Enter the confirm password \n"))

        if(new == confirm):
            print("password resetted")

        else:
            print("Passwors doesn't match")

    else:
        print("ok bye")
