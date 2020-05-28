import os
path = 'E:/high_low_beam/blue/low/'
# path = 'D:/SVM/demo/test/FDDBimages/'
# path = 'C:/Users/win10-zw/Desktop/myFile/frames/my_frames/'
# path = 'D:/frames/my_frames/'
# path = 'D:/SVM/demo/face/face_testing_image/'

i = 1
for filename in os.listdir(path):
    dst ="low" + str(i) + ".png"
    src =path+ filename
    dst =path+ dst

    # rename() function will
    # rename all the files
    os.rename(src, dst)
    i += 1

# from PIL import Image
# import os, glob
#
#
# def batch_image(in_dir, out_dir):
#     if not os.path.exists(out_dir):
#         print(out_dir, 'is not existed.')
#         os.mkdir(out_dir)
#
#     if not os.path.exists(in_dir):
#         print(in_dir, 'is not existed.')
#         return -1
#     count = 0
#     # for files in glob.glob(in_dir + '/*'):
#     for dirpath, dirs, files in os.walk(in_dir):
#         print(dirpath, dirs, files)
#         filepath, filename = os.path.split(files)
#
#         out_file = filename[0:9] + '.png'
#         # print(filepath,',',filename, ',', out_file)
#         im = Image.open(files)
#         new_path = os.path.join(out_dir, out_file)
#         print(count, ',', new_path)
#         count = count + 1
#         im.save(os.path.join(out_dir, out_file))
#
# # file = '//DESKTOP-ASB277M/Users/iwaywin/Downloads/CarData/TrainImages/'
# path = 'C:/Users/win10-zw/PycharmProjects/Lane_detection_CNN/data/tusimple_test_image/test_set/clips/'
# targetDir = 'C:/Users/win10-zw/PycharmProjects/Lane_detection_CNN/data/tusimple_test_image/test_set_/'
# if __name__ == '__main__':
#     batch_image(path, targetDir)


# import cv2
# import os
# import numpy as np
# from matplotlib import pyplot as plt
# import math
# import glob
# from os.path import isfile, join
# import os.path as ops
# # from show_image import demo
# # import cv2
# # Read video as frames and seperate as training ans testing
# # video_path = 'C:/Users/win10-zw/Desktop/myFile/FeigeDownload/LaneChange2/'
# # video_path = 'C:/Users/win10-zw/Desktop/'
# # video_path = "C:/Users/win10-zw/Desktop/myFile/"
# # video_path = '//192.168.199.148/Videos/20180828Video(Company_camera8125)_conbine/'
# # video_path = '//192.168.199.148/Videos/20180809Video(Company_camera9125)_conbine/'
# # video_path = '//192.168.199.148/Videos/VIDEO-CIF-Conbine/'
# video_path = '//192.168.199.148/videos4/0904-dongbei-night-combineXX/'
#
# output_image_path = 'D:/frames/'
#
# # output_image_path = 'D:/SVM/demo/Car/test/car_test/'
# os.makedirs(output_image_path, exist_ok=True)
#
# # video_path_in = 'C:/Users/win10-zw/Desktop/myProject/lanenet_lane_detection_master/data/outputdata/outputdata/'
# files = glob.glob(os.path.join(video_path, '*.ts'))
# files = [f for f in os.listdir(video_path) if isfile(join(video_path, f))]
# #for sorting the file names properly
# files.sort(key = lambda x: x[5:-4])
# files.sort()
# a = []
# for i in range(len(files)):
#     filename=video_path + files[i]
# #     print(filename)
#     #reading each files
#     vc = cv2.VideoCapture(filename)
# #     print(vc)
#     c = 1
#     if vc.isOpened():#判断是否正常打开
#
#         rval,frame = vc.read()
#     else:
#         rval = False
#     timeF = 40 #视频帧计数间隔频率
#
#     while rval: #循环读取视频帧
#         rval,frame = vc.read()
#         if (c%timeF == 0):
#             cv2.imwrite(output_image_path+'night5_' +str(c)+'.png',frame)
#
#         c = c + 1
#         cv2.waitKey(1)
#     vc.release()