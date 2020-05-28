# import os
#
# label_dir = 'F:/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/imgs/COCO/train2017/'
# # label_dir = 'C:/Users/iwaywin/PycharmProjects/3D_Car_Detection/3D_Bounding_box/Kitti/testing/testing_result/'
#
# category_list = [0,1,2,3,5]
# # category_list = ['car']
# for label in os.listdir(label_dir):
#     if label[-4:] == '.txt':
#         full_path= os.path.join(label_dir,label)
#         # print(full_path)
#         file_data = []
#         with open(full_path,'r+') as file:
#             for line in file:
#                 cate = line.split(" ")[0]
#                 box = line[1:]
#                 # print(cate, box)
#                 if int(cate) in category_list:
#                     # for i in range(len(id)):
#                     #     cate = id[i]
#                     # print(line)
#                     file_data.append(str(cate)+ box )
#         print(file_data)
#         file.close()
#         file = open(full_path, 'w')
#         file.writelines(file_data)
#         file.close()
#


import os
label_dir = 'F:/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/imgs/COCO/val2017/'
# label_dir = 'C:/Users/iwaywin/PycharmProjects/3D_Car_Detection/3D_Bounding_box/Kitti/testing/testing_result/'
category_list = ['2','3','4','6','7','8']
id = [0,1,2,3,4,5]
# category_list = ['car']
for label in os.listdir(label_dir):
    if label[-4:] == '.txt':
        # print(label)
        full_path= os.path.join(label_dir,label)
        # if os.path.getsize(full_path) == 0:
        #     print(full_path)
        #     os.remove(full_path)
        file_data = []
        with open(full_path,'r+') as file:
            for line in file:
                cate = line.split(" ")[0]
                box = line[1:]
                # print(cate)
                if int(cate) in id:
                    if int(cate) == 5:
                        cate = id[4]
                        # print(cate)
                    # elif cate == '0':
                    #     cate = id[0]
                    # elif cate == '1':
                    #     cate = id[1]
                    # elif cate == '2':
                    #     cate = id[2]
                    # elif cate == '3':
                    #     cate = id[3]
                    # elif cate == '8':
                    #     cate = id[5]

                    file_data.append(str(cate)+ box )
        print(file_data)
        file.close()
        file = open(full_path, 'w')
        file.writelines(file_data)
        file.close()
