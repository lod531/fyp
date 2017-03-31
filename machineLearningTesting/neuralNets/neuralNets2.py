import numpy as np
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV


trainingData = np.load('trainingDataset.npy')
testData = np.load('testDataset.npy')

trainingLabels = np.load('trainingLabels.npy')
testLabels = np.load('testLabels.npy')

encoder = OneHotEncoder([115, 115, 115, 115, 115,
                            115, 115, 115, 115, 115])

encoder.fit(trainingData)
trainingData = encoder.transform(trainingData).toarray()

encoder.fit(testData)
testData = encoder.transform(testData).toarray()

scaler = StandardScaler()

scaler.fit(trainingData)

trainingData = scaler.transform(trainingData)
testData = scaler.transform(testData)

hyperParameterSelector = pickle.load(open("neuralNets.cv", 'rb'))

print hyperParameterSelector.best_params_

print hyperParameterSelector.best_score_
