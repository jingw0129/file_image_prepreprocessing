import cv2
import os
import numpy as np
import random
import math
import glob
from os.path import isfile, join
import os.path as ops

video_paths = '//192.168.199.148/Videos/'

output_image_path = '//DESKTOP-ASB277M/Data_3D/Training/'
if os.path.exists(output_image_path) is False:
    try:
        os.makedirs(output_image_path, exist_ok=True)
    except:
        print('already exists')

video_path_list = []
for video_path in os.listdir(video_paths):
    if 'combine' in video_path or 'conbine' in video_path:
        video_path_list.append(os.path.join(video_paths,video_path))
video_path_list = random.choices(video_path_list,k = 25)
print(len(video_path_list))

file = 2
file_number=0
for video_list in video_path_list:
    for video in os.listdir(video_list):
        video_dir = os.path.join(video_list+'/', video)
        if video_dir[-4:]=='.avi':
            print(video_dir)
            vc = cv2.VideoCapture(video_dir)
            c = 0
            if vc.isOpened():#判断是否正常打开
                rval,frame = vc.read()
            else:
                rval = False
            timeF = 80 #视频帧计数间隔频率
            while rval: #循环读取视频帧
                rval,frame = vc.read()
                if (c%timeF == 0):
                    try:
                        os.makedirs(os.path.join(output_image_path, str(file) + '/'))
                    except:
                        print('file has been made')
                    print(os.path.join(output_image_path, str(file)+'/'+video[:-4] + '_' +str(file_number)+'.png'))
                    if os.path.exists(video[:-4] + '_' +str(file_number)+'.png') is False:
                        cv2.imwrite(output_image_path+str(file)+'/'+video[:-4] +'_'+str(file_number)+'.png',frame)
                        # print('here')
                        file_number = file_number+1
                        if file_number > 5000:
                            file_number = 0
                            try:
                                file = file + 1
                                os.makedirs(os.path.join(output_image_path, str(file) + '/'))
                            except:
                                print('exist')
                c = c + 1



            cv2.waitKey(1)
            vc.release()