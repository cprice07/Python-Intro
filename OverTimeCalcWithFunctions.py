# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours
# worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() 
# and use the function to do the computation. The function should return a value. Use 45 hours and a 
# rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read 
# a string and float() to convert the string to a number. Do not worry about error checking the user 
# input unless you want to - you can assume the user types numbers properly. Do not name your variable
# sum or use the sum() function.


# Function designated to compute regular and overtime pay
def computepay(h, r):
    # For all hours worked at or below 40 pay hourly rate
    if h <= 40 :
        total = h * r
        return (total)
    # For all hours worked above 40 pay overTime and add to regular pay
    else :
        normalRate = 40 * r
        overTime = h - 40
        overRate = r * 1.5
        overPay = overTime * overRate
        return (overPay + normalRate)

# Prompt user input for hours worked
hrs = input("Enter Hours: ")
# Prompt user input for rate per hour
rate = input("Enter Rate Per Hour: ")

# Convert string input to float
h = float(hrs)
r = float(rate)

# Call function computepay() to  calculate total pay
p = computepay(h, r)

#Print result of calculation
print("Pay", p)