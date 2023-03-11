# Install all needed modules with:
# pip3 install numpy tensorflow keras matplotlib scipy
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import numpy as np
import matplotlib.pyplot as plt

PATH = 'cats_and_dogs'

train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')
test_dir = os.path.join(PATH, 'test')

# Get number of files in each directory. The train and validation directories
# each have the subdirecories "dogs" and "cats".
total_train = sum([len(files) for r, d, files in os.walk(train_dir)])
total_val = sum([len(files) for r, d, files in os.walk(validation_dir)])
total_test = len(os.listdir(test_dir))

# Variables for pre-processing and training.
batch_size = 128
epochs = 15
IMG_HEIGHT = 150
IMG_WIDTH = 150

# https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator#flow_from_directory

'''Create image generators for each of the three image data sets (train, validation, test). 
Use ImageDataGenerator to read / decode the images and convert them into floating point tensors. 
Use the rescale argument (and no other arguments for now) to rescale the tensors from values between 0 and 255 to values between 0 and 1.'''
train_image_generator = ImageDataGenerator(rescale=1./255)
validation_image_generator = ImageDataGenerator(rescale=1./255)
test_image_generator = ImageDataGenerator(rescale=1./255)


'''For the *_data_gen variables, use the flow_from_directory method. Pass in the batch size, directory, target size ((IMG_HEIGHT, IMG_WIDTH)), 
class mode, and anything else required. test_data_gen will be the trickiest one. For test_data_gen, make sure to pass in shuffle=False to the 
flow_from_directory method. This will make sure the final predictions stay is in the order that our test expects. 
For test_data_gen it will also be helpful to observe the directory structure.'''
train_data_gen = train_image_generator.flow_from_directory(directory=train_dir, batch_size=128, 
                                                           target_size=(IMG_HEIGHT, IMG_WIDTH), shuffle=True, class_mode='binary')
val_data_gen = test_image_generator.flow_from_directory(directory=validation_dir, batch_size=128,target_size=(IMG_HEIGHT, IMG_WIDTH), shuffle=True, class_mode='binary')

test_data_gen = test_image_generator.flow_from_directory(directory=PATH, classes=['test'], target_size=(IMG_HEIGHT, IMG_WIDTH), shuffle=False, class_mode=None, batch_size=batch_size) 

def plotImages(images_arr, probabilities = False):
    fig, axes = plt.subplots(len(images_arr), 1, figsize=(5,len(images_arr) * 3))
    if probabilities is False:
      for img, ax in zip( images_arr, axes):
          ax.imshow(img)
          ax.axis('off')
    else:
      for img, probability, ax in zip( images_arr, probabilities, axes):
          ax.imshow(img)
          ax.axis('off')
          if probability > 0.5:
              ax.set_title("%.2f" % (probability*100) + "% dog")
          else:
              ax.set_title("%.2f" % ((1-probability)*100) + "% cat")
    plt.show()


train_image_generator = ImageDataGenerator(rotation_range=45, width_shift_range=0.2, height_shift_range=0.2, horizontal_flip=True, zoom_range=0.2, shear_range=0.2, rescale=1./255)

train_data_gen = train_image_generator.flow_from_directory(batch_size=batch_size,directory=train_dir,target_size=(IMG_HEIGHT, IMG_WIDTH),class_mode='binary')

augmented_images = [train_data_gen[0][0][0] for i in range(5)]

plotImages(augmented_images)

model = Sequential()

model.add(Conv2D(32, (3,3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(32, (3,3), activation='relu'))
model.add(MaxPooling2D((2,2)))
model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dense(2, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

history = model.fit(train_data_gen, steps_per_epoch=15, epochs=epochs, validation_data=val_data_gen,validation_steps=8)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

pred_class = model.predict(test_data_gen, verbose=1)

predicted_class = np.argmax(model.predict(test_data_gen), axis=-1)
print('Predicted results: ', predicted_class)

probabilities = predicted_class.tolist()

actual_probabilities = [np.max(vector) for vector in probabilities]

final_images = [test_data_gen[0][0][0] for i in range(50)]
plotImages(final_images,actual_probabilities)

answers =  [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0,
            1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0,
            1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 
            0, 0, 0, 0, 0, 0]

correct = 0
for probability, answer in zip(probabilities, answers):
  if round(probability) == answer:
    correct +=1

print('Number of correct prediction:', correct,'/',len(answers))
print('Accuracy:', correct/len(answers))

