import cv2

# Read image in grayscale
img = cv2.imread(".//Images//galaxy.jpg", 0)

# resize the image
resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

# Show the image in cv2 window
cv2.imshow("Galaxy", resized_img)

# write the image back
cv2.imwrite(".//Images//Galaxy_resize.jpg", resized_img)

# Wait for user to press any key to close the window
cv2.waitKey(0)

# Close all cv2 windows
cv2.destroyAllWindows()
