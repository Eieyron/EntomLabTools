'''
	author: dmdelarosa@up.edu.ph
	description: Tesseract OCR sample
	References: 
		https://github.com/tesseract-ocr/tesseract/
		https://medium.freecodecamp.org/getting-started-with-tesseract-part-i-2a6a6b1cf75e
	Installation of Tesseract for Ubuntu:
		sudo add-apt-repository ppa:alex-p/tesseract-ocr
		sudo apt-get update
		sudo apt-get install tesseract-ocr
		pip3 install pytesseract
	Installation of Tesseract for Windows:
		https://github.com/UB-Mannheim/tesseract/wiki
'''

import numpy as np
import cv2
import pytesseract

# load sample image
image = cv2.imread("sample.png",0)
# clean image
image = cv2.blur(image,(5,5))
# binarize the image
ret,binarized = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

# get connected components
ret,labels,stats,centroids = cv2.connectedComponentsWithStats(binarized,8)

# for each component, check character
for i in range(1,ret):
	t = stats[i, cv2.CC_STAT_TOP];
	b = t + stats[i, cv2.CC_STAT_HEIGHT] -1;
	l = stats[i, cv2.CC_STAT_LEFT];
	r = l + stats[i, cv2.CC_STAT_WIDTH] -1;
	# well = binarized[t:b, l:r]
	well = binarized[t-5:b+5, l-5:r+5]
	cv2.imshow("he{}".format(i), well)
	print(pytesseract.image_to_string(well, config="--psm 7"))

cv2.imshow("Full", binarized)
print("Whole image: "+pytesseract.image_to_string(binarized))

cv2.waitKey(0)
cv2.destroyAllWindows()



