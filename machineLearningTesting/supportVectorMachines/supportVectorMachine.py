import numpy as np
from sklearn import svm

trainingData = np.load('trainingDataset.npy')
testData = np.load('testDataset.npy')

trainingLabels = np.load('trainingLabels.npy')
testLabels = np.load('testLabels.npy')

scaler = StandardScaler()

scaler.fit(trainingData)


