import cv2
import numpy as np
import time
filename = 'D1'
capt = cv2.VideoCapture('/home/mgharasu/Videos/Dan videos/dip/'+filename+'.avi')
# f= open(filename+'.txt','w')
frame_number = 0
frame_seq = list()
coord_seq = list()
rep_count = 0
rec_points = 0
class CoordinateStore:
    def __init__(self):
        self.points = []

    def select_point(self,event,x,y,flags,param):
        global frame_number, rep_count, frame_seq, coord_seq, rec_points
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
                frame_seq = [frame_number]
                coord_seq = [[x,y]]
                rec_points = 1
            else:
                frame_seq.append(frame_number)
                coord_seq.append([x,y])


coordinateStore1 = CoordinateStore()


# Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('select')
cv2.setMouseCallback('select',coordinateStore1.select_point)
scale = 0.6
x,y=0,0
count = 0
while True:
    ret, frame = capt.read()
    if not ret:
        break

    # count+=1
    # # print(count)
    # if count<300:
    #     frame_number=300
    #     continue
    
    # frame = cv2.resize(frame())
    frame = cv2.resize(frame,(int(frame.shape[1]*scale),int(frame.shape[0]*scale)))
    frame_number += 1
    # time.sleep(0.1)
    cv2.imshow("main", frame)
    
    if (cv2.waitKey(1) & 0xFF == ord('q')) or frame_number in [1,320]:
        # while True:
        cv2.imshow("select", frame)
        k = cv2.waitKey(0) & 0xFF
        if rep_count == 16:
            print("rep count is 17")
    # if  frame_number == 603:
    #     f.write(str(rep_count)+","+str(frame_seq[0])+","+str(frame_seq[1])+","+str(frame_number)+","+str(coord_seq[0][0])+","+str(coord_seq[0][1])+","+str(coord_seq[1][0])+","+str(coord_seq[1][1])+","+str(x)+","+str(y)+"\n")
    time.sleep(0.2)
    print(frame_number)
        # cv2.setMouseCallback('Drawing spline',mousePosition,param)
# f.close()

"""
1,1,22,77,436,218,412,96,429,222
2,77,99,139,429,222,417,91,441,219
3,139,167,211,441,219,423,91,436,220
4,211,234,278,436,220,417,90,431,224


"""
