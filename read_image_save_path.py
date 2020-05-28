import os
outer_path = '//XJL/People_xjl/'
new_path = 'C:/Users/win10-zw/PycharmProjects/Lane_detection_CNN/data/tusimple_test_image/test_set_/'

folderlist = os.listdir(outer_path)  # 列举文件夹
print(folderlist)
for folder in folderlist:
    if folder.endswith('.avi'):
        inner_path = os.path.join(outer_path, folder)
        print(inner_path)
#     total_num_folder = len(folderlist)  # 文件夹的总数
#     print('total have %d folders' % (total_num_folder))  # 打印文件夹的总数
#
#     # filelist = os.listdir(inner_path)  # 列举图片
#     # print(filelist)
#     i = 0
#     for item in filelist:
#         total_num_file = len(filelist)  # 单个文件夹内图片的总数
#         if item.endswith('.avi'):
#             src = os.path.join(os.path.abspath(inner_path), item)  # 原图的地址
#             dst = os.path.join(os.path.abspath(new_path), str(folder) + '_' + str(i) + '.png')  # 新图的地址（这里可以把str(folder) + '_' + str(i) + '.jpg'改成你想改的名称）
#             try:
#                 os.rename(src, dst)
#                 print('converting %s to %s ...' % (src, dst))
#                 i += 1
#             except:
#                 continue
#     print('total %d to rename & converted %d jpgs' % (total_num_file, i))


# import  os
# import os.path
# import shutil
# import time,  datetime
# # path = 'C:/Users/win10-zw/Desktop/Faces/FDDB_images/'
# # path = '//192.168.199.148/ml/car/car/TrainSampleAuto/'
# path = 'C:/Users/win10-zw/PycharmProjects/Lane_detection_CNN/data/tusimple_test_image/clips/'
# targetDir = 'C:/Users/win10-zw/PycharmProjects/Lane_detection_CNN/data/tusimple_test_image/sample/'
#
# def moveFileto(sourceDir,  targetDir):
#     shutil.copy(sourceDir,  targetDir)
#
#
# # outfile = open('test_image_path.txt', 'a')                          # 以追加方式打开输出文件
# n = 0
# for dirpath, dirs, files in os.walk(path):                # 递归遍历当前目录和所有子目录的文件和目录
#     i = 0
#     for name in files:
#         print(name)# files保存的是所有的文件名
#         if os.path.splitext(name)[1] == '.':
#             n=n+1
#             filename = os.path.join(dirpath, name)       # 加上路径，dirpath是遍历时文件对应的路径
#             filename = filename.replace('\\', '/')
#             name = name.replace('\\', '/')
#             print(filename)
#             # moveFileto(filename,  targetDir)
# #             # os.remove(filename)
# #             dst = "1" + str(i) + ".png"
# #             src = targetDir
# #             dst = os.path.dirname(targetDir) + '/'+ dst
# #             print(dst)
# #             os.rename(src, dst)
# #             i+=1
# #
# #             print(filename)
# #             # f = open(filename, 'r')
# #             # guid = f.readlines()[1].split(': ')[1]       # 获取文件第二行以': '分割的后者
#             outfile.write('/home/ai/PIC_CAR/' + name + "\n")                          # 写入输出文件
#             # f.close()
# # # print(n)
# outfile.close()
#
