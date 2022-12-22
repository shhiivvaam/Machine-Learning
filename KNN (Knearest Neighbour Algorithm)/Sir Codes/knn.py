# -*- coding: utf-8 -*-
"""KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ERJXqgRmtUFitHt_EVChFr7hVeNc6pCq

# **KNN on IRIS Dataset** using CSV file
"""

import pandas as pd
df=pd.read_csv('/content/IRIS.csv')
print(df)

X=df.drop('species',axis='columns')
y=df['species']
print(X)
print('------------------------------------------------')
print(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=9)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

model.predict(X_test)

print(model.score(X_test,y_test))

df1=df[:50]
df2=df[50:100]
df3=df[100:]
import matplotlib.pyplot as plt
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.scatter(df1['sepal_length'],df1['sepal_width'],color='red',marker='+')
plt.scatter(df2['sepal_length'],df2['sepal_width'],color='cyan',marker='D')
plt.scatter(df3['sepal_length'],df3['sepal_width'],color='blue',marker='<')
plt.legend(['setosa','versicolor','virginica'])
plt.show()

"""# **KNN on IRIS Dataset** using sklearn dataset"""

import pandas as pd
from sklearn.datasets import load_iris
d=load_iris()
df=pd.DataFrame(d['data'],columns=d['feature_names'])
df['target']=d['target']
print(df)

X=df.drop('target',axis='columns')
y=df['target']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=9)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)
model.predict(X_test)
print(model.score(X_test,y_test))

"""# **KNN on Digits Dataset(MNIST)** using CSV file



"""

df1=pd.read_csv('/content/mnist.csv',on_bad_lines='skip')
df1.dropna(inplace=True)

X=df1.drop('label',axis='columns')
y=df1['label']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=9)

model=KNeighborsClassifier(n_neighbors=3)

model.fit(X_train,y_train)

model.predict(X_test)

print(model.score(X_test,y_test))

"""# **KNN on Digits Dataset**  using sklearn Dataset"""

from sklearn.datasets import load_digits
d=load_digits()
df2=pd.DataFrame(d['data'],columns=d['feature_names'])

df2

print(list(d.keys()))

df2['target']=d['target']
X=df2.drop('target',axis='columns')
y=df2['target']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=9)
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

model.predict(X_test)

print(model.score(X_test,y_test))

"""# **Extra**"""

#X=[[1,2,3,4,5,6,7,8,9,10]]
X=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
y=[1,4,9,16,25,36,49,64,81,100]
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X,y)

print(model.predict([[11]]))

print(model.score(X,y))