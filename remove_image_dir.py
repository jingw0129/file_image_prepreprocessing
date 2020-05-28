import os
label_dir = 'C:/Users/iwaywin/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/labels/labels/train2017/'
image_dir = 'C:/Users/iwaywin/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/data/'
labels = []
for label in os.listdir(label_dir):
   labels.append(label[:-4])
# print(labels)
# for image in os.listdir(image_dir):
#     full_path = os.path.join(image_dir, image)
file_data = []
with open(image_dir+'train.txt','r+') as file:
    for line in file:
        cate = line.split("/")[-1][:-5]
        # print(cate)
        if cate in labels:
            print(line)
            file_data.append(line+'\n')
file.close()
file = open(image_dir+'train.txt', 'w')
file.writelines(file_data)
file.close()
