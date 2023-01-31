# Open the file in read mode
with open('file.txt', 'r') as file:
  
  # Read the contents of the file line by line
  for line in file:
    # Print each line
    print(line, end = '')

