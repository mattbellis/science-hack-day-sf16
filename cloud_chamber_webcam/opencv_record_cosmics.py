import numpy as np

import cv2

import subprocess

cap = cv2.VideoCapture(1)

w=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
h=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))

print w,h

directory = "images"

cmd = "rm %s/*.png" % (directory)
return_code = subprocess.call(cmd, shell=True)

nimages = 128
nimages_half = int(128/2)

images = []
for i in range(0,nimages):
    images.append(None)

i = 0
ibuf = 0

istart = 0
second_half_recording = False
iend = 0

prev = None
first = True

# Start with a first screen
ret,prev = cap.read()
prev = cv2.cvtColor(prev,cv2.COLOR_BGR2GRAY)

recorded_enough = False

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret==True:

        #diff = frame - prev
        diff = cv2.absdiff(frame,prev)
        mean = diff.mean()

        # Show the frame
        cv2.imshow('frame',frame)
        #k = cv2.waitKey(0) & 0xFF

        images[ibuf] = frame

        print ibuf,istart,iend,mean

        # Stop recording, keep the last bit and just go a bit further
        #if cv2.waitKey(1) & 0xFF == ord('q') and second_half_recording==False:
        threshold = 10.0
        if (mean>threshold and second_half_recording==False and ibuf>1) or cv2.waitKey(1) & 0xFF == ord('q'):
            ISTART = ibuf - nimages_half
            if istart < 0:
                istart = nimages + istart
            #print "-------------------- ",istart
            second_half_recording = True
            iend = 0

        # Keep track of doing second half of the recording
        if second_half_recording:
            iend += 1

        if iend>=nimages_half:
            break

        ibuf += 1
        prev = frame

        # Start filling the buffer back in the beginning.
        if ibuf >= nimages:
            ibuf = 0
            recorded_enough = True



    else:
        break

if recorded_enough == False:
    nimages = ibuf 


cap.release()

for i in range(0,nimages):
    filename = "%s/cc%04d.png" % (directory,i)

    index = istart + i
    if index>=nimages:
        index -= nimages

    print i,index
    #cv2.imshow('frame',images[index])
    cv2.imwrite(filename,images[index])

# Make a movie out of the images.
cmd = "ffmpeg -framerate 18 -i %s/cc%s.png -c:v libx264 -r 30 -y -pix_fmt yuv420p %s/out.mp4" % (directory,"%04d",directory)
return_code = subprocess.call(cmd, shell=True)


# Release everything if job is finished
cv2.destroyAllWindows()

