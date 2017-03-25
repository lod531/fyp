import numpy as np
from sklearn.preprocessing import OneHotEncoder

testArray = np.zeros((2, 2))

testArray[0][1] = 1

encoder = OneHotEncoder([2, 2])

encoder.fit(testArray)

print testArray

print encoder.transform(testArray).toarray()

testArray2 = np.zeros((2, 2))

testArray2[1][1] = 1

encoder.fit(testArray2)

print encoder.transform(testArray2).toarray()

print np.zeros((2, 2))
