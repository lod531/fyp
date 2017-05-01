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

currentNumberOfLayers = 10
layers = []
for i in range(0, 50):
   layers.append(currentNumberOfLayers)
   currentNumberOfLayers += 10

parameter_grid = [{'hidden_layer_sizes': layers}]

hyperParameterSelector = GridSearchCV(MLPClassifier(10), param_grid = parameter_grid, n_jobs = 1)

hyperParameterSelector.fit(trainingData, trainingLabels)

with open("neuralNets.cv", 'wb') as theFile:
    pickle.dump(hyperParameterSelector, theFile)

print hyperParameterSelector.best_params_
