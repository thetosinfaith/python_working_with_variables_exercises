#Create a program that reassigns a variable with a new data type after its initial assignment and handles any resulting errors.

try:
    x = 10
    y = 'Africa Most Celebrated Woman in Technology ';
    result = x + y

except TypeError as e:
    print(f"Error: {e}")

