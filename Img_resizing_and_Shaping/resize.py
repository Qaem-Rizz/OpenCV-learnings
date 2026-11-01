import cv2

img_path = "goku.png"

image = cv2.imread(img_path)

if image is None:
    print("Error: Unable to load image")
else:
    resized= cv2.resize(image, (400, 450))  #[pehle width then height - tuple form me]


    cv2.imshow("Image", image)
    cv2.imshow("Resized Image", resized)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()