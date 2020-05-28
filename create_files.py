import os
import shutil
from PIL import Image


des_path = 'E:/NEW_BIG_SAMPLES/Car/NEG/'
# dst = os.path.join(os.path.abspath(new_path), '1_' + str(i) + '.png')
# new_path = []
# c = 3
for c in range(2,4):
    os.makedirs(os.path.join(os.path.abspath(des_path), 'cas' + str(c) +'/neg'))
    # new_path.append(os.path.join(os.path.abspath(des_path), 'cas' + str(c) +'/neg'))
    # c = c+1