import cv2
import numpy as np
import os
from os.path import isfile, join

pathIn = '//DESKTOP-ASB277M/Users/iwaywin/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/imgs/COCO/val2017_/'
pathOut = '//DESKTOP-ASB277M/Users/iwaywin/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/video.avi'
fps = 0.5
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
# for sorting the file names properly
files.sort(key=lambda x: x[5:-4])
files.sort()
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
# for sorting the file names properly
files.sort(key=lambda x: x[5:-4])
for i in range(len(files)):
    filename = pathIn + files[i]
    print(filename)
    # reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    # inserting the frames into an image array
    frame_array.append(img)
out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
print(frame_array)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()