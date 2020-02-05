import cv2
import numpy as np
from os import listdir
from os.path import isfile, join


def substract(img1, img2):
    img1 = np.int16(img1)
    img2 = np.int16(img2)
    img = np.abs(img1 - img2)



# load all images into an array
myImages = [f for f in listdir("dataset2012/dataset/baseline/pedestrians/input/") if isfile(join("dataset2012/dataset/baseline/pedestrians/input/", f))]
num_images = len(myImages)


#Load background model (which is the first image)
bg_image = cv2.imread("dataset2012/dataset/baseline/pedestrians/input/in000001.jpg", 0)


#load each image
for n in range(0, num_images):
    image = cv2.imread("dataset2012/dataset/baseline/pedestrians/input/"+myImages[n], 0)

    # transform both images to int16
    image = np.int16(image)
    bg_image = np.int16(bg_image)

    # calculate the difference
    image = np.abs(image - bg_image)

    # if img < threshold then img = 0 (returns booleans 0 & 1)
    image[image < 40] = 0

    # if img != 0 then img = 255
    image[image != 0] = 255

    # save the image
    imagename = "bg1/image"+str(n)+".jpg"
    cv2.imwrite(imagename, image)

