import csv
# read image
import cv2
import matplotlib.pyplot as plt
import os
import os.path
# image_path = '//192.168.199.148/ml/car/side_view/car_side_view_pos1/'
image_path = 'E:/rider_image/bridge_image_neg_for_selecting/'
# save_path = '//192.168.199.148/ml/Rider/rider_neg/rider_negs_9/'
save_path = '//192.168.199.148/ml/Rider/rider_neg/rider_negs10/'
size_crop = 40
# os.remove('//192.168.199.148/ml/LaneSample/NEG3/Thumbs.db')
c = 0
file = 4
for img in os.listdir(image_path):
    # print(img[-4:])
    if img[-4:] == '.png':
        full_path = os.path.join(image_path,img)
        # img = cv2.imread(full_path)
        # cropped = img[0:60, 0:60]
        # cv2.imwrite(save_path + "cropped_" + str(c) + ".png", cropped)
        # c=c+1
        image = os.path.join(image_path, img)
        print(image)
        image = cv2.imread(image)
        try :
            H = image.shape[0]
            W = image.shape[1]
            for j in range(int(H/2), int(H),size_crop):
                for i in range(0,W,size_crop):
                    cropped = image[j:j+size_crop,i:i+size_crop]
                    h = cropped.shape[0]
                    w = cropped.shape[1]
                    if os.path.exists(os.path.join(save_path, str(file) + '/')) == False:
                        os.makedirs(os.path.join(save_path, str(file) + '/'))
                    if h >=size_crop and w >= size_crop:
                        cv2.imwrite(save_path + str(file) + '/' + "rider" + str(c) + ".png", cropped)
                        c = c + 1
                    if c > 1000:
                        c = 0
                        try:
                            file = file + 1
                            os.makedirs(os.path.join(save_path, str(file) + '/'))
                        except:
                            print('exist')

        except:
            print(None)

