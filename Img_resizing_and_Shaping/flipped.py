import cv2

img_path = "goku.png"
image = cv2.imread(img_path)

if image is None:
    print("Error: Unable to load image")

else:
    flipped_horizontal = cv2.flip(image, 1)  # 1 for horizontal flip, 0 for vertical flip , -1 for both horizontal and vertical flip
    flipped_vertical = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)
    
    cv2.imshow("Flipped horizontal", flipped_horizontal)
    cv2.imshow("Flipped vertical", flipped_vertical)
    cv2.imshow("Flipped both", flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()