import cv2

img_path="goku.png"

image = cv2.imread(img_path)

if image is not None:
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Greyscale Image", grey)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found or unable to read the image.")

    