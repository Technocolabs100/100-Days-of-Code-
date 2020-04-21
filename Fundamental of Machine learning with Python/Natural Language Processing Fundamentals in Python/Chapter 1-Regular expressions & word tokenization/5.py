# Non-ascii tokenization
# In this exercise, you'll practice advanced tokenization by tokenizing some non-ascii based text. You'll be using German with emoji!

# Here, you have access to a string called german_text, which has been printed for you in the Shell. Notice the emoji and the German characters!

# The following modules have been pre-imported from nltk.tokenize: regexp_tokenize and word_tokenize.

# Unicode ranges for emoji are:

# ('\U0001F300'-'\U0001F5FF'), ('\U0001F600-\U0001F64F'), ('\U0001F680-\U0001F6FF'), and ('\u2600'-\u26FF-\u2700-\u27BF').

# Instructions
# 100 XP
# Instructions
# 100 XP
# Tokenize all the words in german_text using word_tokenize(), and print the result.
# Tokenize only the capital words in german_text.
# First, write a pattern called capital_words to match only capital words. Make sure to check for the German Ü!
# Then, tokenize it using regexp_tokenize().
# Tokenize only the emoji in german_text. The pattern using the unicode ranges for emoji given in the assignment text has been written for you. Your job is to use regexp_tokenize() to tokenize the emoji.

#Non-ascii tokenization
# Tokenize and print all words in german_text
all_words = word_tokenize(german_text)
print(all_words)

# Tokenize and print only capital words
capital_words = r"[A-ZÜ]\w+"
print(regexp_tokenize(german_text, capital_words))

# Tokenize and print only emoji
emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
print(regexp_tokenize(german_text, emoji))