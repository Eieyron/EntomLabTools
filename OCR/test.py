import cv2 
import pytesseract
from headers import square_resize_px, pad, get_grayscale, thresholding, connected_components, resize, opening, closing

img = cv2.imread('sample_number_read.png')
test = img.copy()

cv2.imshow('sample',img)

gray = get_grayscale(img)
cv2.imshow('gray',gray)

thresh = thresholding(gray, inv=1)
cv2.imshow('thresh',thresh)

thresh = opening(thresh)

(numLabels, labels, stats, centroids) = connected_components(thresh, connectivity=8)

output = thresholding(gray)
output = closing(output)

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
        # output = img.copy()
        test = cv2.rectangle(test, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
        buffer = 10
        cropped = output[y-buffer:y+h+buffer, x-buffer:x+w+buffer]

        height, width = cropped.shape

        if height > width:
            padding = height - width
            padding //= 2
            squared =  pad(cropped, width_pad=padding)
            squared = square_resize_px(squared, 28)


        elif width > height:
            padding = width - height        
            padding //= 2
            squared =  pad(cropped, height_pad=padding)
            squared = square_resize_px(squared, 28)

        components.append(squared)
        # cv2.imwrite("number"+str(index), )


        cv2.imshow('cc',output)
        
    print("[INFO] {}".format(text))

cv2.imshow('bounded numbers',test)

for ind, i in enumerate(components):

    # resized = resize(i, scale_percent=60)

    # cv2.imshow('cc resized'+str(ind), resized)
    cv2.imshow('cc'+str(ind), i)
    cv2.imwrite('./test/cc'+str(ind)+'.jpg', i)

    custom_config = '--psm 10 --oem 1 -c tessedit_char_whitelist=0123456789'
    x = pytesseract.image_to_string(i, config=custom_config)

    print(str(ind),x)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

custom_config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789'
x = pytesseract.image_to_string(output, config=custom_config)

print('as whole image: ', x)

cv2.waitKey(0)
cv2.destroyAllWindows()
