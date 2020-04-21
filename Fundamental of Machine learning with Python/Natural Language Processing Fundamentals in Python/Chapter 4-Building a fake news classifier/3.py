# Inspecting the vectors
# To get a better idea of how the vectors work, you'll investigate them by converting them into pandas DataFrames.

# Here, you'll use the same data structures you created in the previous two exercises (count_train, count_vectorizer, tfidf_train, tfidf_vectorizer) as well as pandas, which is imported as pd.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Create the DataFrames count_df and tfidf_df by using pd.DataFrame() and specifying the values as the first argument and the columns (or features) as the second argument.
# The values can be accessed by using the .A attribute of, respectively, count_train and tfidf_train.
# The columns can be accessed using the .get_feature_names() methods of count_vectorizer and tfidf_vectorizer.
# Print the head of each DataFrame to investigate their structure.
# Test if the column names are the same for each DataFrame by creating a new object called difference to see the difference between the columns that count_df has from tfidf_df. Columns can be accessed using the .columns attribute of a DataFrame. Subtract the set of tfidf_df.columns from the set of count_df.columns.
# Test if the two DataFrames are equivalent by using the .equals() method on count_df with tfidf_df as the argument.

count_df = pd.DataFrame(count_train.A, columns=count_vectorizer.get_feature_names())

# Create the TfidfVectorizer DataFrame: tfidf_df
tfidf_df = pd.DataFrame(tfidf_train.A, columns=tfidf_vectorizer.get_feature_names())

# Print the head of count_df
print(count_df.head())

# Print the head of tfidf_df
print(tfidf_df.head())

# Calculate the difference in columns: difference
difference = set(count_df.columns) - set(tfidf_df.columns)
print(difference)

# Check whether the DataFrames are equal
print(count_df.equals(tfidf_df))