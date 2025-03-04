import time  #for importing time module

attempts = 3
password = "" #set to an empty string

while True:
    while attempts > 0: #code breaks when input password is right.
        password = input("\nEnter the password : ")  # input field stores password
        if password == "python123":
            print("Login Successful!")  # prints confirmation if password is correct
            break  # exits the first while loop if password is correct
        else:
            attempts -= 1  # attempts reduced on wrong input
            if attempts > 0:
                print("Wrong! Try again")  # prompt to input for attempts left
            else:
                print("Too many Failed attempts! Access Denied")  # prompt when no attempts are left
                print("⏳ Please wait 5 seconds before retrying...")
                time.sleep(5)  # Wait for 5 seconds before ending
                attempts = 3
                password = ""
    if password == "python123":
        break           ##exiting second while loop