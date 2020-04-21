# French NER with polyglot II
# Here, you'll complete the work you began in the previous exercise.

# Your task is to use a list comprehension to create a list of tuples, in which the first element is the entity tag, and the second element is the full string of the entity text.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Use a list comprehension to create a list of tuples called entities.
# The output expression of your list comprehension should be a tuple. Remember to use () to create the tuple.
# The first element of each tuple is the entity tag, which you can access using its .tag attribute.
# The second element is the full string of the entity text, which you can access using ' '.join(ent).
# Your iterator variable should be ent, and you should iterate over all of the entities of the polyglot Text object, txt.
# Print entities to see what you've created.

# Create the list of tuples: entities
entities = [(ent.tag, ' '.join(ent)) for ent in txt.entities]

# Print the entities
print(entities)

