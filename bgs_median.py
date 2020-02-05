import cv2
import numpy as np
from os import listdir
from os.path import isfile, join


# load all images into an array
temp = [f for f in listdir("dataset2012/dataset/baseline/PETS2006/input/") if isfile(join("dataset2012/dataset/baseline/PETS2006/input/", f))]

bufferSize = 60
buffer = []
myImages = []


# put the first n (which is the size of the buffer) images in buffer and the others in myImages array
for i in range(len(temp)):
    if i < bufferSize:
        buffer.append(temp[i])
    else:
        myImages.append(temp[i])


num_images = len(myImages)
bufferImages = []

# load initial buffer images
for b in range(0, bufferSize):
    img =  cv2.imread("dataset2012/dataset/baseline/PETS2006/input/"+buffer[b], 0)
    bufferImages.append(img)

# create copy of buffer to update it later
bufferImagesCopy = bufferImages

#load each image
for n in range(0, num_images):

    image = cv2.imread("dataset2012/dataset/baseline/PETS2006/input/"+myImages[n], 0)

    # transform list to array to use median function on it
    bufferImages = np.array(bufferImages)

    mediane = np.median(bufferImages, axis=0)

    # updating the buffer (remove first image and add current image)
    bufferImagesCopy.pop(0)
    bufferImagesCopy.append(image)
    bufferImages = bufferImagesCopy

    # transform both images to int16
    image = np.int16(image)
    mediane = np.int16(mediane)

    # calculate the difference
    image = np.abs(image - mediane)

    # if img < threshold then img = 0 (returns booleans 0 & 1)
    image[image < 40] = 0

    # if img != 0 then img = 255
    image[image != 0] = 255


    # save the image
    imagename = "bg3-1/image"+str(n)+".jpg"
    cv2.imwrite(imagename, image)
