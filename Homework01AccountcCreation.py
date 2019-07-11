while True:
    try:
        process = int(input("""\nPlease Select From the Following Options:
    1-Create an Account
    2-Exit
    Your Selection: """))
        if process == 1:
            with open("registrationFile.txt", "a+") as f:
                username = input("Please Enter a Username: ")
                for i in f.readlines():
                    if (username + '\n') == i:
                        print("Unfortunately This Username is Taken.")
                        break
                else:
                    password = input("Please Enter a Password: ")
                    f.write(username + '\n')
                    print("Congratulations, Your Account is Created.")
                    break
        elif process == 2:
            print("Exiting The Program.")
            break
        else:
            print("Something Went Wrong, Please Try Again!")
    except ValueError:
        print("Please Enter '1' or '2'")