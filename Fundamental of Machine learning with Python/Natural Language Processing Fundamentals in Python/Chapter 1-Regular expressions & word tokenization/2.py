# Word tokenization with NLTK
# Here, you'll be using the first scene of Monty Python's Holy Grail, which has been pre-loaded as scene_one. Feel free to check it out in the IPython Shell!

# Your job in this exercise is to utilize word_tokenize and sent_tokenize from nltk.tokenize to tokenize both words and sentences from Python strings - in this case, the first scene of Monty Python's Holy Grail.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Import the sent_tokenize and word_tokenize functions from nltk.tokenize.
# Tokenize all the sentences in scene_one using the sent_tokenize() function.
# Tokenize the fourth sentence in sentences, which you can access as sentences[3], using the word_tokenize() function.
# Find the unique tokens in the entire scene by using word_tokenize() on scene_one and then converting it into a set using set().
# Print the unique tokens found. This has been done for you, so hit 'Submit Answer' to see the results!

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
print(unique_tokens)
