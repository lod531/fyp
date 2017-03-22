import numpy as np
from sklearn.neighbors import KDTree

trainingData = np.load('trainingDataset.npy')
testData = np.load('testDataset.npy')

trainingLabels = np.load('trainingLabels.npy')
testLabels = np.load('testLabels.npy')

kdTree = KDTree(trainingData)

numberOfNeighbours = 30
distances, indexes = kdTree.query(testData, k = numberOfNeighbours)


correctCount = 0
for i in range(0, len(indexes)):
    victoryCount = 0
    threshold = 0
    for j in range(0, numberOfNeighbours):
        if trainingLabels[indexes[i][j]] == 1:
            victoryCount = victoryCount + 1/distances[i][j]
        threshold = threshold + 1/distances[i][j]
    if victoryCount > threshold/2:
        if testLabels[i] == 1:
            correctCount = correctCount + 1
    else:
        if testLabels[i] == 0:
            correctCount = correctCount + 1


    



print "Result accuracy:"
print float(correctCount)/len(testLabels)
