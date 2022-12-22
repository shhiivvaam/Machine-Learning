# -*- coding: utf-8 -*-
"""Logistic Regression Sigmoid.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19UUrCbh_vGD5-zUP8OQ1ShukVVfgX38V
"""

from sklearn import datasets
dir(datasets)

from sklearn.datasets import load_iris
df=load_iris(as_frame=False)      # Returns a dictionary
print(df)

print(list(df.keys()))

print(df['frame'])

print(df['data'].shape)

X=df['data'][:,3:]                                            #Difference between [3:] and [3].reshape(-1,1)
print(X)
print(X.shape)

y=df['target']
print(y)
print(y.shape)

y=df['target']==2
print(y)
print(y.shape)

import numpy as np
y=(df['target']==2).astype(np.int)
print(y)
print(y.shape)

from sklearn.linear_model import LogisticRegression 
model=LogisticRegression()
model.fit(X,y)
tt=model.predict([[2.5]])
print(tt)

import numpy as np
xnew=np.linspace(0,3,1000).reshape(-1,1)
y_prob=model.predict_proba(xnew)
print(xnew) 
print('--------------------')
print(y_prob)

import matplotlib.pyplot as plt 
plt.plot(xnew,y_prob[:,1])

Xnew1=df['data'][:,3:] 
print(Xnew1)

y_prob1=model.predict_proba(Xnew1)
print(y_prob1)

plt.plot(Xnew1,y_prob1[:,1])