# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. 

# Prompts user input
score = input("Enter Score: ")
# Converts user input from string to float
sc = float(score)

# If user input is above 1.0 or below 0.0 print error
# Otherwise print corresponding grade to input value
if sc > 1.0:
    print("Error: must enter number between values of 0.0 and 1.0.")
    quit()
elif sc >= 0.9:
    print("A")
elif sc >= 0.8:
    print("B")
elif sc >= 0.7:
    print("C")
elif sc >= 0.6:
    print("D")
elif sc < 0.0:
    print("Error: must enter number between values of 0.0 and 1.0.")
    quit()
elif sc < 0.6:
    print("F")





