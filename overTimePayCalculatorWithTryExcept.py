#  3.1 Write a program to prompt the user for hours
#  and rate per hour using input to compute gross pay.
#  Pay the hourly rate for the hours up to 40 and 1.5 times
#  the hourly rate for all hours worked above 40 hours. 
#  Use 45 hours and a rate of 10.50 per hour to test the program
#  (the pay should be 498.75). You should use input to read a 
#  string and float() to convert the string to a number.
#  Do not worry about error checking the user input - assume 
#  the user types numbers properly.

#Prompts user input for hours worked
hrs = input("Enter Hours:")
#Prompts user input for rate per hour
rph = input("Enter Rate Per Hour:")

#try-except for input besides numeric
try:
    #Converts string input to float
    h = float(hrs)
    #Converts string input to float
    r = float(rph)
except:
    print("Error: please enter numeric input")
    quit()
#For all hours worked at or below 40 pay hourly rate
if h <= 40 :
    total = h * r
    print (total)
#For all hours worked above 40 pay overTime and add to regular pay
else :
    normalRate = 40 * r
    overTime = h - 40
    overRate = r * 1.5
    overPay = overTime * overRate
    print (overPay + normalRate)


