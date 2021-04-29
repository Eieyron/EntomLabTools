from headers import crop, square, pad, get_grayscale, thresholding, connected_components, resize, opening, closing
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

dir = 'to_classify/'
images = []
image_names = []

to_classify = []

verbose = input("verbose?: Y/N ")

for obj in os.listdir(dir):
    if obj == '.DS_Store':
        continue
    objdir = os.path.join(dir,obj)

    image_name = obj.replace('.png','')

    print('[INFO] Reading:', objdir)
    
# read sample image
    img = cv2.imread(objdir)
    if verbose == 'Y': cv2.imshow('sample',img)
    
# copy image for testing purposes
    test = img.copy()
    
# grayscale image
    gray = get_grayscale(img)
    if verbose == 'Y': cv2.imshow('gray',gray)

# binarize image
    thresh = thresholding(gray, inv=1)
    if verbose == 'Y': cv2.imshow('thresh',thresh)

# remove unwanted information
    # closed7 = closing(thresh, size=[7])
    # if verbose == 'Y': cv2.imshow('closed7', closed7)

    closed5 = closing(thresh, size=[5])
    if verbose == 'Y': cv2.imshow(image_name, closed5)

# get components connected
    (numLabels, labels, stats, centroids) = connected_components(closed5, connectivity=8)
    areas = [x[cv2.CC_STAT_AREA] for x in stats]
    index_of_biggest_area = 0
    biggest_area = 0

    for index, area in enumerate(areas):

        if index == 0:
            continue
    
        if biggest_area < area:
            index_of_biggest_area = index
            biggest_area = area
            
    print(index_of_biggest_area)

    left = stats[index_of_biggest_area, cv2.CC_STAT_LEFT]
    up = stats[index_of_biggest_area, cv2.CC_STAT_TOP]
    to_right = stats[index_of_biggest_area, cv2.CC_STAT_WIDTH]
    to_down = stats[index_of_biggest_area, cv2.CC_STAT_HEIGHT]
    area = stats[index_of_biggest_area, cv2.CC_STAT_AREA]
    (cX, cY) = centroids[index_of_biggest_area]

    print('bounded area:',area)

    test = cv2.rectangle(test, (left, up), (left + to_right, up + to_down), (0, 255, 0), 2)

    if verbose == 'Y': cv2.imshow('bounded biggest area', test)

    padded_closed = pad(closed5, height_pad=10, width_pad=10)
    # left += 10
    # up += 10
    
    buffer = 10
    cropped = crop(padded_closed, left, up, to_right, to_down)

    if verbose == 'Y': cv2.imshow('cropped', cropped)

    squared = square(cropped)

    if verbose == 'Y': cv2.imshow('squared biggest area', squared)


    squared = squared/255

    # put greyscale values in third dimension
    squared = np.atleast_3d(squared)

    if not squared.shape == (28,28,1):
        print("THERE IS A NOT SQUARE")
        continue

    to_classify.append(squared)
    image_names.append(image_name)
    images.append(img)

    if verbose == 'Y': 
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# turn component list to np array that the model can read
to_predict = np.array(to_classify)

# print(to_predict.shape)

# probabilities
probs = model.predict(to_predict)

# get prediction array
prediction = probs.argmax(axis=1)

print("prediction len: {} | image len: {}".format(len(prediction), len(image_names)))
total_correct = 0

verbose = input("verbose?: Y/N ")

for ind, i in enumerate(prediction):

    predicted = i
    actual = int(image_names[ind][0])

    total_correct += 1 if predicted == actual else 0

    percentage = (total_correct / (ind+1)) * 100

    if verbose == 'Y': cv2.imshow(image_names[ind][0],images[ind])    

    print('{} predicted: {} | actual: {} | correct%: {}'.format(ind, predicted, actual, percentage))

    if verbose == 'Y':
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#     if verbose == 'Y': cv2.imshow("number", components[ind])
#     cv2.waitKey(0)

