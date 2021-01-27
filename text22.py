import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
from wordcloud import WordCloud

nltk.download('popular')

stop_words = stopwords.words('english')
stop_words.append("'s")
stop_words.append("n\'t")
ps = PorterStemmer()

url = 'http://programminghistorian.github.io/ph-submissions/assets/basic-text-processing-in-r/sotu_text/236.txt'
text = requests.get(url).text
words = word_tokenize(text)

#불용어 처리
filter_words = [w for w in words if w.lower() not in stop_words]

#어간추출
stem_words=[]
for word in filter_words:
    stem_words.append(ps.stem(word))

#문장부호 제거
nopunc_words = [word for word in stem_words if word not in string.punctuation]
text = ''.join([char for char in text if char not in string.punctuation])

#워드 클라우드 그리기
wordcloud = WordCloud().generate(text)
fig=plt.figure(figsize=(10,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
