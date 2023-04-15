# Prompt user for hours worked
hrs = input("Enter Hours:")
# Convert user inputted string to a float
hrs = float(hrs)

# Prompt user for rate of pay
rate = input("Enter Rate:")
# Convert user inputted string to a float
rate = float(rate)

# Calculate pay rate
payRate = rate * hrs

# Output string and float for user
print("Pay:", payRate)