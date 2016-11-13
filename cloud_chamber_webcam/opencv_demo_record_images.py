import numpy as np

import cv2

import subprocess

cap = cv2.VideoCapture(1)

w=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
h=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))

print w,h

directory = "images"


i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        # write the frame
        filename = "%s/cc%04d.png" % (directory,i)
        cv2.imwrite(filename,frame)

        cv2.imshow('frame',frame)
        i += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Make a movie out of the images.
cmd = "ffmpeg -framerate 20 -i %s/cc%s.png -c:v libx264 -r 30 -y -pix_fmt yuv420p %s/out.mp4" % (directory,"%04d",directory)
return_code = subprocess.call(cmd, shell=True)


# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

