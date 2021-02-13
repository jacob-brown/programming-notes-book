# The Basics

Basic tutorial using the tf.keras API to build and train models. 


**Aim of project**: Build and train a model that can recognise clothing

**Dataset**: "Fashion MNIST" is 70,000 grayscale images in 10 categories. 60,000 to train and 10,000 to evaluate.


Fashion MNIST and MNIST are good at checking if the model works before deploying on the actual data.

# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import sys # python version only, not needed for tf

print(tf.__version__)
print(sys.version)

## Import and load the data
* data is loaded into numpy arrays
* comprises of training and test data
* images are 28x28 NumPy arrays, with pixel values ranging from 0 to 255
* Labels correspond to:
    0. T-shirt/top
    1. Trouser
    2. Pullover
    3. Dress
    4. Coat
    5. Sandal
    6. Shirt
    7. Sneaker
    8. Bag
    9. Ankle boot

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


explore the data

print(train_images.shape)
print(test_images.shape)
print(len(train_images))
print(len(test_images))

## Preprocess the data
currently pixel data is 0-255, we need to convert it to 0-1

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

train_images = train_images/255
test_images = test_images/255

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

Prior to training, check that the images and labels are correctly ordered.

plt.figure(figsize = (10, 10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])

plt.show()

## Build the model
First configure the layers, then compile the model

*Layers* extract representations from data fed into them

Deep learning consists of several layers

We will use 3:
1. No learning, reshape to a one dimensional array
2. Fully connected dense neural layer (with 128 nodes)
3. Fully connected dense neural layer (with 10 nodes) - returns logits array with length of 10
    * Each node will contain a score that indicates that the image belongs to a particular class


    
logits - "The vector of raw (non-normalized) predictions that a classification model generates, which is ordinarily then passed to a normalization function."

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

## Compile the model
Add additional features to the model during compiling:

* *Loss function* - Measures how accurate the model is during training, aim is to minimise these
* *Optimiser* - How the model is updated, based on the data and the loss function
* *Metrics* - Used to mnitor training and testing steps. eg. accuracy is an example of a metrics



model.compile(optimizer = 'adam',
             loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
             metrics=['accuracy'])

## Training the model
Steps of training:

1. Feed the model the **training data** (images and labels)
2. The model learns to associate images and labels
3. Ask the model to make predictions on the **test data**
4. Verify the models predictions with the **test data** labels

### Feed the model
**epochs** roughly means how many times you go through your training set. 


Note how the accuracy gradually increases.

model.fit(train_images, train_labels, epochs=10)

### Evaluate the accuracy
How accurate is the model at evaluating the **test data**


test_loss, test_acc = model.evaluate(test_images, test_labels, verbose = 2)


An accuracy of 0.88 is quite alot less than 0.91 in terms of ML.

*Obverfitting* is occuring. The model "memorises" the noise of the training data, negatively effecting its performance on new data

We will come back to this at a later stage. 

### Make predictions

Logits are the raw model outputs, first we must normalise them.  

We will attach a *softmax layer*, which converts them to probabilities


probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)

For each image in the test set, the model has predicted the probability that the image belongs to 1 of the 10 classes of clothing. 

Each value represents the *models confidence*

predictions[0]

highest_value = np.argmax(predictions[0])
print(highest_value)
print(class_names[highest_value])

### Verify predictions

Define plotting functions. 
* blue indicates correctly identified
* red failures
* converts prediction to a percentage

`plot_image` - plot the image, prediction, and if correct (red/blue)
`plot_value_array` - plot barchat of array prediction scores, and if correct (red/blue)

def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')


i = 0 

plt.figure(figsize=(6,3))
plt.subplot(1, 2, 1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()


i = 12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()


The model can be wrong, even when very confident

# Plot the first X test images, their predicted labels, and the true labels.
# Color correct predictions in blue and incorrect predictions in red.
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()


### Using the trained model 
We can now use the trained model to evaluate a single instant (i.e. image) 

usually keras is used for batch processing, so we still need to add the single image to a list

test_image_index = 10

img = test_images[test_image_index]
img = np.expand_dims(img, 0)

img.shape

predict the correct label

predictions_single = probability_model.predict(img)
predictions_single

i = test_image_index
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()