# Open the file in read mode
with open('file.txt', 'r') as file:
  # Read the lines of the file one by one
  for line in file:
    # Split the line into words
    words = line.split()
    # Print the words separated by #
    print("#".join(words))

