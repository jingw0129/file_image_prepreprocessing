import os
import cv2
import tkinter as tk
from tkinter import *

file  = open('C:/Users/win10-zw/Desktop/Faces/FDDB-folds/combination_path/11.txt','r')
data = file.readlines()
number = []
file_paths = {}
for num,line in enumerate(data,1):
    if len(line) <= 4:
        number.append(line[0])
        file_paths[data[num-2]] = num-2
number = number[:-1]
# print(number)
file_paths_ = list(file_paths.keys())
file_path_index = list(file_paths.values())
last_annots_index = [a-b for a,b in zip(list(file_paths.values()), list([1]*len(file_path_index)))]

annots_list = []
image_list = []

for i in range(len(file_path_index)-1):
    # image_path = 'C:/Users/win10-zw/Desktop/Faces/FDDB_images/'+ file_paths_[i].replace("\n","") + '.png'
    image_path = file_paths_[i].replace("\n", "")
    # print(image_path)
    image = cv2.imread(image_path)
    image_list.append(image)
    # print(data[file_path_index[i] : last_annots_index[i+1]+1][2:])
    annots_list.append(data[file_path_index[i] : file_path_index[i+1]][2:])
print(annots_list)
path_to_annots = list(zip(file_paths_, annots_list))
print(len(path_to_annots), len(number))
f_new =  open('new_annots_file.txt', 'a+')

def add_label(event):
    path_to_annots = list(zip(file_paths_, annots_list))
    for line_ in [path_to_annots[j]]:
        check_exist = [str(line_[0])]
        print(check_exist[0])

        if len(data) != 0:
            if check_exist[0] not in data[0]:
                f_new.write(str(line_[0]) + number[j] + '\n')
        else:
            f_new.write(str(line_[0]) + number[j] + '\n')

        for k in range(len(line_[1])):
            # print(line_[1][0])
            if line_[1][k].split() == annot:
                annot.append('others')
                # print(annot)
                line_[1][k] = str(annot)
                f_new.write(str(line_[1][k]) + '\n')


def label_BSD(event):
    path_to_annots = list(zip(file_paths_, annots_list))
    for line_ in [path_to_annots[j]]:
        check_exist = [str(line_[0])]
        print(check_exist[0])

        if len(data) != 0:
            if check_exist[0] not in data[0]:
                f_new.write(str(line_[0]) + number[j] + '\n')
        else:
            f_new.write(str(line_[0]) + number[j] + '\n')

        for k in range(len(line_[1])):
            # print(line_[1][0])
            if line_[1][k].split() == annot:
                annot.append('bsd')
                # print(annot)
                line_[1][k] = str(annot)
                f_new.write(str(line_[1][k]) + '\n')
#
f_new =  open('new_annots_file.txt', 'a+')
for j in range(len(annots_list)):
    for k in range(len(annots_list[j])):

        annot = annots_list[j][k].split()
        print(annot)
        image = image_list[j]
        x = int(annot[0])
        y = int(annot[1])
        w = int(annot[2])
        h = int(annot[3])
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)
        # print(image)
        cv2.imshow('result', image)
        f_new = open('new_annots_file.txt', 'a+')
        data = f_new.readlines()
        if len(data) !=0:
            print(data[0])
        Do1 = tk.Tk()
        Do2 = tk.Tk()
        frame1 = Frame(Do1, width=100, height=100)
        frame2 = Frame(Do2, width=200, height=200)
        frame1.bind('<Button-1>', add_label)
        frame2.bind('<Button-1>', label_BSD)

        frame1.pack()
        frame2.pack()
        Do1.mainloop()
        Do2.mainloop()
        cv2.waitKey(0)


