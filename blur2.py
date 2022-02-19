import cv2

# Read the image ได้ทีละภาพ
img = cv2.imread('C:/Users/HP/Downloads/facial_expressions-master/images/Aaron_Eckhart_0001.jpg')
 
# Convert to greyscale
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# Find the laplacian of this image and
# calculate the variance
var = cv2.Laplacian(grey, cv2.CV_64F).var()
 
# if variance is less than the set threshold
# image is blurred otherwise not
if var < 4:
    print('Image is Blurred')
else:
    print('Image Not Blurred')

