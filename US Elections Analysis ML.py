import pandas as pd
from pandas import Series, DataFrame
import re
import matplotlib.pyplot as plt
import matplotlib as mlp
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.svm import SVC

tfidf = TfidfVectorizer(max_features=10000, ngram_range=(1,2))
df = pd.read_csv('trumptweets.csv')
#print(df.shape)
df.drop(['id', 'link', 'date', 'retweets', 'favorites', 'mentions', 'hashtags','geo'], axis=1, inplace=True)
df['sentiment'] = np.random.randint(2, size=(41122))
#print(df.shape)
#print(df.tail)

x = df['content']
x = tfidf.fit_transform(x)
y = df['sentiment']
#print(x.shape)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2, random_state= 0)
#print(x_train.shape)
#print(x_test.shape)

#clf = LinearSVC()
#clf.fit(x_train, y_train)

#y_pred = clf.predict(x_test)
#print(classification_report(y_test, y_pred))

clf2 = SVC()
clf2.fit(x_train, y_train)

print('Accuracy on testing data is', clf2.score(x_test, y_test))
print('Accuracy on training data is', clf2.score(x_train, y_train))

#kernal=['linear', 'rbf', 'poly', 'sigmoid']
#for i in kernal:
#	clf2=SVC(kernal=1,C=1.0)
#	clf2.fit(x_train, y_train)
#	print('For kernal:',i)
#	print('Accuracy is :',clf2.score(x_test,y_test))