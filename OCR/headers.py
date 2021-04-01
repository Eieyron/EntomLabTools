import cv2
import numpy as np

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image, inv=0):

    if inv == 0:
        inv_const = cv2.THRESH_BINARY
    elif inv == 1:
        inv_const = cv2.THRESH_BINARY_INV

    return cv2.threshold(image, 0, 255, inv_const + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#closing - dilation followed by erosion
def closing(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# match the height/width to which dimension is bigger
def square(image, dimension=28):

    height, width = image.shape

    if height > width:
        padding = height - width
        padding //= 2
        image = pad(image, width_pad=padding)
        image = square_resize_px(image, dimension)

    elif width > height:
        padding = width - height        
        padding //= 2
        image = pad(image, height_pad=padding)
        image = square_resize_px(image, dimension)

    return image

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 

#connected components
def connected_components(image, connectivity=4):
    return cv2.connectedComponentsWithStats( image, connectivity, cv2.CV_32S)

def resize(img, scale_percent=60):

    print('Original Dimensions : ',img.shape)
    
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    print('Final Dimensions : ', dim)
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

def square_resize_px(img, target_pixel):
    dim = (target_pixel, target_pixel)

    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


def pad(img, height_pad=0, width_pad=0):
    '''
        pads image with given height and width padding
        current available anchors:
        0 - center
    '''

    top, bottom, left, right = (height_pad, height_pad, width_pad, width_pad)
    borderType = cv2.BORDER_REPLICATE

    return cv2.copyMakeBorder(img, top, bottom, left, right, borderType, None, None)


