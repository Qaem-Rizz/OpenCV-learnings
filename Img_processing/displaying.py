import cv2

img_path="goku.png"

image = cv2.imread(img_path)

if image is None:
    print("Image not found")

else:
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
