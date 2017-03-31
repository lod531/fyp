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

cParameters = []
for i in range(-5, 16):
    cParameters.append(pow(2, i))

gammaParameters = []
for i in range(-15, 3):
    gammaParameters.append(pow(2, i))

parameterGrid = [{'C': cParameters, 'gamma': gammaParameters, 'kernel': ['rbf']}]

hyperParameterSelector = GridSearchCV(SVC(C=1), param_grid = parameterGrid, n_jobs = -1)

hyperParameterSelector.fit(trainingData, trainingLabels)

print hyperParameterSelector.best_params_

with open("gridSearch.cv", 'wb') as theFile:
    pickle.dump(hyperParameterSelector, theFile)
