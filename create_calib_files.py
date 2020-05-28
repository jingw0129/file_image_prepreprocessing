import os
import numpy as np
import math
# # parameters of the camera
based_dir = 'E:/label_2/'
save_dir = 'E:/calib/'
K = np.array([0,637.85, -61.51, 22.2, -42.45, 27.73])
k1 = K[1]
k3 = K[2]
k5 = K[3]
k7 = K[4]
k9 = K[5]
# Cx = 4
# Cy = 4
c_x = 648.33
c_y = 357.42

asp = 1

def power(x, n): #如def power (x,n=2) 设置了n的默认值为2
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# get the index of each number in the matrix
pixel_index_dic = {}
X_correct = []
Y_correct = []
# //print(gray_frame_array[0][1279])
for gr_i in range(1280):
    for gr_j in range(720):

        u = gr_i - 720 / 2
        v = gr_j - 1280 / 2
        phi = np.arctan2(v, u)
        r = np.sqrt(pow(u, 2) + pow(v, 2))
        thita1 = math.pi / 2

        R1 = (k1) * thita1 + (k3) * power(thita1, 3) + (k5) * power(thita1, 5) + (k7) * power(thita1, 7) + (k9) * power(
            thita1, 9)
        f = R1 // thita1
        thita = np.arctan2(r, f)
        R = (k1) * thita + (k3) * power(thita, 3) + (k5) * power(thita, 5) + (k7) * power(thita, 7) + (k9) * power(
            thita, 9)
#

for name in os.listdir(based_dir):
    base_full_path = os.path.join(based_dir,name)
    with  open(save_dir + '/' + name[:-4] + '.txt', 'w') as calib:
        calib.write('P0:'+' '+str(f)+' '+str(0.000000000000e+00) + ' '+ str(c_x) + ' ' + str(0.000000000000e+00) + ' ' + str(0.000000000000e+00)+ ' '+ str(f)+ ' '+ str(c_y)+ ' '+ str(0.000000000000e+00) + ' ' + str(0.000000000000e+00)+' '+ str(0.000000000000e+00)+' '+str(1.000000000000e+00)+' '+ str(0.000000000000e+00))

# if os.path.exists(save_dir + '/' + name) is False:
    #     os.makedirs(save_dir + '/' + name)
    # i = 0
    # for sub_name in os.listdir(base_full_path):
    #     i = i+1
    #     print(i, sub_name[:-4])
    #