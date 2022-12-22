# -*- coding: utf-8 -*-
"""Day2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yuI8Lew5axkkv4QLskj72gob_cmIEqpO
"""

import pandas as pd
data=pd.read_csv('/content/IRIS.csv')
data.head()



data.corr()

data.shape

data.dtypes

data.describe()

data

data.loc[148]

data.info()

df1=pd.read_csv('/content/IRISCopy.csv')
df1.info()

import matplotlib.pyplot as plt
plt.plot([i for i in range(1,6)],[j for j in range(5,10)],marker='+')
plt.show()

#plt.plot([1,2,3],[4,5,6])
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/content/IRIS.csv')

plt.plot(df.sepal_length,df.sepal_width)
plt.title('GRAPH SEPAL LENGTH vs SEPAL WIDTH')
plt.xlabel('LENGTH')
plt.ylabel('WIDTH')

plt.show()

plt.bar(df.species,df.sepal_length)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Bar chart')
plt.show()
df.describe()

plt.hist([1,1,1,1,5,4])
plt.show()

plt.hist(df.species)
plt.show()

plt.scatter(df.petal_length,df.petal_width)
plt.show()

a=[3,10,30,8]
b=['ABove 40','Between 30-40','Between 20-30','Less than 20']
c=['green','red','blue','grey']
plt.pie(a,labels=b,colors=c,startangle=0,explode=(0,0,1,0))
plt.show()

plt.boxplot(df.sepal_length)