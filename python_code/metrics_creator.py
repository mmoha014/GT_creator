# import numpy as np

# name = 'BBC'
# # out_f = open("gt_int/gt_"+name)
# for i in range(1,11):
#     # if i in [3,7]:
#     #     continue
#     filename = name+str(i)+".txt"
#     f = open("out/out_"+filename,'r')
#     out_f = open("gt_int/out_"+filename,"w")
#     for l in f.readlines():
#         v=l.split(',')
#         rep = int(v[0])
#         b1f=int(v[1])
#         tf=int(v[2])
#         b2f=int(v[3])
#         b1x=int(np.round(float(v[4])))
#         b1y=int(np.round(float(v[5])))
#         tx=int(np.round(float(v[6])))
#         ty=int(np.round(float(v[7])))
#         b2x=int(np.round(float(v[8])))
#         b2y=int(np.round(float(v[9])))
#         out_f.write(str(rep)+" "+str(b1f)+" "+str(tf)+" "+str(b2f)+" "+str(b1x)+" "+str(b1y)+" "+str(tx)+str(ty)+" "+str(b2x)+" "+str(b2y)+"\n")
#     out_f.close()
#     f.close()
# print("conversion is done")


import numpy as np

name = 'LR'
# out_f = open("gt_int/gt_"+name)
for i in range(1,11):
    i=4
    # if i in [3,7]:
    #     continue
    filename = name+str(i)+".txt"
    inp_f = open(filename,'r')
    # out_f = open("out_metrics/gt_mets_"+filename,'w')
    for l in inp_f.readlines():
        v=l.split(',')
        rep = int(v[0])
        b1f=int(v[1])
        tf=int(v[2])
        b2f=int(v[3])
        b1x=int(np.round(float(v[4])))
        b1y=int(np.round(float(v[5])))
        tx=int(np.round(float(v[6])))
        ty=int(np.round(float(v[7])))
        b2x=int(np.round(float(v[8])))
        b2y=int(np.round(float(v[9])))
        # out_f.write(str(rep)+" "+str(b1f)+" "+str(tf)+" "+str(b2f)+" "+str(b1x)+" "+str(b1y)+" "+str(tx)+str(ty)+" "+str(b2x)+" "+str(b2y)+"\n")
        liftT = abs(b1f-tf)/30.0
        lowerT = abs(tf-b2f)/30.0
        Rep_Duration = liftT+lowerT#(abs(b1f-tf)+abs(tf-b2f))/30.0
        lift_range = abs(b1y-ty)
        lower_range  =abs(ty-b2y)
        lift_vel = lift_range/liftT        
        lower_vel = lower_range/lowerT
        # out_f.write(str(liftT)+","+str(lowerT)+","+str(Rep_Duration)+","+str(lift_range)+","+str(lower_range)+","+str(lift_vel)+","+str(lower_vel)+"\n")
        
    # out_f.close()
    inp_f.close()
print("calculation is done")

