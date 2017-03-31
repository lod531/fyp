import numpy as np
import utilities as ut
import pickle
from sklearn.neighbors import BallTree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import OneHotEncoder

trainingData = np.load('trainingDataset.npy')
testData = np.load('testDataset.npy')

trainingLabels = np.load('trainingLabels.npy')
testLabels = np.load('testLabels.npy')

encoder = OneHotEncoder([115, 115, 115, 115, 115,
                            115, 115, 115, 115, 115])

encoder.fit(trainingData)
trainingData = encoder.transform(trainingData).toarray()

encoder.fit(testData)
testData = encoder.transform(testData).toarray()

'''
kdTree = BallTree(trainingData)

with open("kdtree.tree", 'wb') as theFile:
    pickle.dump(kdTree, theFile)

kdTree = pickle.load(open("kdtree.tree", 'rb'))

'''

neighbors = KNeighborsClassifier(n_neighbors = 4, algorithm = 'ball_tree', weights='distance')

neighbors.fit(trainingData, trainingLabels)




for i in range(1, 11):
    print i
    neighbors.set_params(n_neighbors = i, weights='distance')
    print neighbors.score(testData, testLabels)
