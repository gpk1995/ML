import pandas as pd
#import numpy as np

dataset = pd.read_csv('adult.csv')
X = dataset[['age','workclass','education-num','marital-status',	'occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','y']]

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X['workclass'] = labelencoder.fit_transform(X['workclass'])
X['marital-status'] = labelencoder.fit_transform(X['marital-status'])
X['occupation'] = labelencoder.fit_transform(X['occupation'])
X['relationship'] = labelencoder.fit_transform(X['relationship'])
X['race'] = labelencoder.fit_transform(X['race'])
X['sex'] = labelencoder.fit_transform(X['sex'])
X['native-country'] = labelencoder.fit_transform(X['native-country'])
X['y'] = labelencoder.fit_transform(X['y'])

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 2, init = 'k-means++',random_state= 1)
y_kmeans = kmeans.fit_predict(X)

from sklearn.metrics import confusion_matrix
confusion_matrix(X['y'], y_kmeans)
(24720+159)/(24720+7682+159)