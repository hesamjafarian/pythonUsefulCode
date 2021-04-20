# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 00:44:51 2021

@author: infoz
"""
import pandas as pd 
import numpy as np

data = pd.read_csv("converted_csv.csv", dtype='float')

#npList = np.asarray(data)

x = data.iloc[:,0:6].values
y = data.iloc[:,6].values

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(x, y, stratify=y,random_state=1)
clf = MLPClassifier(random_state=1, max_iter=1000).fit(X_train, y_train)

clf.predict_proba(X_test[:1])
clf.predict(X_test[:5, :])
clf.score(X_test, y_test)

filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)