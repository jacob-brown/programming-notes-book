# Basic Text Classification

**Aim**: Classify IMDB comments as positive or negative (i.e. sentiment)

We'll train a binary classifier to perform sentiment analysis on an IMDB dataset.

Hence binary, either positive or negative.

**Dataset**: 50,000 movie reviews. 25,000 reviews for training and 25,000 reviews for testing 

The data is *balanced* as it has equal number training and testing. 


import matplotlib.pyplot as plt
import os
import re
import shutil
import string
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import preprocessing
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization

Download the data - (run once! jupyter cell converted to raw)

url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

dataset = tf.keras.utils.get_file("data/aclImdb_v1.tar.gz", url,
                                    untar=True, cache_dir='.',
                                    cache_subdir='')


general cleanup: move the folder to data - (run once! jupyter cell converted to raw)

shutil.move('aclImdb','data/aclImdb')

Create a path to the data 

dataset_dir = os.path.join("./data/", 'aclImdb')

print(dataset_dir)

os.listdir(dataset_dir)

train_dir = os.path.join(dataset_dir, 'train')
os.listdir(train_dir)

`pos` and `neg` directories contain many reviews in text files

sample_file = os.path.join(train_dir, 'pos/1181_9.txt')

with open(sample_file) as f:
    print(f.read())

## Load the data

1. Reformat the directory structure (`text_dataset_from_directory` will be used)
2. Create a labeled `tf.data.Dataset`


`tf.data` is:
* iterable 
* can pass directly into `model.fit`



N.B. `text_dataset_from_directory` needs the following data sctructure:

main_directory/
...class_a/
......a_text_1.txt
......a_text_2.txt
...class_b/
......b_text_1.txt
......b_text_2.txt

eg. 

`class_a` will be `neg`  

`class_b` will be `pos` 

### 1. Reformat the directory structure

# run once
remove_dir = os.path.join(train_dir, 'unsup')
shutil.rmtree(remove_dir)

os.listdir(train_dir)

### 2. Create a labeled `tf.data.Dataset`

"When running a machine learning experiment, it is a best practice to divide your dataset into three splits: train, validation, and test."

The currect dataset lacks a validation dataset, we should create one.

Splitting 80:20 training:validation

We set a *seed* so as the data is split without overlapping

*batch size* is the number of training examples in one forward/backward pass. The higher the batch size, the more memory space you'll need.
   
batch size defalut = 32


seed=42

# training
print("training")

raw_train_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'data/aclImdb/train',
    validation_split=0.2,
    subset='training',
    seed=seed
)

# validation
print("\nvalidating")

raw_val_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'data/aclImdb/train',
    validation_split=0.2,
    subset='validation',
    seed=seed
)

# testing
print("\ntesting")

raw_test_ds = tf.keras.preprocessing.text_dataset_from_directory('data/aclImdb/test')


### Investigate the data

Note how the reviews contain html

print("label 0: ", raw_train_ds.class_names[0])
print("label 1: ", raw_train_ds.class_names[1])

for text, label in raw_train_ds.take(1):
    for i in range(3):
        print("review: ", text.numpy()[i])
        print("label: ", label.numpy()[i])
        print("\n")

### Prepare the data
* remove html
* remove punctuation
* vectorize text

*Tokenization* - split string into tokens, eg. sentance to words 

*Vectorization* - converting tokens to numbers, allows them to be fed into the neural network

We will use `preprocessing.TextVectorization`, this will remove punctuation but not html


# convert to lowercase and remove html

def custom_standardization(input_data):
  lowercase = tf.strings.lower(input_data)
  stripped_html = tf.strings.regex_replace(lowercase, '<br />', ' ')
  return tf.strings.regex_replace(stripped_html,
                                  '[%s]' % re.escape(string.punctuation),
                                  '')


create the *vecorization* layer (standardize, tokenize, and vectorize)

it will use the `custom_standardization` and will output an `int` (vectorization)

max_features = 10000
sequence_length = 250

vectorize_layer = TextVectorization(
    standardize = custom_standardization,
    max_tokens = max_features,
    output_mode = 'int',
    output_sequence_length=sequence_length
)

next we fit the state of the preprocessing layer to the dataset, using `adapt` 

# first remove the labels (i.e. text only dataset)
train_text = raw_train_ds.map(lambda x, y : x)

# then call adapt
vectorize_layer.adapt(train_text)


defien a vectorization function

def vectorize_text(text, label):
  text = tf.expand_dims(text, -1)
  return vectorize_layer(text), label

**investigate the data**

print('1287: ', vectorize_layer.get_vocabulary()[1287])
print('length: ', len(vectorize_layer.get_vocabulary()))

# retrieve a batch (of 32 reviews and labels) from the dataset
text_batch, label_batch = next(iter(raw_train_ds))
first_review, first_label = text_batch[0], label_batch[0]
print("Review", first_review)
print("Label", raw_train_ds.class_names[first_label])
print("Vectorized review", vectorize_text(first_review, first_label))

### Map the vectorization layer to the datasets


train_ds = raw_train_ds.map(vectorize_text)
val_ds = raw_val_ds.map(vectorize_text)
test_ds = raw_test_ds.map(vectorize_text)

### Configure the dataset for performance

2 methods used when loading data, to make sure the I/O does not becoming blocking

`cache()` - cache the data in memory, we can also store on disk if very large

`prefetch()` - overlaps preprocessing and model execution when training

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)

## Create the model

Layers:
1. `Embedding` - takes ints and looks up embedding vector for each word-index. Vectors are learned during training
2. `GlobalAveragePooling1D` - "returns a fixed-length output vector for each example by averaging over the sequence dimension"
3. `Dense` - hidden, fully connected layer with $n$ hidden units
4. Single output node, densly connected



`Dropout` helps prevent overfitting

N.B. embedding is the process of taking high-dimensional vectors and passing them into a (simpler) low-dimensional space.

embedding_dim = 16

model= tf.keras.Sequential([
    layers.Embedding(max_features + 1, embedding_dim),
    layers.Dropout(0.2),
    layers.GlobalAveragePooling1D(),
    layers.Dropout(0.2),
    layers.Dense(1)
])

model.summary()

## Loss function and optimiser

Binary and model outputs probability, we will use `losses.BinaryCrossentropy`.



model.compile(
    loss=losses.BinaryCrossentropy(from_logits=True),
    optimizer = 'adam',
    metrics=tf.metrics.BinaryAccuracy(threshold=0.0)
)

## Train the model

epochs = 10

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
)

## Evaluate the model

model.evaluate(test_ds)

our accuracy is about 87% with this approach (a quick and dirty fix)

## Accuracy and loss over time
How well did the training go? 

We can plot *accuracy* and *loss* for the training and the validation.

`model.fit()` returns `history`, a dict of the training.history



**Training loss** is the error on the training set of data. 

**Validation loss** is the error after running the validation set of data through the trained network


history_dict = history.history
history_dict.keys()


acc = history_dict['binary_accuracy']
val_acc = history_dict['val_binary_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

epochs = range(1, len(acc) + 1)


def plotVal():
    plt.plot(epochs, loss, 'bo', label='Training loss')
    # b is for "solid blue line"
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

def plotAcc():
    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend(loc='lower right')


plt.figure(figsize=(12,6))
plt.subplot(1, 2, 1)
plotVal()
plt.subplot(1,2,2)
plotAcc()
plt.show()


**training**: loss decrease, and accuracy increase - what we want and expect

**validation**: loss and accuracy plateau before the training - not really what we want

From this the validation dataset (i.e. "new data") underperforms, due to *overfitting*. The model performs far better on the training dataset than it does on the new data.

## Export the model

We may want to include the `TextVectorization` layer in our model before feeding it more data. 

We can create a new model by using the existing trained one. 

export_model = tf.keras.Sequential([
    vectorize_layer,
    model,
    layers.Activation('sigmoid')
])

export_model.compile(
    loss=losses.BinaryCrossentropy(from_logits=False),
    optimizer = 'adam',
    metrics= ['accuracy']
)

# test with raw strings

examples = [
    "What a great film!",
    "load of crap",
    "best film of the year :)",
    "rubbish film, not worth your time"
]

export_model.predict(examples)


print("label 0: ", raw_train_ds.class_names[0])
print("label 1: ", raw_train_ds.class_names[1])