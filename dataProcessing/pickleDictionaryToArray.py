import numpy as np
import pickle

resultDictionary = pickle.load(open("resultDictionary.dict", "rb"))

#these are all lists.
#direHeroes is a list of lists, each list containing
#5 heroes. Same for radiantHeroes. 
#MatchOutcomes is a list of values
direHeroes = resultDictionary["direHeroes"]
radiantHeroes = resultDictionary["radiantHeroes"]
matchOutcomes = resultDictionary["matchOutcomes"]

#two thirds of the matches go to training, one third to testing
numberOfTargetMatches = len(matchOutcomes)/4 * 3
numberOfTestMatches = len(matchOutcomes) - numberOfTargetMatches
#reason for magic number 11 there is 5 heroes per team plus the
#match outcome = 5+5+1 = 11
trainingArray= np.zeros((numberOfTargetMatches, 10))
testArray = np.zeros((numberOfTestMatches, 10))
trainingLabels = np.zeros(numberOfTargetMatches)
testLabels = np.zeros(numberOfTestMatches )

for i in range(0, numberOfTargetMatches):
    currentDireHeroes = direHeroes.pop()
    currentRadiantHeroes = radiantHeroes.pop()
    #5 for number of heroes
    for j in range(0, 5):
        trainingArray[i, j] = currentDireHeroes.pop()
    for j in range(5, 10):
        trainingArray[i, j] = currentRadiantHeroes.pop()
    trainingLabels[i] = matchOutcomes.pop()


for i in range(0, numberOfTestMatches):
    currentDireHeroes = direHeroes.pop()
    currentRadiantHeroes = radiantHeroes.pop()
    #5 for number of heroes
    for j in range(0, 5):
        testArray[i, j] = currentDireHeroes.pop()
    for j in range(5, 10):
        testArray[i, j] = currentRadiantHeroes.pop()
    testLabels[i] = matchOutcomes.pop()



with open("trainingDataset.npy", "wb") as theFile:
    np.save(theFile, trainingArray)

with open("testDataset.npy", "wb") as theFile:
    np.save(theFile, testArray)

with open("testLabels.npy", "wb") as theFile:
    np.save(theFile, testLabels)

with open("trainingLabels.npy", "wb") as theFile:
    np.save(theFile, trainingLabels)
