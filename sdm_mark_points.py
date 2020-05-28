# get points by clicking the mouse
import glob
import os
from os.path import isfile, join
import cv2
import csv

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a.append([x,y])
#         b.append(y)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img)
        return a

a = []
image_path_in = '//Desktop-asb277m/SDM_Frames/'
files = glob.glob(os.path.join(image_path_in, '*.png'))


files = [f for f in os.listdir(image_path_in) if isfile(join(image_path_in, f))]

#for sorting the file names properly
files.sort(key = lambda x: x[5:-4])
files.sort()
print(files)

file_name_ = []
img_array = []

for i in range(len(files)):
    if os.path.splitext(files[i])[1] == '.png':

        filename=image_path_in + files[i]
        file_name_.append(filename)
    #     reading each files
        img = cv2.imread(filename)
        print(img)
        img_array.append(img)
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
        cv2.imshow("image", img)

#     while (True):
#         try:
#             cv2.waitKey(100)
#         except Exception:
#             cv2.destroyAllWindows()
#             break

    cv2.waitKey(0)
cv2.destroyAllWindows()



with open("output_xy1.csv", "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerows(a)
p = []
for i in range(0,len(a),4):
    p.append(a[i:i+4])

name_coors_dic = dict(zip(file_name_, p))
with open("name_xy.csv", "w", newline="") as f:
    for keys in name_coors_dic.keys():
        f.write("%s,%s\n"%(keys,name_coors_dic[keys]))