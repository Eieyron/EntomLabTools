from headers import crop, square, pad, get_grayscale, thresholding, connected_components, resize, opening, closing
from pyimagesearch.cnn.networks.lenet import LeNet
from tensorflow.compat.v1.keras.optimizers import SGD
from collections import OrderedDict

import numpy as np
import cv2



class Float_Evaluator():

    def __init__(self):

        # Build Le Net Model
        self.weights = "./weights/lenet_weights.hdf5"

        # initialize the optimizer and model
        print("[INFO] compiling model...")
        self.opt = SGD(lr=0.01)
        self.model = LeNet.build(
            numChannels=1, 
            imgRows=28, 
            imgCols=28,
            numClasses=10,
            weightsPath=self.weights)

        self.model.compile(
            loss="categorical_crossentropy", 
            optimizer=self.opt,
            metrics=["accuracy"])

    def classify(self, objdir=None, image=None, verbose=False):

        if not image is None:
            img = image
        else:
            # read sample image
            img = cv2.imread(objdir)

        if verbose: cv2.imshow('sample',img)
            
        # copy image for testing purposes
        test = img.copy()
            
        # grayscale image
        gray = get_grayscale(img)
        if verbose: cv2.imshow('gray',gray)

        # binarize image
        thresh = thresholding(gray, inv=1)
        if verbose: cv2.imshow('thresh',thresh)

        # get components connected
        (numLabels, labels, stats, centroids) = connected_components(thresh, connectivity=8)

        numbers = {}

        total_area = img.shape[0] * img.shape[1]

        for index, stat in enumerate(stats):

            if index in [0,1]:
                continue

            left = stat[cv2.CC_STAT_LEFT]
            up = stat[cv2.CC_STAT_TOP]
            to_right = stat[cv2.CC_STAT_WIDTH]
            to_down = stat[cv2.CC_STAT_HEIGHT]
            area = stat[cv2.CC_STAT_AREA]
            (cX, cY) = centroids[index]

            # total_area += area

            if area/total_area*100 < 1 : # if area of the component is less than 1% of the total area, then it's a period
                
                # gotta find a better way of identifying a period
                # for now this suffices

                numbers[cX] = '.'

            else: 

                test = cv2.rectangle(test, (left, up), (left + to_right, up + to_down), (0, 255, 0), 2)

                if verbose: cv2.imshow('current label', test)

                cropped = crop(thresh, left, up, to_right, to_down, buffer=0)

                if verbose: cv2.imshow('cropped', cropped)

                padded_closed = pad(cropped, height_pad=10, width_pad=10)

                squared = square(padded_closed)
                if verbose: cv2.imshow('squared', squared)

                squared = squared/255

                # put greyscale values in third dimension
                squared = np.atleast_3d(squared)

                to_classify = [squared]
                to_predict = np.array(to_classify)

                # probabilities
                probs = self.model.predict(to_predict)

                # get prediction array
                prediction = probs.argmax(axis=1)

                # print(prediction[0])

                # return prediction[0]
                numbers[cX] = prediction[0]

                if verbose:
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()


        od = OrderedDict(sorted(numbers.items()))

        number = "".join([ str(y) for (x,y) in od.items()])

        print(number)
        to_return = "Error"
        try:
            to_return = float(number)
        except:
            print("[ERROR] Field does contain not Float")

        return to_return

            
# fe = Float_Evaluator()
# fe.classify(objdir='float0.png', verbose=True)

