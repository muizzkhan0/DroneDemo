from tracemalloc import take_snapshot
from djitellopy import Tello
import KeyboardControlModule as kp
import time
import cv2


# Connecting to the drone
drone = Tello()
drone.connect()
drone.streamon();
print(drone.get_battery())

# Video stream constants
width = 360
height = 240

while True:

    # Displaying video stream
    myFrame = drone.get_frame_read().frame
    img = cv2.cvtColor(myFrame, cv2.COLOR_BGR2RGB)
    cv2.imshow("Camera Feed", img)
    
    # Capturing frames from the video stream
    if(kp.getKey("x")):
        cv2.imwrite(f'Resources/New_Data/{time.time()}.jpg', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
drone.end()
