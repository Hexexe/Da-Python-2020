#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet = "abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words


def load_finnish():
    finnish_url = "https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename = "src/kotus-sanalista_v1.xml"
    load_from_net = False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines = []
            for line in data:
                lines.append(line.decode('utf-8'))
        doc = "".join(lines)
    else:
        with open(filename, "rb") as data:
            doc = data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))


def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines = map(lambda s: s.rstrip(), data.readlines())
    return lines


def get_features(a):
    features = np.zeros((len(a), len(alphabet)))
    for i, w in enumerate(a):
        c = Counter(w)
        for j, l in enumerate(alphabet):
            features[i, j] = c[l]
    return features


def contains_valid_chars(s):
    return alphabet_set.issuperset(s)


def get_features_and_labels():
    f = [i.lower() for i in load_finnish() if contains_valid_chars(i.lower())]
    e = [i.lower()
         for i in load_english() if contains_valid_chars(i.lower()) and i[0].islower()]
    X = np.vstack([get_features(f), get_features(e)])
    y = np.hstack([[0]*len(f), [1]*len(e)])
    return X, y


def word_classification():
    X, y = get_features_and_labels()
    return cross_val_score(MultinomialNB(), X, y, cv=model_selection.KFold(n_splits=5, shuffle=True, random_state=0))


def main():
    print("Accuracy scores are:", word_classification())


if __name__ == "__main__":
    main()
