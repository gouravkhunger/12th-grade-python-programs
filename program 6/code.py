# Prompt the user to enter a string
string = input("Enter a string: ")

# Initialize a flag to track whether the string is a palindrome
is_palindrome = True

# Use a loop to check if the string is a palindrome
for i in range(len(string) // 2):
    if string[i] != string[-i - 1]:
        is_palindrome = False
        break

# Print the result
if is_palindrome:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")

