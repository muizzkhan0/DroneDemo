import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from matplotlib import pyplot as plt
import cv2
import os

new_model = load_model("model.h5")
class_labels = ["No line","Sharp Left","Sharp Right","Slight Left","Slight Right","Straight"]

num = 1

while num <= 5:
    img_path = os.path.join("Test_Data", f"IMG_{num}.JPG")
    img = cv2.imread(img_path)
    resized_img = tf.image.resize(img, (256,256))
    prediction = new_model.predict(np.expand_dims(resized_img/255,0)) # expand dims cuz the model expects a batch of images
    print(f"{prediction}")

    index = np.argmax(prediction)
    print(f"Predicted Class for IMG_{num}.JPG: {class_labels[index]}")
    num += 1
    
"""
img = cv2.imread('Test_Data/IMG_6365.JPG')
resize = tf.image.resize(img, (256,256))

yhat = new_model.predict(np.expand_dims(resize/255, 0))
index = np.argmax(yhat)
print(class_labels[index])

plt.imshow(resize.numpy().astype(int))
plt.show() """