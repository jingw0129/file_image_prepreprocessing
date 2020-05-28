import os
import shutil
# based_dir1 = 'D:/3DTest/camera_para/image_label/'
# based_dir2 = 'D:/3DTest/camera_para/camera_para/'
#
# for b1 in os.listdir(based_dir1):
#     for b2 in os.listdir(based_dir2):
#         if b1 == b2:
#             full1 = os.path.join(based_dir1, b1)
#             full2 = os.path.join(based_dir2, b2)
#
#             labels = os.listdir(full1)
#             images = os.listdir(full2)
#             # print(images)
#             for img in images:
#                 if img[:-4]+'.txt' not in labels:
#                     if img[-4:] != '.txt':
#                         os.remove(os.path.join(full2,img))
#                         print(img[:-4]+'.txt' + '\n')


based_dir1 = 'C:/Users/iwaywin/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/labels/labels/val2017/'
based_dir2 = 'C:/Users/iwaywin/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/imgs/COCO/val2017/'

labels = []
for b1 in os.listdir(based_dir1):
    labels.append(b1)
    # print(labels)
i = 0
for b2 in os.listdir(based_dir2):
    images = os.path.join(based_dir2, b2)
    # print(labels, images)
    if b2[:-4]+'.txt' not in labels and b2[:-4]!='txt':
        i=i+1
        shutil.move(images,'C:/Users/iwaywin/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/imgs/COCO/val_backup/')
        # os.remove(images)
        print(images+ '\n')
print(i)