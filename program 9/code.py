# Open the input file in read mode and the output file in write mode
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
  
  # Read the contents of the input file line by line
  for line in input_file:
    # If the line does not contain the character "a", write it to the output file
    if "a" not in line:
      output_file.write(line)

