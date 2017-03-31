import numpy as np
import pickle
from sklearn.neighbors import BallTree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

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

svm = SVC(C=4, gamma=0.015625)

svm.fit(trainingData, trainingLabels)

print svm.score(testData, testLabels)
