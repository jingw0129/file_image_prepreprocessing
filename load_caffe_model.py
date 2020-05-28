import sys
sys.path.insert(0,'D:/Anaconda3/envs/caffe/caffe-windows/python/')
import caffe
from caffe.proto import caffe_pb2
# caffe_model_pth = 'F:/HiSVP_PC_V1.2.2.0/software/data/detection/yolov3/model/yolov3.caffemodel'
proto_path = 'F:/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/Model_Transfer_Pytorch-to-Caffe/vgg19_bn.prototxt'
caffe_model_pth = 'F:/PycharmProjects/YOLO_pytorch/pytorch-yolo-v3-custom/Model_Transfer_Pytorch-to-Caffe/vgg19_bn.caffemodel'
# caffe_model_pth = 'F:/PycharmProjects/YOLO_pytorch/PyTorch-YOLOv3/yolov3_cus'
net = caffe.Net(proto_path,caffe_model_pth, caffe.TEST)

# W = net.params['layer1-conv'][0].data[...]
# b = net.params['layer1-conv'][1].data[...]
print(net.params.keys())
#
net_param = caffe_pb2.NetParameter()
net_str = open(caffe_model_pth, 'rb').read()

net_param.ParseFromString(net_str)
net_list = [net_param.layer]
print(net_list)
for layer in net_list:
    for la in layer:
        print(la.name) # first layer

print(net_param.layer) # last layer