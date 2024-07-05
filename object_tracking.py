import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))
def nothing(x):
    pass 
cv2.namedWindow("Color_Picker")
cv2.createTrackbar("LowerHue", "Color_Picker", 0, 255, nothing)
cv2.createTrackbar("LowerSaturation", "Color_Picker", 0, 255, nothing)
cv2.createTrackbar("LowerValue", "Color_Picker", 0, 255, nothing)
cv2.createTrackbar("UpperHue", "Color_Picker", 255, 255, nothing)
cv2.createTrackbar("UpperSaturation", "Color_Picker", 255, 255, nothing)
cv2.createTrackbar("UpperValue", "Color_Picker", 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame from camera")
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("LowerHue", "Color_Picker")
    l_s = cv2.getTrackbarPos("LowerSaturation", "Color_Picker")
    l_v = cv2.getTrackbarPos("LowerValue", "Color_Picker")
    u_h = cv2.getTrackbarPos("UpperHue", "Color_Picker")
    u_s = cv2.getTrackbarPos("UpperSaturation", "Color_Picker")
    u_v = cv2.getTrackbarPos("UpperValue", "Color_Picker")
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    out.write(res) 
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
