from djitellopy import Tello
import cv2
import time

#video stream constats
width = 320
height = 240 # width and height of the image


# Connecting to the drone
drone = Tello()
drone.connect()

print(drone.get_battery())

drone.streamon()

while True:
    myFrame = drone.get_frame_read().frame
    #img = cv2.resize(myFrame, (width, height))
    myFrame = cv2.cvtColor(myFrame, cv2.COLOR_BGR2RGB)
    cv2.imshow("Camera Feed", myFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
drone.end()