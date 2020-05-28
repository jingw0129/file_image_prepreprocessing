import os, os.path
import shutil
from PIL import Image
# rider
# path = '//WIN10-1/rider/cas1/pos/'
# path = '//192.168.199.148/ml/Rid/er/rider_pos/'
# path = '//XJL/rider/rider/TrainSampleAuto/cas38_new/case1/'
# wheel
# path = '//192.168.199.148/Wheel/TrainSampleAuto/cas1/pos/'
# path = '//DESKTOP-ASB277M/pos_from_neg/'
# car
# path = '//192.168.199.148/ml/car/car/cas1/pos/'
# path = '//192.168.199.148/ml/car/car/cas1/pos1_from_yolo/cas1/'
# path = '//192.168.199.148/ml/car/car/cas1/pos1_from_yolo/cas2/'
# rider
# path = '//XJL/negs/'
# path = '//WIN10-1/rider/TrainSampleAuto/'
# car
# path = '//192.168.199.148/ml/car/car/TrainSampleAuto/'
# wheel
path = '//192.168.199.148/Wheel/TrainSampleAuto/cas18/neg/'
new_path = '//192.168.199.148/NEW_samples_largger/Wheel/neg/cas18/neg/'
i = 0
j = 0

for root, _, files in os.walk(path):
    root = root.replace('\\', '/')
    # if os.path.basename(root) == 'neg':
    #     print(root)
    for f in files:
        fullpath = os.path.join(root, f)
        if os.path.basename(fullpath) != 'Thumbs.db':
            # os.remove(fullpath)
            # print(fullpath)
            fullpath = fullpath.replace('\\', '/')
            j = j+1
            img = Image.open(fullpath)
            width, height = img.size
            try:
                # if os.path.getsize(fullpath) >= 64 * 64:   #set file size in kb
                if width >= 32:
                    dst = os.path.join(os.path.abspath(new_path), '1_' + str(i) + '.png')
                    # print(dst)
                    shutil.copy(fullpath, dst)
                    i = i + 1
                    print(fullpath)

            except WindowsError:
                print("Error" + fullpath)
print(i, j)
# # i = 0
# # for root, _, files in os.walk("//192.168.199.148/ml/LaneSample/laneneg_over6060_1/"):
# #     for f in files:
# #         fullpath = os.path.join(root, f)
# #         print(fullpath)
# #         # os.remove('//192.168.199.148/ml/LaneSample/lane_neg_big_1/Thumbs.db')
