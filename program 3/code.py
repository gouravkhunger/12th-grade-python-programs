def is_armstrong(n):
    str_num = str(n)
    sum = 0
    for c in str_num:
        sum += int(c) ** 3
    return sum == n

# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

