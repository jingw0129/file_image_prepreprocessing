import os, os.path
import shutil
from PIL import Image
# rider
# path = '//WIN10-1/rider/TrainSampleAuto/cas1/pos/'
# path = '//192.168.199.148/ml/Rider/rider_pos/'
# path = '//XJL/rider/rider/TrainSampleAuto/cas38_new/case1/'
# wheel
# path = '//192.168.199.148/Wheel/cas1/pos/'
# path = '//DESKTOP-ASB277M/pos_from_neg/'
# car
# path = '//192.168.199.148/ml/car/car/cas1/pos/'
# path = '//192.168.199.148/ml/car/car/cas1/pos1_from_yolo/cas1/'
# path = '//192.168.199.148/ml/car/car/cas1/pos1_from_yolo/cas2/'
# rider
# path = '//XJL/negs/'
path = '//WIN10-1/rider/TrainSampleAuto/'
# car
# path = '//192.168.199.148/ml/car/car/TrainSampleAuto/'
# wheel
# path = '//192.168.199.148/Wheel/TrainSampleAuto/cas16/neg/'
new_path = 'E:/NEW_BIG_SAMPLES/Rider/NEG/'
i = 0
j = 0
sub_file =[]
for root_, cas, image in os.walk(path):
    root = os.path.join(path,root_).replace('\\', '/')
    for c in range(len(cas)):
        # print(c)
        if cas[c][:3] == 'cas':
            sub_file.append((cas[c]+ '/neg').replace('\\', '/'))

    for c in range(len(sub_file)):
        for img in image:
            image_path = os.path.join(root,img).replace('\\', '/')
            # print(image_path)
            try:
                if os.path.basename(image_path) != 'Thumbs.db':
                    image_ = Image.open(image_path)
                    width, height = image_.size
                    if width > 32:
                        if not os.path.exists(new_path + sub_file[c]):
                            os.makedirs(new_path + sub_file[c])
                        dst = (new_path + sub_file[c]+'/_' + str(i) + '.png').replace('\\', '/')
                        print(dst)
                        shutil.copy(image_path, dst)
                        i=i+1

            except:
                print(None)


