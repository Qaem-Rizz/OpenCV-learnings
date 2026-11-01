import cv2

img_path=input("Enter the path to the image: ")

image = cv2.imread(img_path)

if image is not None:
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    print("Do you want to see the converted image?: ")
    choice = input("select 'y' for yes or 'n' for no: ")

    if choice.lower() == 'y':
        cv2.imshow("Greyscale Image", grey)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("You chose not to view the image.")

    print("Do you want to save the converted image?: ")
    save_choice = input("select 'y' for yes or 'n' for no: ")


    if save_choice.lower() == 'y':
        img_name = input("Enter the name for the saved image (with extension, e.g., 'image.png'): ")
        
        
        cv2.imwrite(img_name, grey)
        
        print("Image saved successfully.")
    
    else:
        print("You chose not to save the image.")


else:
    print("Image not found or unable to read the image.")

    