import os
label_dir = 'C:/Users/iwaywin/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/imgs/COCO/train2017/'
# label_dir = 'C:/Users/iwaywin/PycharmProjects/3D_Car_Detection/3D_Bounding_box/Kitti/testing/testing_result/'
for label in os.listdir(label_dir):
    # print(label[-3:])
    if label[-3:] == 'txt':
        # print(label)
        full_path= os.path.join(label_dir,label)

        file_data = []
        with open(full_path,'r+') as file:
            for line in file.readlines():
                if line == '\n':
                    print('do')
        #             line = line.strip("\n")
        #         file_data.append(line)
        #
        # file1 = open(full_path, 'w')
        # file1.writelines(file_data)
        # file.close()
        # file1.close()