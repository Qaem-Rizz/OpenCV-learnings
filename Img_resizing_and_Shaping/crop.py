import cv2

img_path ="goku.png"

image=cv2.imread(img_path)

if image is None:
    print("Could not read the image.")
else:
    h,w,c = image.shape
    print(f"Height: {h}\nWidth: {w}")

    # Perform cropping operation

    print("Do you want to crop the image?")
    choice = input("Enter 'y' for yes or 'n' for no: ")
    
    if choice.lower() == 'y':
        w1=int(input("Enter the starting width (x1) for cropping: "))
        w2=int(input("Enter the ending width (x2) for cropping: "))
        h1=int(input("Enter the starting height (y1) for cropping: "))
        h2=int(input("Enter the ending height (y2) for cropping: "))

        cropped = image[w1:w2, h1:h2]  # Crop the image (y1:y2, x1:x2) - similar to SLICING
        
        cv2.imshow("Original Image", image)
        cv2.imshow("Cropped Image", cropped)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    