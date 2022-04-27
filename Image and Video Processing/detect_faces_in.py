# Other face features can be found here: https://github.com/opencv/opencv/tree/4.x/data/haarcascades

import cv2

face_cascade = cv2.CascadeClassifier(
    ".//Images//Files//haarcascade_frontalface_default.xml")

# Reading image in grayscale will increase performance of model of face recognition
img = cv2.imread(".//Images//Files//face1.jpg")

# Convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.1,
                                      minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)


# Visualize the image
cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
