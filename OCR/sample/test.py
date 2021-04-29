from headers import square, pad, get_grayscale, thresholding, connected_components, resize, opening, closing
from pyimagesearch.cnn.networks.lenet import LeNet
from tensorflow.compat.v1.keras.optimizers import SGD

import os
import numpy as np
import cv2

# Build Le Net Model
weights = "./weights/lenet_weights.hdf5"

# initialize the optimizer and model
print("[INFO] compiling model...")
opt = SGD(lr=0.01)
model = LeNet.build(
    numChannels=1, 
    imgRows=28, 
    imgCols=28,
	numClasses=10,
	weightsPath=weights)

model.compile(
    loss="categorical_crossentropy", 
    optimizer=opt,
	metrics=["accuracy"])

# read sample image
img = cv2.imread('sample/handwritten_numbers.png')
cv2.imshow('sample',img)

# copy image for testing purposes
test = img.copy()

# grascale image
gray = get_grayscale(img)
cv2.imshow('gray',gray)

# binarize image
thresh = thresholding(gray, inv=1)
cv2.imshow('thresh',thresh)

# remove unwanted 
# thresh = opening(thresh)

# get components connected
(numLabels, labels, stats, centroids) = connected_components(thresh, connectivity=8)

components = []

for index, i in enumerate(range(0, numLabels)):

    if i == 0:
        text = "examining component {}/{} (background)".format(i + 1, numLabels)
    else:
        text = "examining component {}/{}".format( i + 1, numLabels)

        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        area = stats[i, cv2.CC_STAT_AREA]
        (cX, cY) = centroids[i]

        test = cv2.rectangle(test, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
        buffer = 10
        cropped = thresh[y-buffer:y+h+buffer, x-buffer:x+w+buffer]

        squared = square(cropped)

        squared = squared/255

        # put greyscale values in third dimension
        squared = np.atleast_3d(squared)

        print(squared.shape)

        if not squared.shape == (28,28,1):
            print("THERE IS A NOT SQUARE")
            continue

        components.append(squared)

        # cv2.imshow('cc',thresh)
        
    print("[INFO] {}".format(text))

print(len(components))
cv2.imshow('bounded numbers',test)

# turn component list to np array that the model can read
to_predict = np.array(components)

print(to_predict.shape)

# probabilities
probs = model.predict(to_predict)

# get prediction array
prediction = probs.argmax(axis=1)

for ind, i in enumerate(prediction):

    print('{} predicted: {}'.format(ind, i))

    cv2.imshow("number", components[ind])
    cv2.waitKey(0)

# cv2.waitKey(0)
cv2.destroyAllWindows()
