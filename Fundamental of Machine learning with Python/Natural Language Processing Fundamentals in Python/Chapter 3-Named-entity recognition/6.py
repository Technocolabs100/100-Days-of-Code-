# Exercise
# Exercise
# Spanish NER with polyglot
# You'll continue your exploration of polyglot now with some Spanish annotation. This article is not written by a newspaper, so it is your first example of a more blog-like text. How do you think that might compare when finding entities?

# The Text object has been created as txt, and each entity has been printed, as you can see in the IPython Shell.

# Your specific task is to determine how many of the entities contain the words "Márquez" or "Gabo" - these refer to the same person in different ways!

# Instructions
# 100 XP
# Instructions
# 100 XP
# Iterate over all of the entities of txt, using ent as your iterator variable.
# Check whether the entity contains "Márquez" or "Gabo". If it does, increment count.
# Hit 'Submit Answer' to see what percentage of entities refer to Gabriel García Márquez (aka Gabo).

count = 0

# Iterate over all the entities
for ent in txt.entities:
    # Check whether the entity contains 'Márquez' or 'Gabo'
    if "Márquez" in ent or "Gabo" in ent:
        # Increment count
        count += 1

# Print count
print(count)

# Calculate the percentage of entities that refer to "Gabo": percentage
percentage = count * 1.0 / len(txt.entities)
print(percentage)
