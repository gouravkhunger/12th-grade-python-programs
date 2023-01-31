# Prompt the user to enter the number of terms
num_terms = int(input("Enter the number of terms: "))

# Initialize the first two terms of the series
a, b = 0, 1

# Generate and print the Fibonacci series
for i in range(num_terms):
    print(a)
    a, b = b, a + b

