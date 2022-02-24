from headers import crop, grayscale, findContours, square, pad, get_grayscale, thresholding, connected_components, resize, opening, closing

import os
import numpy as np
import cv2

def evaluate_multiple_choice(img, choices, verbose=False):

    # objdir = "contours3.png"

    # img = cv2.imread(objdir)

    imgray = grayscale(img)
    if verbose: cv2.imshow('sample',img)

    thresh = thresholding(imgray, inv=1)
    if verbose: cv2.imshow('inverted binarized',thresh)

    contours, hierarchy = findContours(thresh)

    child_matrix = {}

    # fill child_matrix
    for index, cont in enumerate(contours):

        if hierarchy[0, index, 3] == 1: # if part of a choice

            child_matrix[index] = []

            for child_index, child in enumerate(hierarchy[0]):
                if child[3] == index:
                    child_matrix[index].append(child_index)
            
    # print(child_matrix)
    answer = 'x'
    area_diff = 'x'
    biggest_area_diff = 'x'
    initial = True
    final = False

    centroids = {}

    for key,val in child_matrix.items():
        
        # print(key,val)

        M = cv2.moments(contours[key])
        cx = int(M['m10']/M['m00'])
        centroids[key] = cx

        if val == []:
            answer = key
            final = True
            continue

        elif not final:

            child_area = 0
            for child_index in val:
                child_area += cv2.contourArea(contours[child_index])

            area_diff = cv2.contourArea(contours[key]) - child_area
            # print("parent area:", cv2.contourArea(contours[key]))
            # print("child area:", child_area)
            # print("area diff:", area_diff)
                
            img = cv2.drawContours(img, [contours[key]], -1, (0,0,255), 2)
            
            if initial:
                
                biggest_area_diff = area_diff 
                answer = key
                initial = False
            
            else:
                
                if biggest_area_diff <= area_diff:
                    biggest_area_diff = area_diff
                    answer = key

    # print(centroids)
    # print(answer)

    ranking = {key: rank for rank, key in enumerate(sorted(centroids, key=centroids.get, reverse=False), 0)}

    return({
        "answer":ranking[answer],
        "value":choices[ranking[answer]]
    })


