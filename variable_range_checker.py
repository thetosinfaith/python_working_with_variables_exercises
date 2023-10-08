# Create a program that assigns a numeric value to a variable and checks whether it falls within a specific range. Handle the case where the value is out of the defined range and provide feedback accordingly.

numeric_value = 10
lower_bound = 1
upper_bound = 100

if numeric_value >= lower_bound and numeric_value >= upper_bound:
    print("The numeric value is within the range.")

else:
    print("The numeric value is outside the range.")