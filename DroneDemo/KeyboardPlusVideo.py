from djitellopy import Tello
import KeyboardControlModule as kp
from time import sleep
import cv2

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

    # Only send controls if drone has taken off
    drone.send_rc_control(values[0], values[1], values[2], values[3])

    # Displaying video stream
    myFrame = drone.get_frame_read().frame
    img = cv2.cvtColor(myFrame, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (width, height))
    cv2.imshow("Camera Feed", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
drone.end()
