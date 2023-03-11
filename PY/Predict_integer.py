# Hide those harmless tensorflow messages
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load data
from numpy import loadtxt

# Sequential and dense, for constructing the model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load the dataset
dataset = loadtxt('data.csv', delimiter=',')
rows_total = 11

# split into input (X) and output (y) variables
X = dataset[:,0:rows_total-1]
y = dataset[:,rows_total-1]

# define the keras model
model = Sequential()
model.add(Dense(24, input_shape=(rows_total-1,), activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=30, batch_size=rows_total-1)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*rows_total-10))

# make probability predictions with the model
predictions = model.predict(X)
rounded = [round(x[0]) for x in predictions]
