import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from sklearn.metrics.pairwise import euclidean_distances

col_err_f = []
col_dist_c = []
name = "SP"
f = open("er_"+"err_metrics_"+name+".txt","w")
for fnum in range(1,11):
    # if fnum in [1,3,4,5,7]:
    #     continue
    if fnum!=7:
        continue

    filename = name+str(fnum)
    gtf =open(filename+".txt","r")
    outf = open("out/out_"+filename+".txt","r")
    gtlines = list()# gtf.readlines()
    outlines = list()#outf.readlines()
    lines = gtf.readlines()
    for i in range(len(lines)):
        l = lines[i]
        v = l.split(',')
        gtlines.append([int(v[0]),int(v[1]), int(v[2]),int(v[3]),float(v[4]),float(v[5]),float(v[6]), float(v[7]),float(v[8]), float(v[9])])

    lines = outf.readlines()
    for i in range(len(lines)):
        l=lines[i]
        v = l.split(',')
        outlines.append([int(v[0]),int(v[1]), int(v[2]),int(v[3]),float(v[4]),float(v[5]),float(v[6]), float(v[7]),float(v[8]), float(v[9])])

    b1errf=0 #f=frame
    terrf=0
    b2errf=0
    b1dist_c=0 #c=coordinate
    tdist_c=0
    b2dist_c = 0
    for i,out in enumerate(outlines):
        b1errf = abs(out[1]-gtlines[i][1])
        terrf = abs(out[2]-gtlines[i][2])
        b2errf = abs(out[3]-gtlines[i][3])
        col_err_f.append(b1errf)
        col_err_f.append(b2errf)
        col_err_f.append(terrf)
        b1dist_c = abs(out[5]-gtlines[i][5])#euclidean_distances([[out[4],out[5]]],[[gtlines[i][4],gtlines[i][5]]])
        tdist_c = abs(out[7]-gtlines[i][7]) #euclidean_distances([[out[6],out[7]]],[[gtlines[i][6],gtlines[i][7]]])
        b2dist_c = abs(out[9]-gtlines[i][9])#euclidean_distances([[out[8],out[9]]],[[gtlines[i][8],gtlines[i][9]]])
        col_dist_c.append(b1dist_c)
        col_dist_c.append(b2dist_c)
        col_dist_c.append(tdist_c)
        
    n_reps = len(outlines)
    # print(max(bl))

    # f.write(str(b1errf/n_reps)+","+str(terrf/n_reps)+","+str(b2errf/n_reps)+","+str(b1dist_c/n_reps)+","+str(tdist_c/n_reps)+","+str(b2dist_c/n_reps)+"\n")
f.write(str(col_err_f)+","+str(col_dist_c))
f.close()
print("data write done")
# for l in gtlines:
