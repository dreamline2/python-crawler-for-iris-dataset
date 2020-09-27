#!/usr/bin/env python
## -*- coding: utf-8 -*-
import requests
import pandas as pd
import matplotlib.pyplot as plt
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
html = requests.get(url)
fn = 'iris.csv'
with open(fn, 'wb+') as f:
    for i in html.iter_content(1024):
        data = f.write(i)

cols = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv('iris.csv', names = cols)
iris_mean = iris.groupby('species', as_index=False).mean()
iris_mean.plot(kind='bar')
plt.xticks(iris_mean.index,iris_mean['species'], rotation=0)
plt.show()