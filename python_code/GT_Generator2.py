import time
import numpy as np
import cv2
import os
import re
import random 



def keyFunc(afilename):
    nondigits = re.compile("\D")
    return int(nondigits.sub("", afilename))

filename = 'D1'
folder = '/home/mgharasu/Videos/Dan videos/dip/'

# capt = cv2.VideoCapture('/home/mgharasu/Videos/Dan videos/curl/'+filename+'.avi')
files = os.listdir(folder+filename)

frame_files = list()
for x in sorted(files, key=keyFunc):
   frame_files.append(x)

count = 1
frame_number = 0
frame_seq = list()
coord_seq = list()
rep_count = 0
rec_points = 0

class CoordinateStore:
    def __init__(self):
        self.points = []

    def select_point(self,event,x,y,flags,param):
        global frame_number, rep_count, frame_seq, coord_seq, rec_points, count
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(frame,(x,y),3,(255,0,0),-1)
            self.points.append((x,y))
            print(x,y)
            rec_points += 1
            if rec_points % 3 == 0: 
                rep_count += 1               
                print("==============> rep count is ",rep_count)
                # f.write(str(rep_count)+","+str(frame_seq[0])+","+str(frame_seq[1])+","+str(frame_number)+","+str(coord_seq[0][0])+","+str(coord_seq[0][1])+","+str(coord_seq[1][0])+","+str(coord_seq[1][1])+","+str(x)+","+str(y)+"\n")
                # frame_number = 0
                frame_seq.append(count)
                coord_seq.append([x,y])
                rec_points = 0
            else:
                frame_seq.append(count)
                coord_seq.append([x,y])


coordinateStore1 = CoordinateStore()
cv2.namedWindow('select')
cv2.setMouseCallback('select',coordinateStore1.select_point)

scale = .6
while (count<len(frame_files)):
    frame = cv2.imread(folder+filename+'/'+str(count)+'.jpg')
    frame = cv2.resize(frame,(int(frame.shape[1]*scale),int(frame.shape[0]*scale)))

    if count>len(frame_files)-15:
        frame = cv2.putText(frame, "remaining frames: "+str(len(frame_files)-count),(50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 2)
    cv2.imshow("main", frame)
    
    def callme():
        cv2.imshow("select", frame)
        k = cv2.waitKey(0) & 0xFF
    
    k = cv2.waitKey(0) & 0xFF
    if (k == ord('q')):# or (count in [1,320]):
        callme()
        
    if k == ord('z'):
        # To Do            
        count -= 1
        # cv2.waitKey(0)

    if k == ord('x'):
        # To Do
        count += 1
        # cv2.waitKey(0)

    # if  frame_number == 603:
    #     f.write(str(rep_count)+","+str(frame_seq[0])+","+str(frame_seq[1])+","+str(frame_number)+","+str(coord_seq[0][0])+","+str(coord_seq[0][1])+","+str(coord_seq[1][0])+","+str(coord_seq[1][1])+","+str(x)+","+str(y)+"\n")
    # time.sleep(0.2)
    # count+=1
    
    print(count)
# frame_seq = [1, 58, 127, 129, 194, 269, 271, 338, 438]
# coord_seq = [[421, 219], [421, 137], [422, 231], [422, 231], [422, 132], [422, 232], [421, 235], [424, 134], [422, 226]]
# capt.release()
gt_f = open(folder+filename+'-new.txt','w')
line = ''
c=0
while c<len(frame_seq):
    if (c+1)%3==0:
        line += str(frame_seq[c])+','+str(coord_seq[c][0])+','+str(coord_seq[c][1])+','
        gt_f.write(line[:-1]+'\n')
        line = ''
    else:
        line += str(frame_seq[c])+','+str(coord_seq[c][0])+','+str(coord_seq[c][1])+','
    c+=1
    
gt_f.close()