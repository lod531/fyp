import pickle

result = pickle.load(open("resultDictionary.dict", "rb"))

result2 = result["direHeroes"]

totalLength = len(result2)

numberOfTrainingSamples = totalLength/4 * 3

numberOfTestingSamples = totalLength-numberOfTrainingSamples

print "Number of training samples:"
print numberOfTrainingSamples

print "Number of testing samples:"
print numberOfTestingSamples
