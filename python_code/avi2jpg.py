import cv2
import os

for i in range(8,9):
    filename = 'D'+str(i)
    folder = '/home/mgharasu/Videos/Dan videos/dip/'
    if not os.path.exists(folder+filename):
        os.makedirs(folder+filename)


    capt = cv2.VideoCapture(folder+filename+'.avi')
    fr_num = 0
    while True:
        ret, frame = capt.read()
        if not ret:
            break
        fr_num += 1
        cv2.imwrite(folder+filename+'/'+str( fr_num)+'.jpg',frame)