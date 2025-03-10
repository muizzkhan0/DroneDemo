from djitellopy import Tello
import KeyboardControlModule as kp
from time import sleep

# Connecting to the drone
drone = Tello()
drone.connect()
print(drone.get_battery())
# Initializing keyboard control
kp.init()

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

    return [l_r, f_b, u_d, yaw]



while True:
    values = getKeyInput()
    if takeoff == False:
        if(kp.getKey("SPACE")):
            drone.takeoff()
            takeoff = True
    else:
        if(kp.getKey("SPACE")):
            drone.land()
            takeoff = False
        drone.send_rc_control(values[0], values[1], values[2], values[3])
    sleep(0.05)



