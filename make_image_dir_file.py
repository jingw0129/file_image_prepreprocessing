import os

coco_dir = 'F:/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/imgs/COCO/val2017/'
image_dir = 'F:/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/imgs/COCO/val2017/'
for co in os.listdir(coco_dir):
    if co[-4:] =='.txt':
        full_path = os.path.join(image_dir,co[:-4]+'.jpg')
        print(full_path)
        with open('F:/PycharmProjects/yolov3-multigpu/data/val.txt','a') as f:
            f.write(full_path+'\n')