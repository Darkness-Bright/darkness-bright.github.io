# Hide those harmless tensorflow messages
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load data
from numpy import loadtxt

# Sequential and dense, for constructing the model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load the dataset
data = loadtxt('data.csv', delimiter=',')
rows_total = data.shape[1]
columns_total = data.shape[0]
# split into input (X) and output (y) variables
X = data[:,0:rows_total-1]
y = data[:,rows_total-1]

# Control how many epochs to train for
epochs = 333

# define the keras model
model = Sequential()
model.add(Dense(24, input_shape=(rows_total-1,), activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=epochs, batch_size=rows_total)

# Summary
dummy,accuracy = model.evaluate(X, y)
model.summary()

# Show sample of predictions
print('Showing first three predictions made:\n')
predictions = (model.predict(X) > 0.5).astype(int)
for i in range(3):
  print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

print('\nModel made, compiled and fit!\nEpochs: '+str(epochs)+'\nAccuracy: '+str(accuracy*100)+'%')
