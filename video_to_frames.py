import cv2
import os
import numpy as np

import math
import glob
from os.path import isfile, join
import os.path as ops
# from show_image import demo
# import cv2
# Read video as frames and seperate as training ans testing

video_path = 'E:/rider_image/bridge_pier/'

# output_image_path = '//Xjl/sample1/'
output_image_path = 'E:/rider_image/bridge_image/'
os.makedirs(output_image_path, exist_ok=True)


files = glob.glob(os.path.join(video_path, '*.ts'))
files = [f for f in os.listdir(video_path) if isfile(join(video_path, f))]
# print(files)
#for sorting the file names properly
files.sort(key = lambda x: x[5:-4])
files.sort()
a = []
print('here')
for i in range(len(files)):
    filename=video_path + files[i]
    print(filename)
#     #reading each files
    vc = cv2.VideoCapture(filename)
    print(vc)
    c = 1
    if vc.isOpened():#判断是否正常打开

        rval,frame = vc.read()
    else:
        rval = False
    timeF = 30 #视频帧计数间隔频率

    while rval: #循环读取视频帧
        rval,frame = vc.read()
        if (c%timeF == 0):
            # if c > 10000:
            cv2.imwrite(output_image_path+'beam' +str(c)+'.png',frame)
                # print('here')
        c = c + 1

    cv2.waitKey(1)
    vc.release()