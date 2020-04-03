import numpy as np
import matplotlib.pyplot as plt

# liftT = abs(b1f-tf)/30.0
# lowerT = abs(tf-b2f)/30.0
# Rep_Duration = liftT+lowerT#(abs(b1f-tf)+abs(tf-b2f))/30.0
# lift_range = abs(b1y-ty)
# lower_range  =abs(ty-b2y)
# lift_vel = lift_range/liftT
# lower_vel = lower_range/lowerT

# col_liftT = [[] for i in range(10)]
# col_liftT = [[] for i in range(10)]
col_liftT = list()
col_lowerT = list()
col_rep_dur = list()
col_liftRange = list()
col_lowerRange = list()
col_lift_velocity= list()
col_lower_velocity = list()

liftT, lowerT,rep_Duration, lift_range,lower_range, lift_vel,lower_vel = list(),list(),list(),list(),list(),list(),list()

listname = ['BBC','D','LR','SP','UR']
for name in listname:
    for i in range(1,11):
        
        if name == 'D' and i in [3,7]:
            continue

        filename = name+str(i)+".txt"
        out_f = open('out_metrics/out_mets_'+filename,'r')
        gt_f =  open('gt_metrics/gt_mets_'+filename,'r')

        for gt,out in zip(gt_f.readlines(),out_f.readlines()):
            v = gt.split(',')
            o = out.split(',')

            # str(liftT)+","+str(lowerT)+","+str(Rep_Duration)+","+str(lift_range)+","+str(lower_range)+","+str(lift_vel)+","+str(lower_vel)+"\n")
            liftT.append(abs(float(v[0])-float(o[0])))
            lowerT.append(abs(float(v[1])-float(o[1])))
            rep_Duration.append(abs(float(v[2])-float(o[2])))
            lift_range.append(abs(float(v[3])-float(o[3])))            
            lower_range.append(abs(float(v[4])-float(o[4])))
            lift_vel.append(abs(float(v[5])-float(o[5])))
            if lift_vel[-1]>100:
                a=0
            lower_vel.append(abs(float(v[6])-float(o[6])))
    
    col_liftT.append(liftT)
    liftT = list()
    col_lowerT.append(lowerT)
    # if lowerT
    lowerT=list()
    col_rep_dur.append(rep_Duration)
    rep_Duration=list()
    col_liftRange.append(lift_range)
    lift_range = list()
    col_lowerRange.append(lower_range)
    lower_range = list()
    col_lift_velocity.append(lift_vel)
    lift_vel = list()
    col_lower_velocity.append(lower_vel)
    lower_vel = list()

data_liftT = [lt for lt in col_lift_velocity] 
a=0

fig = plt.figure(1)
ax=fig.add_subplot(111)
ax.set_xticks([1,2,3,4,5])
ax.set_xlabel('video group')

# lbs=['BBC','D','LR','SP','UR']#['Barbell Curl','lat Raise','Shoulder Press','Upright Row','Dip']
ax.set_xticklabels(listname)
ax.set_ylabel('Error (pixel displacement)')
ax.set_title('Error for lifting range')
bp = ax.boxplot(data_liftT)
plt.show()





