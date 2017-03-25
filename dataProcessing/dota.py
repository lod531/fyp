import dota2api
import time
import pickle
import csv

def getLeastRecentMatchID(listOfMatches):
    leastRecentMatch = listOfMatches.pop()
    listOfMatches.append(leastRecentMatch)
    return leastRecentMatch["match_id"]

def printMatchIDs(listOfMatches):
    for match in listOfMatches:
        print match["match_id"]

api = dota2api.Initialise("6E87FE70D7AB385951B051E0852127B6")

handle = open("resultDictionary.dict", "r+b")
handle1 = open("resultDictionary1.dict", "rb")
handle3 = open("combinedDictionary.dict", "wb")

result = pickle.load(handle)
result1 = pickle.load(handle1)

radiantHeroes = result["radiantHeroes"]
direHeroes = result["direHeroes"]
matchOutcomes = result["matchOutcomes"]

radiantHeroes1 = result1["radiantHeroes"]
direHeroes1 = result1["direHeroes"]
matchOutcomes1 = result1["matchOutcomes"]

for i in range(0, len(radiantHeroes1)):
    print i
    found = False
    j = 0
    while((j < len(radiantHeroes)) & (not found)):
        found = (radiantHeroes[j] == radiantHeroes1[i]) & \
                (direHeroes[j] == direHeroes1[i]) 
        j = j + 1
    if not found:
        radiantHeroes.append(radiantHeroes1[i])
        direHeroes.append(direHeroes1[i])
        matchOutcomes.append(matchOutcomes1[i])

print len(radiantHeroes)

newResultDictionary = {"radiantHeroes": radiantHeroes,
                        "direHeroes": direHeroes,
                        "matchOutcomes": matchOutcomes}

pickle.dump(newResultDictionary, handle3)
