# Comparing NLTK with spaCy NER
# Using the same text you used in the first exercise of this chapter, you'll now see the results using spaCy's NER annotator. How will they compare?

# The article has been pre-loaded as article. To minimize execution times, you'll be asked to specify the keyword arguments tagger=False, parser=False, matcher=False when loading the spaCy model, because you only care about the entity in this exercise.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Import spacy.
# Load the 'en' model using spacy.load(). Specify the additional keyword arguments tagger=False, parser=False, matcher=False.
# Create a spacy document object by passing article into nlp().
# Using ent as your iterator variable, iterate over the entities of doc and print out the labels (ent.label_) and text (ent.text).

# Import spacy
import spacy

# Instantiate the English model: nlp
nlp = spacy.load('en', tagger=False, parser=False, matcher=False)

# Create a new document: doc
doc = nlp(article)

# Print all of the found entities and their labels
for ent in doc.ents:
    print(ent.label_, ent.text)