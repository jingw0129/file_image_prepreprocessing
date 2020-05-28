import json as json

json_file = 'E:/traversable_region_detection/seg_label/test.json'
# json_file = "E:/traversable_region_detection/LaneNet-master/runs/coord_output/predict_test.json"

f = open(json_file,'r')
data = f.readlines()
for d in data:
    print(d)
    # d_json = json.loads(d)
    # print(d_json)
# json_gt = [json.load(line[1]) for line in json.load(open(json_file))]