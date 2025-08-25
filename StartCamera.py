# here will be the main project python code.

import cv2
print(cv2.__version__)

## Run camera 

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("no stream :(")
    exit()


while(True):
    ret, frame = stream.read()
    if not ret:
        print("No more stream :(")
        break

    cv2.imshow("Laptop webcam", frame)
    if cv2.waitKey(1) == ord('q'):
        break


stream.release()
cv2.destroyAllWindows()
