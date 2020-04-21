# Practicing regular expressions: re.split() and re.findall()
# Now you'll get a chance to write some regular expressions to match digits, strings and non-alphanumeric characters. Take a look at my_string first by printing it in the IPython Shell, to determine how you might best match the different steps.

# Note: It's important to prefix your regex patterns with r to ensure that your patterns are interpreted in the way you want them to. Else, you may encounter problems to do with escape sequences in strings. For example, "\n" in Python is used to indicate a new line, but if you use the r prefix, it will be interpreted as the raw string "\n" - that is, the character "\" followed by the character "n" - and not as a new line.

# Instructions

# Import the regular expression module re.
# Split my_string on each sentence ending. To do this:
# Write a pattern called sentence_endings to match sentence endings (., ?, and !).
# Use re.split() to split my_string on the pattern and print the result.
# Find and print all capitalized words in my_string by writing a pattern called capitalized_words and using re.findall().
# Remember the [a-z] pattern shown in the video to match lowercase groups? Modify that pattern appropriately in order to match uppercase groups.
# Write a pattern called spaces to match one or more spaces ("\s+") and then use re.split() to split my_string on this pattern, keeping all punctuation intact. Print the result.
# Find all digits in my_string by writing a pattern called digits ("\d+") and using re.findall(). Print the result.

import re

# Write a pattern to match sentence endings: sentence_endings
sentence_endings = r"[.?!]"

# Split my_string on sentence endings and print the result
print(re.split(sentence_endings, my_string))

# Find all capitalized words in my_string and print the result
capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, my_string))

# Split my_string on spaces and print the result
spaces = r"\s+"
print(re.split(spaces, my_string))

# Find all digits in my_string and print the result
digits = r"\d+"
print(re.findall(digits, my_string))