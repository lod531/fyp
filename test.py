from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import random
import numpy as np

from sklearn.datasets import fetch_mldata
from sklearn import svm

def main():
    mnist = fetch_mldata('MNIST original')
    allData = mnist.data
    allLabels = mnist.target
    numberOfSamples = 1000
    trainingData = np.empty([numberOfSamples, 784])
    trainingLabels = np.empty([numberOfSamples])
    for i in range(0, numberOfSamples):
        j = random.randint(i, 60000)
        trainingData[i] = allData[j]
        trainingLabels[i] = allLabels[j]
    print(type(allData))
    clf = svm.SVC(decision_function_shape = 'ovo')
    print(clf)
    clf.fit(trainingData, trainingLabels)



    results = clf.predict(allData[60000:])
    correct = 0
    for i in range(0, 10000):
        if results[i] == allLabels[i+60000]:
            correct = correct + 1

    print(correct)


def splitDataset(dataset, numberOfTrainingExamples, trainingData, testingData):
    values = dataset.data
    labels = dataset.target
    print(values)
    

if __name__ == "__main__":
    main()
