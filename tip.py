while True:
    try:
        # Prompt the user to enter the bill amount
        bill_amount = float(input("Enter the bill amount\n"))
        
        # If the user has entered either zero or a negative number, prompt them to enter a valid input
        if bill_amount <= 0:
            print("Invalid entry, please enter a number greater than zero.")
            continue
        break
    except ValueError:
        # If the user has entered a non-numerical input, prompt them to enter a valid input
        print("Invalid entry, please enter a number greater than zero.")

# Same for the tip percentage
while True:
    try:
        tip_percentage = float(input("Enter the tip percentage\n"))
        
        if tip_percentage <= 0:
            print("Invalid entry, please enter a number greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid entry, please enter a number greater than zero.")

# Calculate and display the tip, rounded to 2 decimals
print("Tip: $" + str(round(tip_percentage / 100 * bill_amount, 2)) + ".")

# In the end, prompt the user to press Enter, in order to exit the program
input("Press Enter to exit the program")