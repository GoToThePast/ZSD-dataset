import json

coco = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train',
        'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign',
        'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep',
        'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella',
        'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard',
        'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard',
        'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork',
        'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange',
        'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair',
        'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv',
        'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave',
        'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase',
        'scissors', 'teddy bear', 'hair drier', 'toothbrush']

# 读取'./coco/ZSDAnnotations/48_17/seen_classes.txt'
# with open('./coco/ZSDAnnotations/48_17/seen_classes.txt', 'r') as f:
#     seen_classes = f.read().splitlines()
indexs = [28, 21, 47, 6, 76, 41, 18, 63, 32, 36, 81, 22, 61, 87, 5, 17, 49]
# 将indexs从小到大排序
indexs.sort()
with open("./coco/annotations/instances_val2017.json", "r") as f:
    coco_data = json.load(f)

unseen_classes = []
unseen_classes_id = []
for id in indexs:
    for category in coco_data["categories"]:
        if category["id"] == id:
            unseen_classes.append(category["name"])
            unseen_classes_id.append(category["id"])
            break

print(unseen_classes)
print(unseen_classes_id)
print(indexs)
# 保存coco为txt
with open('./coco/ZSDAnnotations/48_17/unseen_classes.txt', 'w') as f:
    for i in unseen_classes:
        f.write(i + '\n')
