import cv2

img_path="goku.png"

img = cv2.imread(img_path)

if img is None:
    print("Error: Could not read the image.")
else:
    print("Image recieved")
