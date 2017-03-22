import numpy as np


trainingData = np.load('trainingDataset.npy')
testData = np.load('testDataset.npy')

trainingLabels = np.load('trainingLabels.npy')
testLabels = np.load('testLabels.npy')


victoryCount= 0
for i in range(0, len(testLabels)):
    if testLabels[i] == 1:
        victoryCount += 1

print victoryCount 
print len(testLabels)
print "Result accuracy:"
print float(victoryCount)/len(testLabels)
