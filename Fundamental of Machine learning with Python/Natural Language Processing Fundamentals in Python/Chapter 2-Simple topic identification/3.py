# Exercise
# Exercise
# Creating and querying a corpus with gensim
# It's time to apply the methods you learned in the previous video to create your first gensim dictionary and corpus!

# You'll use these data structures to investigate word trends and potential interesting topics in your document set. To get started, we have imported a few additional messy articles from Wikipedia, which were preprocessed by lowercasing all words, tokenizing them, and removing stop words and punctuation. These were then stored in a list of document tokens called articles. You'll need to do some light preprocessing and then generate the gensim dictionary and corpus.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Import Dictionary from gensim.corpora.dictionary.
# Initialize a gensim Dictionary with the tokens in articles.
# Obtain the id for "computer" from dictionary. To do this, use its .token2id method which returns ids from text, and then chain which returns tokens from ids. Pass in "computer" as an argument to .get().
# Use a list comprehension in which you iterate over articles to create a gensim MmCorpus from dictionary.
# In the output expression, use the .doc2bow() method on dictionary with article as the argument.
# Print the first 10 word ids with their frequency counts from the fifth document. This has been done for you, so hit 'Submit Answer' to see the results!

from gensim.corpora.dictionary import Dictionary

# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)

# Select the id for "computer": computer_id
computer_id = dictionary.token2id.get("computer")

# Use computer_id with the dictionary to print the word
print(dictionary.get(computer_id))

# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in articles]

# Print the first 10 word ids with their frequency counts from the fifth document
print(corpus[4][:10])