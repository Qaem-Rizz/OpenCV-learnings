import cv2

img_path="goku.png"

image=cv2.imread(img_path)

if image is not None:
    success= cv2.imwrite("goku_copy.png",image)
    if success :
        print("Image saved successfully")
    else:
        print("Error in saving image")
else:
    print("Error in loading image")

    