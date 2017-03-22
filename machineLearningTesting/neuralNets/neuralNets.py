import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier


trainingData = np.load('trainingDataset.npy')
testData = np.load('testDataset.npy')

trainingLabels = np.load('trainingLabels.npy')
testLabels = np.load('testLabels.npy')

scaler = StandardScaler()

scaler.fit(trainingData)

trainingData = scaler.transform(trainingData)
testData = scaler.transform(testData)



layers = (300, 100)
mlp = MLPClassifier(hidden_layer_sizes=layers)
print layers

mlp.fit(trainingData, trainingLabels)

print mlp.score(testData, testLabels)
