# 5.2 Write a program that repeatedly prompts a user
# for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and 
# smallest of the numbers. If the user enters anything
# other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

# Establishes initial values to None
largest = None
smallest = None

# Infinite loop to process user inputted values
while True:
    # Prompts user to input a number value
    num = input("Enter a number: ")
    # When user inputs "done" exit loop and jump to print statements
    if num == "done" :
        break
    try :
        # Converts user inputted string to int
        value = int(num)
        # If loop to find maximum and minimum values
        if largest is None :
            largest = value 
        elif value > largest :
            largest = value
        if smallest is None :
            smallest = value
        elif value < smallest :
            smallest = value
    except :
        # If user inputs invalid value, error will be shown
        print("Invalid input")
        continue 
# Prints maximum and minimum values from input      
print("Maximum is", largest)
print("Minimum is", smallest)


    


