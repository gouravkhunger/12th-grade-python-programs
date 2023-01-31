emails = """
email1@example.com
email2@example.com
email3@example.com
email4@example.com
email5@example.com
email6@example.com
email7@example.com
email8@example.com
email9@example.com
email10@example.com
"""

# Split the string into a list of emails
email_list = emails.split('\n')

# Create an empty dictionary to store the word counts
word_counts = {}

# Iterate through the list of emails
for email in email_list:
  # Split the email into a list of words
  email = email.replace('@', ' ').replace('.', ' ')
  words = email.split()

  # Iterate through the list of words
  for word in words:
    # Update the count for the word in the dictionary
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1

# Sort the dictionary by count in descending order
sorted_word_counts = sorted([(value, key) for (key, value) in word_counts.items()], reverse = True)

# Print the most commonly occurring words
print("Most commonly occurring words:")
for count, word in sorted_word_counts:
  print(f"{word}: {count}")

