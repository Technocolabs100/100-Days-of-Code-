# Training and testing the "fake news" model with TfidfVectorizer
# Now that you have evaluated the model using the CountVectorizer, you'll do the same using the TfidfVectorizer with a Naive Bayes model.

# The training and test sets have been created, and tfidf_vectorizer, tfidf_train, and tfidf_test have been computed. Additionally, MultinomialNB and metrics have been imported from, respectively, sklearn.naive_bayes and sklearn.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Instantiate a MultinomialNB classifier called nb_classifier.
# Fit the classifier to the training data.
# Compute the predicted tags for the test data.
# Calculate and print the accuracy score of the classifier.
# Compute the confusion matrix. As in the previous exercise, specify the keyword argument labels=['FAKE', 'REAL'] so that the resulting confusion matrix is easier to read.


nb_classifier = MultinomialNB()

# Fit the classifier to the training data
nb_classifier.fit(tfidf_train, y_train)

# Create the predicted tags: pred
pred = nb_classifier.predict(tfidf_test)

# Calculate the accuracy score: score
score = metrics.accuracy_score(y_test, pred)
print(score)

# Calculate the confusion matrix: cm
cm = metrics.confusion_matrix(y_test, pred, labels=['FAKE', 'REAL'])
print(cm)