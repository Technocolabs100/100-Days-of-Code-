# Training and testing the "fake news" model with CountVectorizer
# Now it's your turn to train the "fake news" model using the features you identified and extracted. In this first exercise you'll train and test a Naive Bayes model using the CountVectorizer data.

# The training and test sets have been created, and count_vectorizer, count_train, and count_test have been computed.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Import the metrics module from sklearn and MultinomialNB from sklearn.naive_bayes.
# Instantiate a MultinomialNB classifier called nb_classifier.
# Fit the classifier to the training data.
# Compute the predicted tags for the test data.
# Calculate and print the accuracy score of the classifier.
# Compute the confusion matrix. To make it easier to read, specify the keyword argument labels=['FAKE', 'REAL'].

from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

# Instantiate a Multinomial Naive Bayes classifier: nb_classifier
nb_classifier = MultinomialNB()

# Fit the classifier to the training data
nb_classifier.fit(count_train, y_train)

# Create the predicted tags: pred
pred = nb_classifier.predict(count_test)

# Calculate the accuracy score: score
score = metrics.accuracy_score(y_test, pred)
print(score)

# Calculate the confusion matrix: cm
cm = metrics.confusion_matrix(y_test, pred, labels=['FAKE', 'REAL'])
print(cm)
