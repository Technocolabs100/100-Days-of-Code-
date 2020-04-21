# Inspecting your model
# Now that you have built a "fake news" classifier, you'll investigate what it has learned. You can map the important vector weights back to actual words using some simple inspection techniques.

# You have your well performing tfidf Naive Bayes classifier available as nb_classifier, and the vectors as tfidf_vectorizer.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Save the class labels as class_labels by accessing the .classes_ attribute of nb_classifier.
# Extract the features using the .get_feature_names() method of tfidf_vectorizer.
# Create a zipped array of the classifier coefficients with the feature names and sort them by the coefficients. To do this, first use zip() with the arguments nb_classifier.coef_[0] and feature_names. Then, use sorted() on this.
# Print the top 20 weighted features for the first label of class_labels.
# Print the bottom 20 weighted features for the second label of class_labels.

class_labels = nb_classifier.classes_

# Extract the features: feature_names
feature_names = tfidf_vectorizer.get_feature_names()

# Zip the feature names together with the coefficient array and sort by weights: feat_with_weights
feat_with_weights = sorted(zip(nb_classifier.coef_[0], feature_names))

# Print the first class label and the top 20 feat_with_weights entries
print(class_labels[0], feat_with_weights[:20])

# Print the second class label and the bottom 20 feat_with_weights entries
print(class_labels[1], feat_with_weights[-20:])
