import numpy as np

import cv2

cap = cv2.VideoCapture(1)

w=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
h=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))

print w,h

# Define the codec and create VideoWriter object
# For opencv3.0
#out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640,480))

# For opencv2.4
#out = cv2.VideoWriter('/home/bellis/output.avi',cv2.cv.CV_FOURCC('X','V','I','D'), 20.0, (w,h),True)
#fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
#fourcc = cv2.cv.CV_FOURCC(*'mjpg')
#out = cv2.VideoWriter('/home/bellis/science-hack-day-sf16/cloud_chamber_webcam/output.mp4',fourcc, 20.0, (w,h),True)
#fourcc = cv2.cv.CV_FOURCC('H','2','6','4')
#fourcc = cv2.cv.CV_FOURCC(*'H264')
#out = cv2.VideoWriter('/home/bellis/science-hack-day-sf16/cloud_chamber_webcam/output.mkv',fourcc, 20.0, (w,h),True)
#fourcc = cv2.cv.CV_FOURCC('m','p','4','v')
#fourcc = cv2.cv.CV_FOURCC(*'mp4v')
#out = cv2.VideoWriter('/home/bellis/output.mp4',fourcc, 20.0, (w,h),True)
#fourcc = cv2.cv.CV_FOURCC('X','V','I','D')
#fourcc = cv2.cv.CV_FOURCC('i', 'Y', 'U', 'V')
fourcc = cv2.cv.CV_FOURCC(*'XVID')
#out = cv2.VideoWriter('/home/bellis/science-hack-day-sf16/cloud_chamber_webcam/output.avi',fourcc, 20.0, (w,h),True)
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (w,h),True)

print out
print type(out)


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        # write the frame
        out.write(frame)
        #print ret,frame

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

