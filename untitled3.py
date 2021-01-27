import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

sent = pd.read_csv('sent_train.tsv', delimiter='\t')
sent.set_index('PhraseId', inplace=True)
sent.head()

y = sent.Sentiment
x = sent.Phrase

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=3)

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(10,10,10), random_state=1, max_iter=500)
mlp.fit(x_train, y_train)


