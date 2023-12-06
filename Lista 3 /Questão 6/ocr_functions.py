#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:48:35 2020

@author: Rodrigo
"""

import numpy as np
import cv2 as cv
import imutils

from imutils import contours

class ocr_Helper():
    
    def __init__(self):
        
        # define a dictionary that maps the first digit of a credit card
        # number to the credit card type
        self.FIRST_NUMBER = {
            "3": "American Express",
            "4": "Visa",
            "5": "MasterCard",
            "6": "Discover Card"
        }
        
        # load the reference OCR-A image from disk, convert it to grayscale,
        # and threshold it, such that the digits appear as *white* on a
        # *black* background
        # and invert it, such that the digits appear as *white* on a *black*
        ref = cv.imread("ocr_a_reference.png")
        
        ref = cv.cvtColor(ref, cv.COLOR_BGR2GRAY)
        ref = cv.threshold(ref, 10, 255, cv.THRESH_BINARY_INV)[1]
        
        # find contours in the OCR-A image (i.e,. the outlines of the digits)
        # sort them from left to right, and initialize a dictionary to map
        # digit name to the ROI
        refCnts = cv.findContours(ref.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        refCnts = refCnts[1] if imutils.is_cv3() else refCnts[0]
        refCnts = imutils.contours.sort_contours(refCnts, method="left-to-right")[0]
        
        self.digits = {}
        
        # loop over the OCR-A reference contours
        for (i, c) in enumerate(refCnts):
            # compute the bounding box for the digit, extract it, and resize
            # it to a fixed size
            (x, y, w, h) = cv.boundingRect(c)
            roi = ref[y:(y + h), x:(x + w)]
         
            # update the digits dictionary, mapping the digit name to the ROI
            self.digits[i] = roi

    def find_card_numbers(self, img_rgb, img_gray, mask):
        
        img_return = img_rgb.copy()
        
        # find contours in the thresholded image, then initialize the
        # list of digit locations
        cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        cnts = cnts[1] if imutils.is_cv3() else cnts[0]
        
        locs = []
        
        # loop over the contours
        for (i, c) in enumerate(cnts):
            # compute the bounding box of the contour, then use the
            # bounding box coordinates to derive the aspect ratio
            (x, y, w, h) = cv.boundingRect(c)
            ar = w / float(h)
         
            # since credit cards used a fixed size fonts with 4 groups
            # of 4 digits, we can prune potential contours based on the
            # aspect ratio
            if ar > 2.5 and ar < 4.5:
                # contours can further be pruned on minimum/maximum width
                # and height
                if (w > 40 and w < 70) and (h > 10 and h < 20):
                    # append the bounding box region of the digits group
                    # to our locations list
                    locs.append((x, y, w, h))
        
        # sort the digit locations from left-to-right, then initialize the
        # list of classified digits
        locs = sorted(locs, key=lambda x:x[0])
        
        
        output = []
        
        # loop over the 4 groupings of 4 digits
        for (i, (gX, gY, gW, gH)) in enumerate(locs):
            # initialize the list of group digits
            groupOutput = []
            
            group = img_gray[gY - 5:gY + gH + 5, gX - 5:gX + gW + 5]
            group = cv.threshold(group, 0, 255,cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
            
            digitCnts = cv.findContours(group.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            
            digitCnts = digitCnts[1] if imutils.is_cv3() else digitCnts[0]
            digitCnts = contours.sort_contours(digitCnts,method="left-to-right")[0]
            
            # loop over the digit contours
            for c in digitCnts:
                # compute the bounding box of the individual digit, extract
                # the digit, and resize it to have the same fixed size as
                # the reference OCR-A images
                (x, y, w, h) = cv.boundingRect(c)
                roi = group[y:y + h, x:x + w]
                roi = cv.resize(roi, (22, 36))
            
                # initialize a list of template matching scores	
                scores = []
            
                # loop over the reference digit name and digit ROI
                for (digit, digitROI) in self.digits.items():
                    # apply correlation-based template matching, take the
                    # score, and update the scores list
                    result = cv.matchTemplate(roi, digitROI,cv.TM_CCOEFF)
                    (_, score, _, _) = cv.minMaxLoc(result)
                    scores.append(score)
            
                # the classification for the digit ROI will be the reference
                # digit name with the *largest* template matching score
                groupOutput.append(str(np.argmax(scores)))
            
                # draw the digit classifications around the group
                cv.rectangle(img_return, (gX - 5, gY - 5),
                              (gX + gW + 5, gY + gH + 5), (0, 0, 255), 2)
                cv.putText(img_return, "".join(groupOutput), (gX, gY - 15),
                            cv.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)
        
            # update the output digits list
            output.extend(groupOutput)
            
        return img_return