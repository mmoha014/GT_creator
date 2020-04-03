import matplotlib.pyplot as plt
import numpy as np

data = list()#np.zeros((3,10))#20))
reps = list()
b1_frame = list()
top_frame = list()
b2_frame = list()
b1x, b2x, b1y,b2y = list(), list(), list(),list()
for i in range(1,11):
    filename = 'BBC'+str(i)
    folder = 'curl'
    #====================== ground truth read ===========================
    # f = open('/home/mgharasu/Videos/Dan videos/'+folder+'/'+filename+'.txt')
    f = open(filename+'.txt')
    gt_reps = []
    gt_B1_frame, gt_Top_frame, gt_B2_frame = list(),list(),list()
    gt_b1x,gt_b1y,gt_b2x,gt_b2y = list(),list(),list(),list()
    gt_dur,gt_vel = list(),list()

    for l in f.readlines():
        v=l.split(',')
        gt_reps.append(int(v[0]))
        gt_B1_frame.append(int(v[1]))
        gt_Top_frame.append(int(v[2]))
        gt_B2_frame.append(int(v[3]))
        gt_b1x.append(float(v[4]))
        gt_b1y.append(float(v[5]))
        gt_b2x.append(float(v[6]))
        gt_b2y.append(float(v[7]))
        gt_dur.append(float(v[8]))
        gt_vel.append(float(v[9]))

    #==================== output read ===================================
    f = open('/home/mgharasu/Documents/Noah_project/alpha2/AlphaPose/gt/out_'+filename+'.txt')
    out_reps = []
    out_B1_frame, out_Top_frame, out_B2_frame = list(),list(),list()
    out_b1x,out_b1y,out_b2x,out_b2y = list(),list(),list(),list()
    out_dur,out_vel = list(),list()
    # total = []
    for l in f.readlines():
        v=l.split(',')
        out_reps.append(int(v[0]))
        out_B1_frame.append(int(v[1]))
        out_Top_frame.append(int(v[2]))
        out_B2_frame.append(int(v[3]))
        out_b1x.append(float(v[4]))
        out_b1y.append(float(v[5]))
        out_b2x.append(float(v[6]))
        out_b2y.append(float(v[7]))
        out_dur.append(float(v[8]))
        out_vel.append(float(v[9]))
        # total.append([int(v[0]),int(v[1]),int(v[2]),int(v[3]),float(v[4]),float(v[5]),float(v[6]),float(v[7]),float(v[8]),float(v[9])])
        

    for i in range(0,len(gt_B1_frame)):
        data.append([abs(gt_B1_frame[i]-out_B1_frame[i]),abs(gt_Top_frame[i]-out_Top_frame[i]),abs(gt_B2_frame[i]-out_B2_frame[i])])
        # data[0][i] = 
        # data[1][i] = 
        # data[2][i] = 

        # data[0][2*i+1] = out_B1_frame[i]
        # data[1][2*i+1] = out_Top_frame[i]
        # data[2][2*i+1] = out_B2_frame[i]

x = np.arange(20)
plt.bar(x, data[0], color='b', width=0.25)
plt.bar(x+.25, data[1], color='g', width=0.25)
plt.bar(x+.5, data[2], color='r', width=0.25)
plt.show()

# columns = ('GT1','OUT1','GT2','OUT2','GT3','OUT3','GT4','OUT4','GT5','OUT5','GT6','OUT6','GT7','OUT7','GT8','OUT8','GT9','OUT9','GT10','OUT10')
# rows = ['rep_startFrame', 'rep_halfFrame', 'rep_endframe']
# index = np.arange(len(columns)) + 0.3
# bar_width = 0.4
# values = np.arange(0, 1000, 10)
# value_increment = 1000
# # Initialize the vertical-offset for the stacked bar chart.
# y_offset = np.zeros(len(columns))
# colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
# n_rows = len(data)

# cell_text = []
# for row in range(n_rows):
#     plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
#     y_offset = y_offset + data[row]
#     cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
# # Reverse colors and text labels to display the last value at the top.
# colors = colors[::-1]
# cell_text.reverse()

# # Add a table at the bottom of the axes
# the_table = plt.table(cellText=cell_text,
#                       rowLabels=rows,
#                       rowColours=colors,
#                       colLabels=columns,
#                       loc='bottom')

# # Adjust layout to make room for the table:
# plt.subplots_adjust(left=0.2, bottom=0.2)

# plt.ylabel("frame ".format(value_increment))
# plt.yticks(values * value_increment, ['%d' % val for val in values])
# plt.xticks([])
# plt.title('ground truth versus output')

# plt.show()
