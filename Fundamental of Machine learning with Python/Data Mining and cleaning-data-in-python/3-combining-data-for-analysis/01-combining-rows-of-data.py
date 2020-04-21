'''
Combining rows of data

The dataset you'll be working with here relates to NYC Uber data. The original dataset has all
the originating Uber pickup locations by time and latitude and longitude. For didactic purposes,
you'll be working with a very small portion of the actual data.

Three DataFrames have been pre-loaded: uber1, which contains data for April 2014, uber2, which
contains data for May 2014, and uber3, which contains data for June 2014. Your job in this exercise
is to concatenate these DataFrames together such that the resulting DataFrame has the data for all
three months.

Begin by exploring the structure of these three DataFrames in the IPython Shell using methods such
as .head().

INSTRUCTIONS
100XP
-Concatenate uber1, uber2, and uber3 together using pd.concat(). You'll have to pass the DataFrames
in as a list.
-Print the shape and then the head of the concatenated DataFrame, row_concat.
'''
# Concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1,uber2,uber3])

# Print the shape of row_concat
print(row_concat.shape)

# Print the head of row_concat
print(row_concat.head())
