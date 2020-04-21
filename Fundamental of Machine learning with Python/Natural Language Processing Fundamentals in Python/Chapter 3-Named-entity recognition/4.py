# French NER with polyglot I
# In this exercise and the next, you'll use the polyglot library to identify French entities. The library functions slightly differently than spacy, so you'll use a few of the new things you learned in the last video to display the named entity text and category.

# You have access to the full article string in article. Additionally, the Text class of polyglot has been imported from polyglot.text.

# Instructions
# 100 XP
# Create a new Text object called txt.
# Iterate over txt.entities and print each entity, ent.
# Print the type() of ent.

# Create a new text object using Polyglot's Text class: txt
txt = Text(article)

# Print each of the entities found
for ent in txt.entities:
    print(ent)
    
# Print the type of each entity
print(type(ent))