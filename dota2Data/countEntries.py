import pickle

result = pickle.load(open("resultDictionary.dict", "rb"))

result2 = result["direHeroes"]

print len(result2)
