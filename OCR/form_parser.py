from headers import crop, grayscale, findContours, square, pad, get_grayscale, thresholding, connected_components, resize, opening, closing
from pdf2image import convert_from_path, convert_from_bytes

import multiple_choice_evaluator

import cv2
import numpy as np
import json


images = convert_from_path('forms/out/sample.pdf')

cv2_images = []

# for image in images:    

image = images[0].convert('RGB')

open_cv_image = np.array(image)

# Convert RGB to BGR 
img = open_cv_image[:, :, ::-1].copy() 

imgray = grayscale(img)

thresh = thresholding(imgray, inv=1)

contours, hierarchy = findContours(thresh)

color_dict = {
    # -1:(0,0,0),
    0:(0,0,255), #red 
    1:(0,255,0), #green
    2:(255,0,0), #blue
    # 3:(0,255,255), #yellow
    # 4:(255,255,0), #teal
    # 5:(255,0,255), #magenta
    # 6:(0,0,75), #maroon
    # 7:(0,75,0), #swamp
    # 8:(75,0,0), #ateneo
    # 9:(0,0,0) #black
}

# get contour with bigest area (Table)
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]

# get all cells within table
max_index_children = [ contours[index] for index, x in enumerate(hierarchy[0]) if x[3] == max_index ]

# Arrange contours per column in a table
column = 11
rows = 20

table = [ [] for x in range(0,column)]

for cell in max_index_children:

    column -= 1
    table[column].insert(0,cell)

    if column == 0:
        rows -= 1

        if rows == 0:
            break
        
        else:
            column = 11

table = np.array(table)

with open("forms/sample.json","r") as json_obj:
    # print(json_obj)
    page_format = json.load(json_obj)
    
    page_header = page_format["page_header"]
    page_date = page_format["page_date"]
    form_format = page_format["form_format"]

no_of_questions = len(form_format)

ref_img = img.copy()

# for index, cell in enumerate(max_index_children):
for index, column in enumerate(table):

    if index == no_of_questions:
        break

    if form_format[str(index+1)]["qtype"] == 1:
    
        for cell_index, cell in enumerate(column):
            
            x,y,w,h = cv2.boundingRect(cell)

            cell_img = ref_img[y:y+h, x:x+w]
            cv2.imshow("cell",cell_img)

            img = cv2.drawContours(img, [cell], -1, color_dict[index%3], 2)

            cv2.imshow("image",img)
            # cv2.imwrite("contours"+str(cell_index)+".png",cell_img)

            print(multiple_choice_evaluator.evaluate_multiple_choice(cell_img,form_format[str(index+1)]["choices"]))

            cv2.waitKey(0)
            cv2.destroyAllWindows()



