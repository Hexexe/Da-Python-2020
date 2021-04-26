#!/usr/bin/env python3
import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def yoinkFile(url, frac):
    with gzip.open(url) as f:
        d = f.readlines()
    return d[:int(frac * len(d))]


def spam_detection(random_state=0, fraction=1.0):
    ham = yoinkFile("src/ham.txt.gz", fraction)
    spam = yoinkFile("src/spam.txt.gz", fraction)
    X = CountVectorizer().fit_transform(ham + spam).toarray()
    y = np.concatenate([[0]*len(ham), [1]*len(spam)])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=random_state, train_size=.75)
    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return accuracy_score(y_test, y_pred), len(X_test), (y_test != y_pred).sum()


def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")


if __name__ == "__main__":
    main()
