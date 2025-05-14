import cv2
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocess the images
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

# Reshape images to include channel dimension
train_images = np.expand_dims(train_images, axis=-1)
test_images = np.expand_dims(test_images, axis=-1)

# One-hot encode the labels
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Build the model
model = Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_labels))

# Save the trained model
model.save('digit_predictor.h5')

# Load the model for prediction
model = tf.keras.models.load_model('digit_predictor.h5')

# Load and preprocess the custom image
image = cv2.imread('digit.png', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (28, 28))
image = cv2.bitwise_not(image)  # Invert colors if necessary
image = image.astype('float32') / 255
image = np.expand_dims(image, axis=0)
image = np.expand_dims(image, axis=-1)

# Predict the digit
prediction = np.argmax(model.predict(image))
print("Predicted Digit:", prediction)
