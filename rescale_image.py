import os
from PIL import Image
import cv2
import numpy as np
ext = ['.jpg', '.jpeg', '.png']
# files = os.listdir('.')
files = 'D:/SVM/demo/Car/test/test/'

# def process_image(c, filename, mwidth=1280, mheight=720):


c = 1
for filename in os.listdir(files):
    if os.path.splitext(filename)[1]in ext:
        filename = os.path.join(files,filename)
        print(filename)
        image = Image.open(filename)
        w, h = image.size
        # print(w,h)


        scale = 1.0
        new_im = image.resize((640,360), Image.ANTIALIAS)
        new_im = np.array(new_im)
        b,g,r = cv2.split(new_im)
        new_im = cv2.merge([r,g,b])
        cv2.imwrite('D:/SVM/demo/Car/test/testing_inter/' + 'testing_' + str(c) + '.png', new_im)
        c += 1
        print('ok')
        # new_im.close()

