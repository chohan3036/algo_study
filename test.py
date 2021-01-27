import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

sent = pd.read_csv('sent_train.tsv', delimiter='\t')
sent.head()

y = sent.Sentiment
x = sent.Phrase

tfidf = TfidfVectorizer()
x = tfidf.fit_transform(x)
x_df = pd.DataFrame(x.toarray(), columns=tfidf.get_feature_names())

#train and test plit
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3, random_state=3)

bnb = BernoulliNB()
bnb.fit(x_train, y_train)
y_pred = bnb.predict(x_test)
bnb_score = accuracy_score(y_test, y_pred)

mnb = MultinomialNB()
mnb.fit(x_train, y_train)
y_pred = mnb.predict(x_test)
mnb_score = accuracy_score(y_test, y_pred)

print(bnb_score, mnb_score)

test_data = pd.DataFrame({'Phrase': 'packed with just as much intelligence as action'}, index=[0])
test_data = tfidf.transform(test_data)
b_pred = bnb.predict(test_data)
m_pred = mnb.predict(test_data)

print(b_pred, m_pred)


