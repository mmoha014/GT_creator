import numpy as np
import matplotlib.pyplot as plt

def distance(low, high, x):
    if x>=low and x<= high:
        return 0
    else:
        d1=abs(low-x)
        d2=abs(high-x)
        return d1 if d1<=d2 else d2

dataplot = list()
for type in ['BBC', 'LR','UR']
for i in range(1,11):
    file = 'SP'+str(i)
    gtf = open('/home/mgharasu/Videos/Dan videos/shoulderPress/'+file+'.txt','r')
    outf = open('/home/mgharasu/Documents/Noah_project/alpha2/AlphaPose/out/out_'+file+'.txt','r')

    out = []
    for l in outf.readlines():
        v = l.split(',')
        """
        0 rep_count     4 b1_peak_x       8 b1y_l     12 t_peak       16 tx_h         20 b2fre        24 b2x_l
        1 b1frs         5 b1_peak_y       9 b1y_h     13 tx_peak      17 ty_l         21 b2_peak      25 b2x_h
        2 b1fre         6 b1x_l          10 tfrs     14 ty_peak      18 ty_h         22 b2x          26 b2y_l
        3 b1_peak       7 b1x_h          11 tfre     15 tx_l         19 b2frs        23 b2y          27 b2y_h
        """
        out.append([int(v[0]),int(v[1]),int(v[2]), int(v[3]), float(v[4]),float(v[5]),float(v[6]),float(v[7]),float(v[8]),float(v[9]), int(v[10]), int(v[11]),
        int(v[12]), float(v[13]), float(v[14]), float(v[15]), float(v[16]), float(v[17]), float(v[18]), int(v[19]), int(v[20]), int(v[21]), float(v[22]), float(v[23]),
        float(v[24]), float(v[25]), float(v[26]), float(v[27])])

   

    gt = []
    for l in gtf.readlines():
        v = l.split(',')
        """
        0,1,2: b1f, b1x, b1y       3,4,5: tf, tx, ty        6,7,8: b2f,b2x,b2y
        """
        gt.append([int(v[0]), float(v[1]), float(v[2]), int(v[3]), float(v[4]), float(v[5]), int(v[6]), float(v[7]), float(v[8])])

    Err_liftROM, Err_lowerROM, Err_liftT, Err_lowerT, Err_liftV, Err_lowerV = list(), list(), list(), list(), list(), list()
    for i in range(len(gt)):
        # b1f, b1x, b1y = gt[i][0],gt[i][1],gt[i][2]
        # tf, tx, ty = gt[i][3],gt[i][4],gt[i][5]
        # b2f, b2x, b2y = gt[i][6], gt[i][7], gt[i][8]

        Err_b1f = distance(out[i][1], out[i][2], gt[i][0]) # out_b1frs,out_b1fre, gt_b1f
        Err_b1y = distance(out[i][8], out[i][9], gt[i][2]) # out_b1y_l, out_b1y_h, gt_b1y
        
        Err_tf = distance(out[i][10],out[i][11],gt[i][3]) # out_tfrs,out_tfre,gt_tf
        Err_ty = distance(out[i][17], out[i][18], gt[i][5]) # out_ty_l, out_ty_h, gt_ty

        Err_b2f = distance(out[i][19], out[i][20], gt[i][6]) # b2frs, b2fre, gt_b2f
        Err_b2y = distance(out[i][26], out[i][27], gt[i][8]) # b2y_l, b2y_h, gt_b2y

        out_LiftROM = [abs(out[i][18]-out[i][8]),abs(out[i][9]-out[i][17])]  #b1y_h-ty_l
        out_LowerROM = [abs(out[i][18]-out[i][26]),abs(out[i][27]-out[i][18])] #ty_h-b2y_l
        out_liftT = [abs(out[i][2]-out[i][10])/30.0, abs(out[i][11]-out[i][1])/30.0] #b1fre-tfrs
        out_lowerT = [abs(out[i][11]-out[i][19])/30, abs(out[i][20]-out[i][10])/30.0] #tfre-b2frs
        out_liftV = [out_LiftROM[1]/out_liftT[1], out_LiftROM[0]/out_liftT[0]]
        out_lowerV = [out_LowerROM[1]/out_lowerT[1], out_LowerROM[0]/out_lowerT[0]]

        gt_liftT = abs(gt[i][3]-gt[i][0])/30.0 #tf-b1f
        gt_lowerT = abs(gt[i][6]-gt[i][3])/30.0 # tf-b2f
        gt_liftROM = abs(gt[i][2]-gt[i][5]) # ty-b1y
        gt_lowerROM = abs(gt[i][8]-gt[i][5]) # b2y-ty
        gt_LiftV = gt_liftROM/gt_liftT
        gt_lowerV = gt_lowerROM/gt_lowerT
        # Err_liftROM, Err_lowerROM, Err_liftT, Err_lowerT, Err_liftV, Err_lowerV = list(), list(), list(), list(), list(), list()
        Err_liftROM.append( distance(out_LiftROM[0], out_LiftROM[1], gt_liftROM))
        Err_lowerROM.append(distance(out_LowerROM[0], out_LowerROM[1], gt_lowerROM))
        if Err_lowerROM[-1]>20:
            a=0
        Err_liftT.append(distance(out_liftT[0], out_liftT[1], gt_liftT))
        Err_lowerT.append(distance(out_lowerT[0], out_lowerT[1], gt_lowerT))
        Err_liftV.append(distance(out_liftV[0], out_liftV[1], gt_LiftV))
        Err_lowerV.append(distance(out_lowerV[0], out_lowerV[1], gt_lowerV))

    dataplot.append(Err_lowerV)
fig = plt.figure(1)
ax=fig.add_subplot(111)
# ax.set_xticks([1,2,3,4,5])
ax.set_xlabel('video number')

# lbs=['BBC','D','LR','SP','UR']#['Barbell Curl','lat Raise','Shoulder Press','Upright Row','Dip']
# ax.set_xticklabels(listname)
ax.set_ylabel('Error (pixel displacement/sec in one half rep)')
ax.set_title('Lowering velocity error in the Shoulder Press')
bp = ax.boxplot(dataplot)
plt.show()
