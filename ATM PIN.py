import time         #Time module imported for time functions
attempts = 3        #Providing 3 attempts to the user before exiting after failed attempts
pin = ""

while True:
    while attempts > 0:
        pin = input(f"\nEnter your PIN ({attempts} attempts left): ")  # To store input value
        if pin == "python123":  # condition applied to prompt statements to the user
            print("Welcome to your account!")  # Output when desired input received
            break # Loop breaks on successful output
        else:
            attempts -= 1  # attempts reduced if wrong input received
            if attempts > 0:
                print(f"Incorrect PIN, try again! ({attempts} attempts left)")
            else:
                print("Too many failed attempts! Please wait 5 seconds before retrying...")
                time.sleep(5)  # time delay of 5 seconds before option to retry
                attempts = 3
                pin = ""
    if pin == "python123":
        break           ##exiting second while loop