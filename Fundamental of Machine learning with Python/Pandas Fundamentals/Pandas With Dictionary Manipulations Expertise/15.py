# Exercise
# Exercise
# loc and iloc (3)
# It's also possible to select only columns with loc and iloc. In both cases, you simply put a slice going from beginning to end in front of the comma:

# cars.loc[:, 'country']
# cars.iloc[:, 1]

# cars.loc[:, ['country','drives_right']]
# cars.iloc[:, [1, 2]]
# Instructions
# 100 XP
# Instructions
# 100 XP
# Print out the drives_right column as a Series using loc or iloc.
# Print out the drives_right column as a DataFrame using loc or iloc.
# Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap','drives_right']])
