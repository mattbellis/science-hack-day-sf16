import numpy as np

import cv2

cap = cv2.VideoCapture(1)

w=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
h=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))

print w,h


codecs = ['XVID','MJPG','H264','MP4V','MPEG','h264','xvid','mpeg']
extension = ['avi','mp4','mjpg','mp4v','mkv','mpeg']

for c in codecs:
    for e in extension:

        fourcc = cv2.cv.CV_FOURCC(*c)
        filename = 'output.%s' % (e)

        out = cv2.VideoWriter(filename,fourcc, 20.0, (w,h),True)

        test = out.isOpened()

        if test==True:
            print c,e
        else:
            print test

