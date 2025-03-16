import tensorflow as tf
from tensorflow.keras.models import load_model
from djitellopy import Tello
import numpy as np
from matplotlib import pyplot as plt
import cv2
import os

new_model = load_model("model.h5")
class_labels = ["No line","Sharp Left","Sharp Right","Slight Left","Slight Right","Straight"]

drone = Tello()
drone.connect()
drone.streamon();
print(drone.get_battery())
    
while True:
    myFrame = drone.get_frame_read().frame
    imgDisplay = cv2.cvtColor(myFrame, cv2.COLOR_BGR2RGB)
    cv2.imshow("Camera Feed", imgDisplay)
    resized_img = tf.image.resize(imgDisplay, (256,256))
    prediction = new_model.predict(np.expand_dims(resized_img/255,0))

    index = np.argmax(prediction)
    print(f"Predicted Class: {class_labels[index]}")
    
    # Capturing frames from the video stream
    #if(kp.getKey("x")):
    #    cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
drone.end()