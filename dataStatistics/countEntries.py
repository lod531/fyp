import pickle
import numpy as np
from math import sqrt

dictionary = pickle.load(open("resultDictionary.dict", "rb"))

matchOutcomes = dictionary["matchOutcomes"]
matchOutcomesCopy = list(matchOutcomes)


numberOfMatchesTotal = len(matchOutcomes)
countOfRadiantWins = 0
for i in range(0, len(matchOutcomes)):
    countOfRadiantWins += matchOutcomes.pop()
    
mean = float(countOfRadiantWins)/numberOfMatchesTotal

print "The mean, 0 being a dire win and 1 being a radiant win, is:"
print mean

standardDeviation = 0

for i in range(0, len(matchOutcomesCopy)):
    standardDeviation += pow(matchOutcomesCopy[i] - mean, 2)

standardDeviation = standardDeviation/numberOfMatchesTotal

standardDeviation = sqrt(standardDeviation)

print "Standard deviation:"
print standardDeviation

standardError = (1.96 * standardDeviation)/sqrt(numberOfMatchesTotal)

print "Standard error:"
print standardError
