import pickle

def insert(roll_number, name):
  # Load data in the binary file
  try:  
    with open('students.dat', 'rb') as data_file:
      data = pickle.load(data_file)
  except:
    # In case of an error, use an empty dictionary
    data = {}

  # Append student to the data file
  data[roll_number] = { 'name': name }

  # Open the binary file in write mode
  with open('students.dat', 'wb') as data_file:
    # Write the new dictionary to the file
    pickle.dump(data, data_file)

def search(roll_number):
  # Open the binary file in read mode
  with open('students.dat', 'rb') as data_file:
    # Try reading data from the file
    try:
      student = pickle.load(data_file)

      # Check if the roll number of the student exists in the file
      if roll_number in student:
        # If the roll numbers exists, return the name of the student
        return student[roll_number]['name']

    except:
      # If we haven't found a matching roll number, return None
      return None

# Insert a few students' records
insert(10, "John")
insert(12, "George")
insert(14, "Wilson")

# Prompt the user to enter a roll number
roll_number = int(input("Enter a roll number: "))
name = search(roll_number)

if name:
    print(f"Name: {name}")
else:
    print("Roll number not found!")

