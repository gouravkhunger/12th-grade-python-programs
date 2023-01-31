def find_factorial(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    # Recursive case: multiply n by the factorial of n - 1
    else:
        return n * find_factorial(n - 1)

# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Calculate and print the factorial
factorial = find_factorial(num)
print(f"The factorial of {num} is {factorial}.")

