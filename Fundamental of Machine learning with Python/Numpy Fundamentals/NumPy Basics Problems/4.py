# Lightweight baseball players
# To subset both regular Python lists and numpy arrays, you can use square brackets:

# x = [4 , 9 , 6, 3, 1]
# x[1]
# import numpy as np
# y = np.array(x)
# y[1]
# For numpy specifically, you can also use boolean numpy arrays:

# high = y > 5
# y[high]
# The code that calculates the BMI of all baseball players is already included. Follow the instructions and reveal interesting things from the data!

# Instructions
# 100 XP
# Instructions
# 100 XP
# Create a boolean numpy array: the element of the array should be True if the corresponding baseball player's BMI is below 21. You can use the < operator for this. Name the array light.
# Print the array light.
# Print out a numpy array with the BMIs of all baseball players whose BMI is below 21. Use light inside square brackets to do a selection on the bmi array.
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])