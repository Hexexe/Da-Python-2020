#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    X, y = load_iris(True)
    xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size = 0.2, random_state= 0)
    return naive_bayes.GaussianNB().fit(xTrain, yTrain).score(xTest, yTest)

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
