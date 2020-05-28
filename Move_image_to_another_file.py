import os, os.path
import shutil
import random
import glob
# move a certain mount of pics to another file based on number jinteration. make subfiles at the same time

path = '//DESKTOP-ASB277M/Data_3D/Training/camera_para/'
# save_path = '//DESKTOP-ASB277M/Data_3D/Training/3D_training_data/'
save_path = '//DESKTOP-ASB277M/Data_3D/Testing/'
c = 0
file = 0
if file < 30:
    try:
        for img in os.listdir(path):
            print(img)
            image_select = random.sample(os.listdir(path+'/'+str(img)), 1)

            for image_sel in image_select:
                if os.path.exists(os.path.join(save_path, str(img) + '/')) == False:
                    os.makedirs(os.path.join(save_path, str(img) + '/'))
                if image_sel[-4:] == '.png' and image_sel[-3] != '.db':
                    image = os.path.join(path+str(img)+'/', image_sel)
                    try:
                        print(save_path+ str(img) + '/' + str(image_sel[:-4]), image)
                        shutil.copy(image, save_path+ str(img) + '/' + str(image_sel[:-4]) + ".png")
                        os.remove(image)  # 并删除原有文件
                    except:
                        print('error')
            file = file + 1
    except:
        print('file out of range')



# path = '//DESKTOP-ASB277M/Data_3D/Training/camera_para/'
# # save_path = '//DESKTOP-ASB277M/Data_3D/Training/3D_training_data/'
# save_path = '//DESKTOP-ASB277M/Data_3D/Testing/'
# c = 0
# file = 0
# if file < 10:
#     try:
#         for img in os.listdir(path+'/'+str(file)):
#
#             image_select = random.sample(os.listdir(path+'/'+str(file)), 1)
#
#             for image_sel in image_select:
#                 if os.path.exists(os.path.join(save_path, str(file) + '/')) == False:
#                     os.makedirs(os.path.join(save_path, str(file) + '/'))
#                 if image_sel[-4:] == '.png' and image_sel[-3] != '.db':
#                     image = os.path.join(path+str(file)+'/', image_sel)
#                     try:
#                         print(save_path+ str(file) + '/' + str(image_sel[:-4]), image)
#                         shutil.copy(image, save_path+ str(file) + '/' + str(image_sel[:-4]) + ".png")
#                         # os.remove(image)  # 并删除原有文件
#                     except:
#                         print('error')
#             file = file + 1
#     except:
#         print('file out of range')


# os.remove(os.path.join(img_path, img))  # 并删除原有文件