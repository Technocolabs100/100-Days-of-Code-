# Exercise
# Exercise
# Gensim bag-of-words
# Now, you'll use your new gensim corpus and dictionary to see the most common terms per document and across all documents. You can use your dictionary to look up the terms. Take a guess at what the topics are and feel free to explore more documents in the IPython Shell!

# You have access to the dictionary and corpus objects you created in the previous exercise, as well as the Python defaultdict and itertools to help with the creation of intermediate data structures for analysis.

# The fifth document from corpus is stored in the variable doc, which has been sorted in descending order.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Print the top five words of bow_doc using each word_id with the dictionary alongside word_count. The word_id can be accessed using the .get() method of dictionary.
# Create a defaultdict called total_word_count in which the keys are all the token ids (word_id) and the values are the sum of their occurrence across all documents (word_count). Remember to specify int when creating the defaultdict, and inside the for loop, increment each word_id of total_word_count by word_count.
# Create a sorted list from the defaultdict, using words across the entire corpus. To achieve this, use the .items() method on total_word_count inside sorted().
# Similar to how you printed the top five words of bow_doc earlier, print the top five words of sorted_word_count as well as the number of occurrences of each word across all the documents.
doc = corpus[4]

# Sort the doc for frequency: bow_doc
bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)

# Print the top 5 words of the document alongside the count
for word_id, word_count in bow_doc[:5]:
    print(dictionary.get(word_id), word_count)
    
# Create the defaultdict: total_word_count
total_word_count = defaultdict(int)
for word_id, word_count in itertools.chain.from_iterable(corpus):
    total_word_count[word_id] += word_count

# Create a sorted list from the defaultdict: sorted_word_count 
sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1], reverse=True) 

# Print the top 5 words across all documents alongside the count
for word_id, word_count in sorted_word_count[:5]:
    print(dictionary.get(word_id), word_count)