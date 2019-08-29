# farsinlp-exp

### Introduction

This is code I wrote as part of a relatively independent research project while at CMU.

It tests a hypothesis that adding semantic information in the form of word clusters to the Farsi training set for the CMU-developed TurboParser would improve its performance on sentences with noun phrases. Using cluster sizes drawn from literature on word clustering and on Farsi in specific, this turns out to be false.

### Requirements

-Python
-TurboParser version 2.02. Fair warning: this may be difficult to install.
-Dadegan Dependency Treebank.
-Brown Word Clustering algorithm, found at https://github.com/percyliang/brown-cluster

### Setup and Running

Have this project in the same directory as the TurboParser and the Word Clustering.
python emptyconll.py.
python conll-to-text.py.

To run, ./create-cluster-corpus.sh n, where n is the number of clusters you want.

To test, run python testing.py.
