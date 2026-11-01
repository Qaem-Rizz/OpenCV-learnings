import cv2

img_path="goku.png"

image=cv2.imread(img_path)

if image is None:
    print("Could not read the image.")

else:
    (h,w)= image.shape[:2]
    centre = (w//2, h//2)

    M = cv2.getRotationMatrix2D(centre, 45, 1)   #syntax: cv2.getRotationMatrix2D(center, angle- (+ for anti clock, - for clock), scale)

    rotated = cv2.warpAffine(image, M, (w,h)) #syntax: cv2.warpAffine(src- read image, M, (w,h) pair for newly rotated image )

    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Image", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()