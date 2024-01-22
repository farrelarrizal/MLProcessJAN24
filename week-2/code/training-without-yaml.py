# import important packages
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

# path to the dataset
filename = "../data/breast-cancer-wisconsin.data"

# load data
data = pd.read_csv(filename, header=None)

# add column names
data.columns = ['id', 'clump_thickness', 'uniform_cell_size', 'uniform_cell_shape', 'marginal_adhesion', 'single_epithelial_size', 'bare_nuclei', 'bland_chromatin', 'normal_nucleoli', 'mitoses', 'class']

# replace "?" with -99999
data = data.replace('?', -99999)

# drop id column
data = data.drop(['id'], axis=1)

# Define X (independent variables) and y (target variable)

X = data.drop(['class'], axis=1)
y = data['class']

# split data into train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# call our model and fit to our data
model = KNeighborsClassifier(n_neighbors=5, weights="uniform",
                                  algorithm="auto", leaf_size=25,
                                  p=1, metric="minkowski", n_jobs=-1)

# training the model
model.fit(X_train, y_train)

# test our model
result = model.score(X_test, y_test)
print("Accuracy score is {:.1f} %".format(result*100))

# save our classifier in the model directory
model_name = "KNN_classifier"
joblib.dump(model, '../model/{}.pkl'.format(model_name))
print("Model saved as {}.pkl".format(model_name))
