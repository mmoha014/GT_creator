import cv2
import os

for i in range(4,5):
    filename = 'SP'+str(i)
    folder = '/home/mgharasu/Videos/Dan videos/shoulderPress/'
    if not os.path.exists(folder+filename):
        os.makedirs(folder+filename)


    capt = cv2.VideoCapture(folder+filename+'.avi')
    fr_num = 0
    a=True
    while True:
        ret, frame = capt.read()
        if not ret:
            break
        fr_num += 1
        if fr_num<34 and a:            
            continue
        elif a:
            fr_num = 1
            a=False
        cv2.imwrite(folder+filename+'/'+str( fr_num)+'.jpg',frame)