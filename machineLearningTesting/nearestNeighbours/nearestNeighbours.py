import numpy as np
import utilities as ut
from sklearn.neighbors import KDTree

trainingData = np.load('trainingDataset.npy')
testData = np.load('testDataset.npy')

trainingLabels = np.load('trainingLabels.npy')
testLabels = np.load('testLabels.npy')

kdTree = KDTree(trainingData)

indices = kdTree.query(testData, return_distance = False)

correctCount = 0
for i in range(0, len(testLabels)):
    if testLabels[i] == trainingLabels[indices[i][0]]:
        correctCount = correctCount + 1

print "Result accuracy:"
print float(correctCount)/len(testLabels)
