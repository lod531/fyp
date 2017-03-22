import numpy as np
from sklearn.neighbors import KDTree

def sameHeroCount(teamA, teamB):
    samesiesCount = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if teamA[i] == teamB[j]:
                samesiesCount = samesiesCount + 1
    for i in range(5, 10):
        for j in range(5, 10):
            if teamA[i] == teamB[j]:
                samesiesCount = samesiesCount + 1
    return samesiesCount

trainingData = np.load('trainingDataset.npy')
testData = np.load('testDataset.npy')

trainingLabels = np.load('trainingLabels.npy')
testLabels = np.load('testLabels.npy')

kdTree = KDTree(trainingData)

numberOfNeighbours = 20
indexes = kdTree.query(testData, k = numberOfNeighbours, return_distance = False)

correctCount = 0
for i in range(0, len(indexes)):
    victoryCount = 0
    threshold = 0
    for j in range(0, numberOfNeighbours):
        trainingTeam = trainingData[indexes[i][j]]
        testTeam = testData[i]
        distance = sameHeroCount(trainingTeam, testTeam)
        if distance > 0:
            if trainingLabels[indexes[i][j]] == 1:
                victoryCount = victoryCount + distance
        threshold = threshold + distance
    if victoryCount > threshold/2:
        if testLabels[i] == 1:
            correctCount = correctCount + 1
    else:
        if testLabels[i] == 0:
            correctCount = correctCount + 1

print correctCount
print len(testLabels)
print "Result accuracy:"
print float(correctCount)/len(testLabels)
