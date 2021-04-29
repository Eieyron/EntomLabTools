from headers import crop, grayscale, findContours, square, pad, get_grayscale, thresholding, connected_components, resize, opening, closing

import os
import numpy as np
import cv2


dir = 'multiple_choice/'
images = []
image_names = []

to_classify = []

NEXT = 0
PREV = 1
CHILD = 2
PARENT = 3

verbose = input("verbose?: y/n ")

for obj in os.listdir(dir):
    if obj == '.DS_Store':
        continue
    objdir = os.path.join(dir,obj)

    image_name = obj.replace('.png','')

    print('[INFO] Reading:', objdir)
    
# read sample image
    img = cv2.imread(objdir)

    imgray = grayscale(img)
    if verbose == 'y': cv2.imshow('sample',img)

    thresh = thresholding(imgray, inv=1)
    if verbose == 'y': cv2.imshow('inverted binarized',thresh)

    contours, hierarchy = findContours(thresh)
    # print("hieararchy: \n",hierarchy)
    # if verbose == 'y': cv2.imshow('contour image',contour_image)

    color_dict = {
        # -1:(0,0,0),
        0:(0,0,255), #red 
        1:(0,255,0), #green
        2:(255,0,0), #blue
        3:(0,255,255), #yellow
        4:(255,255,0), #teal
        5:(255,0,255), #magenta
        6:(0,0,75), #maroon
        7:(0,75,0), #swamp
        8:(75,0,0), #ateneo
        9:(0,0,0) #black
    }


    answer_contours = [contour for index, contour in enumerate(contours) if hierarchy[0, index, PARENT] == 1]

    color_dict = {
        0:(0,0,0),
        1:(0,0,255),
        2:(0,255,0),
        3:(255,0,0),
    }

    index_to_choice = {
        0:'d',
        1:'c',
        2:'b',
        3:'a'
    }

    choice_images = {
        'a':None,
        'b':None,
        'c':None,
        'd':None
    }

    for index, c in enumerate(answer_contours):
        # print(c)
        x,y,w,h = cv2.boundingRect(c)

        cropped = crop(imgray, x, y, w, h)
        choice_images[index_to_choice[index]] = crop(imgray, x, y, w, h)

        if verbose == 'y': cv2.imshow(index_to_choice[index],cropped)


        new_contour_image = cv2.drawContours(img, [c], -1, color_dict[index], 2)
        

    if verbose == 'y': cv2.imshow('new contour image',new_contour_image)

    if verbose == 'y':
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    