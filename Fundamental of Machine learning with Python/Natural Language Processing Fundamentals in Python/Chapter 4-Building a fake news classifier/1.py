# CountVectorizer for text classification
# It's time to begin building your text classifier! The data has been loaded into a DataFrame called df. Explore it in the IPython Shell to investigate what columns you can use. The .head() method is particularly informative.

# In this exercise, you'll use pandas alongside scikit-learn to create a sparse text vectorizer you can use to train and test a simple supervised model. To begin, you'll set up a CountVectorizer and investigate some of its features.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Import CountVectorizer from sklearn.feature_extraction.text and train_test_split from sklearn.model_selection.
# Create a Series y to use for the labels by assigning the .label attribute of df to y.
# Using df["text"] (features) and y (labels), create training and test sets using train_test_split(). Use a test_size of 0.33 and a random_state of 53.
# Create a CountVectorizer object called count_vectorizer. Ensure you specify the keyword argument stop_words="english" so that stop words are removed.
# Fit and transform the training data X_train using the .fit_transform() method. Do the same with the test data X_test, except using the .transform() method.
# Print the first 10 features of the count_vectorizer using its .get_feature_names() method.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# Print the head of df
print(df.head())

# Create a series to store the labels: y
y = df.label

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], y, test_size=0.33, random_state=53)

# Initialize a CountVectorizer object: count_vectorizer
count_vectorizer = CountVectorizer(stop_words='english')

# Transform the training data using only the 'text' column values: count_train 
count_train = count_vectorizer.fit_transform(X_train)

# Transform the test data using only the 'text' column values: count_test 
count_test = count_vectorizer.transform(X_test)

# Print the first 10 features of the count_vectorizer
print(count_vectorizer.get_feature_names()[:10])
