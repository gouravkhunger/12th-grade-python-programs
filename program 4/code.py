# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Initialize a variable to store the factorial
factorial = 1

# Calculate the factorial using a loop
for i in range(1, num + 1):
    factorial *= i

# Print the result
print(f"The factorial of {num} is {factorial}.")

