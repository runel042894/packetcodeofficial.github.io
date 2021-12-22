import cv2

img=cv2.imread("image/MFI-Building and wirring.png", 1)


resized_image=cv2.resize(img, (800,400))
cv2.imshow("image/jacert.png", resized_image)
cv2.imwrite("image/MFI-Building and wirring_resized.png", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()