
from djitellopy import Tello
from tensorflow.keras.models import load_model
import numpy as np
import KeyboardControlModule as kp
import time
import cv2

new_model = load_model("model.h5")

# Connecting to the drone
drone = Tello()
drone.connect()
drone.streamon();
print(drone.get_battery())

# Initializing keyboard control
kp.init()

# Video stream constats
width = 360
height = 240

# Controlling the initial state
takeoff = False


def getKeyInput():
    l_r, f_b, u_d, yaw = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"):
        l_r = -speed
    elif kp.getKey("RIGHT"):
        l_r = speed

    if kp.getKey("UP"):
        f_b = speed
    elif kp.getKey("DOWN"):
        f_b = -speed

    if kp.getKey("w"):
        u_d = speed
    elif kp.getKey("s"):
        u_d = -speed

    if kp.getKey("a"):
        yaw = -speed
    elif kp.getKey("d"):
        yaw = speed

    if kp.getKey("o"):
        drone.takeoff()

    if kp.getKey("p"):
        drone.land()

    return [l_r, f_b, u_d, yaw]

while True:
    values = getKeyInput()

    # Uncomment to send controls to drone
    #drone.send_rc_control(values[0], values[1], values[2], values[3]) 

    # Displaying video stream
    myFrame = drone.get_frame_read().frame
    img = cv2.cvtColor(myFrame, cv2.COLOR_BGR2RGB)
    cv2.imshow("Camera Feed", img)

    # resize input image
    resized_img = tf.image.resize(img, (256,256))
    # predict using the model
    prediction = new_model.predict(np.expand_dims(resized_img/255,0))
    # add if statements for handling the prediction
    if(prediction < 0.16):
        print(f'Class 1: {prediction}')
    if(prediction > 0.16 & prediction < 0.33):
        print(f'Class 2: {prediction}')
    if(prediction > 0.33 & prediction < 0.497):
        print(f'Class 3: {prediction}')
    if(prediction > 0.497 & prediction < 0.663):
        print(f'Class 4: {prediction}')
    if(prediction > 0.663 & prediction < 0.83):
        print(f'Class 5: {prediction}')
    if(prediction > 0.83 & prediction < 1):
        print(f'Class 6: {prediction}')
    
    # Capturing frames from the video stream
    if(kp.getKey("x")):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
drone.end()
