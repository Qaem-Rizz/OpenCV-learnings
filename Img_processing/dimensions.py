import cv2

img_path="goku.png"

image=cv2.imread(img_path)

if image is not None:
    h,w,c = image.shape

    print(f"Height: {h}\nWidth: {w}\nChannels: {c}")

else:
    print("Image not found or unable to read the image.")