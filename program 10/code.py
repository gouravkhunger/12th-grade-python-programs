# Initialize variables to count the characters
num_vowels = 0
num_consonants = 0
num_uppercase = 0
num_lowercase = 0

# Open the file in read mode
with open('file.txt', 'r') as file:
  
  # Read the contents of the file
  contents = file.read()
  
  # Iterate over the characters in the file
  for char in contents:
    # Check if the character is a vowel, consonant, uppercase, or lowercase
    if char in 'aeiouAEIOU':
      num_vowels += 1
    elif char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
      num_consonants += 1
    if char.isupper():
      num_uppercase += 1
    elif char.islower():
      num_lowercase += 1

# Print the results
print(f"Number of vowels: {num_vowels}")
print(f"Number of consonants: {num_consonants}")
print(f"Number of uppercase characters: {num_uppercase}")
print(f"Number of lowercase characters: {num_lowercase}")

