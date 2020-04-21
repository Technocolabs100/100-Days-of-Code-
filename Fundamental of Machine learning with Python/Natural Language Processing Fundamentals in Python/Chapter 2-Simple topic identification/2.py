# Exercise
# Exercise
# Text preprocessing practice
# Now, it's your turn to apply the techniques you've learned to help clean up text for better NLP results. You'll need to remove stop words and non-alphabetic characters, lemmatize, and perform a new bag-of-words on your cleaned text.

# You start with the same tokens you created in the last exercise: lower_tokens. You also have the Counter class imported.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Import the WordNetLemmatizer class from nltk.stem.
# Create a list called alpha_only that iterates through lower_tokens and retains only alphabetical characters. You can use the .isalpha() method to check for this.
# Create another list called no_stops in which you remove all stop words, which are held in a list called english_stops.
# Initialize a WordNetLemmatizer object called wordnet_lemmatizer and use its .lemmatize() method on the tokens in no_stops to create a new list called lemmatized.
# Finally, create a new Counter called bow with the lemmatized words and show the 10 most common tokens.

#Text preprocessing practice
# Import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer

# Retain alphabetic words: alpha_only
alpha_only = [t for t in lower_tokens if t.isalpha()]

# Remove all stop words: no_stops
no_stops = [t for t in alpha_only if t not in english_stops]

# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

# Create the bag-of-words: bow
bow = Counter(lemmatized)

# Print the 10 most common tokens
print(bow.most_common(10))