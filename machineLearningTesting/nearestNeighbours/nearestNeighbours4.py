import numpy as np
import utilities as ut
from sklearn.neighbors import KDTree


trainingData = np.load('trainingDataset.npy')
testData = np.load('testDataset.npy')

trainingLabels = np.load('trainingLabels.npy')
testLabels = np.load('testLabels.npy')

kdTree = KDTree(trainingData)

numberOfNeighbours = 20
indexes = kdTree.query(testData, k = numberOfNeighbours, return_distance = False)

mirroredTestData = ut.flipTeams(np.copy(testData))
mirroredIndexes = kdTree.query(mirroredTestData, k = numberOfNeighbours, return_distance = False)

correctCount = 0
for i in range(0, len(indexes)):
    victoryCount = 0
    mirroredVictoryCount = 0
    threshold = 0
    mirroredThreshold = 0
    for j in range(0, numberOfNeighbours):
        trainingTeam = trainingData[indexes[i][j]]
        testTeam = testData[i]
        nearness = ut.sameHeroCount(trainingTeam, testTeam)
        if trainingLabels[indexes[i][j]] == 1:
            victoryCount = victoryCount + nearness 
        threshold = threshold + nearness 


    for j in range(0, numberOfNeighbours):
        trainingTeam = trainingData[mirroredIndexes[i][j]]
        testTeam = mirroredTestData[i]
        nearness = ut.sameHeroCount(trainingTeam, testTeam)
        if trainingLabels[indexes[i][j]] == 0:
            mirroredVictoryCount += nearness 
        mirroredThreshold += nearness 





    if mirroredVictoryCount < victoryCount:
        if victoryCount > threshold/2:
            if testLabels[i] == 1:
                correctCount = correctCount + 1
        else:
            if testLabels[i] == 0:
                correctCount = correctCount + 1
    else:
        if mirroredVictoryCount > mirroredThreshold/2:
            if testLabels[i] == 1:
                correctCount = correctCount + 1
        else:
            if testLabels[i] == 0:
                correctCount = correctCount + 1
       

print "Result accuracy:"
print float(correctCount)/len(testLabels)
