# mport important packages
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib
import yaml

PATH_CONFIG = "../config/config.yaml"
config = yaml.safe_load(open(PATH_CONFIG))


# path to the dataset
filename = config['data_source']['directory'] + config['data_source']['filename']

print(filename)

# load data
data = pd.read_csv(filename, header=None)

# add column names
data.columns = config['data_source']['column_names']

# replace "?" with -99999
data = data.replace('?', -99999)

# drop id column
data = data.drop(config['data_source']['drop_columns'], axis=1)

# Define X (independent variables) and y (target variable)

X = data.drop(config['data_source']['target_name'], axis=1)
y = data[config['data_source']['target_name']]

# split data into train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=config['data_source']['test_size'], random_state=config['data_source']['random_state'])

# call our model and fit to our data
model = KNeighborsClassifier(n_neighbors=config['model']['n_neighbors'], weights=config['model']['weights'],
                                  algorithm=config['model']['algorithm'], leaf_size=config['model']['leaf_size'],
                                  p=config['model']['p'], metric=config['model']['metric'], n_jobs=config['model']['n_jobs'])

# training the model
model.fit(X_train, y_train)

# test our model
result = model.score(X_test, y_test)
print("Accuracy score is {:.1f} %".format(result*100))

# save our classifier in the model directory
model_name = config['model']['model_name']
joblib.dump(model, '../model/{}.pkl'.format(model_name))
print("Model saved as {}.pkl".format(model_name))
