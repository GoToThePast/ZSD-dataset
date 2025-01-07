import json
import os
import csv
from PIL import Image

# 设置类别
# VOC 可见类
# categories = [
#     "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "cat", "chair", "cow", "diningtable",
#     "horse", "motorbike", "person", "pottedplant", "sheep", "tvmonitor"
# ]
# VOC 未见类
# categories = [
#     "car", "dog", "sofa", "train"
# ]
# COCO 65/15 可见类未见类混合，其中没有可见类中的'zebra' 79
# categories=[
#     'person', 'bicycle', 'car', 'motorcycle', 'bus', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'bench',
#     'bird', 'dog', 'horse', 'sheep', 'cow', 'elephant',
#
#     'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'skis',
#     'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass',
#     'cup', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'orange', 'broccoli', 'carrot', 'pizza', 'donut', 'cake', 'chair', 'couch',
#     'potted plant', 'bed', 'dining table', 'tv', 'laptop', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'sink',
#     'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'toothbrush',
#     'airplane', 'train', 'parking meter', 'cat', 'bear', 'suitcase', 'frisbee', 'snowboard', 'fork', 'sandwich', 'hot dog',
#     'toilet', 'mouse', 'toaster', 'hair drier'
# ]
# COCO 65/15 可见类 65
categories=[
    'person', 'bicycle', 'car', 'motorcycle', 'bus', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'bench',
    'bird', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'skis',
    'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass',
    'cup', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'orange', 'broccoli', 'carrot', 'pizza', 'donut', 'cake', 'chair', 'couch',
    'potted plant', 'bed', 'dining table', 'tv', 'laptop', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'sink',
    'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'toothbrush'
]
# COCO 65/15 未见类 15
# categories=[
#     'airplane', 'train', 'parking meter', 'cat', 'bear', 'suitcase', 'frisbee', 'snowboard', 'fork', 'sandwich', 'hot dog',
#     'toilet', 'mouse', 'toaster', 'hair drier'
# ]




# 创建类别映射（类别名称 -> 类别ID）
category_map = {category: idx + 1 for idx, category in enumerate(categories)}

# 读取CSV注释文件
file_name='train_coco_seen_all.csv'
# csv_file = './VOCdevkit/ZSDAnnotations/'+file_name
csv_file = './coco/ZSDAnnotations/65_15/csv/'+file_name
images = []
annotations = []
image_id = 0
count = 0
annotation_id = 0
print(csv_file)
# 打开并读取CSV文件
with open(csv_file, 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        is_exist = False
        image_path, x_min, y_min, x_max, y_max, category_name = row
        x_min, y_min, x_max, y_max = map(int, [x_min, y_min, x_max, y_max])
        # VOC数据集：将../../Dataset/VOC2007/JPEGImages/000006.jpg 转换为 ./VOCdevkit/VOC2007/JPEGImages/000006.jpg
        # image_path = image_path.replace('../../Dataset', './VOCdevkit')
        # COCO数据集：
        image_path ="./coco/" + image_path

        # 处理图片
        image_filename = os.path.basename(image_path)
        for image in images:
            if image['file_name'] == image_filename:
                image_id = image['id']
                is_exist = True
                break

        if not is_exist:
            count += 1
            image_id = count
            image = Image.open(image_path)
            width, height = image.size
            # 添加图片信息
            images.append({
                "id": image_id,
                "file_name": image_filename,
                "width": width,
                "height": height
            })

            # count每1000张图片输出一次
            if count % 1000 == 0:
                print(f"已处理{count}张图片")

        # 处理注释
        category_id = category_map[category_name]
        annotations.append({
            "id": annotation_id + 1,
            "image_id": image_id,
            "category_id": category_id,
            "bbox": [x_min, y_min, x_max - x_min, y_max - y_min],
            "area": (x_max - x_min) * (y_max - y_min),
            "iscrowd": 0
        })
        annotation_id += 1

        # annotation_id每10000个输出一次
        if annotation_id % 5000 == 0:
            print(f"已处理{annotation_id}个注释")



# 构建COCO格式的字典
coco_format = {
    "images": images,
    "annotations": annotations,
    "categories": [{"id": i + 1, "name": category, "supercategory": category} for i, category in enumerate(categories)]
}

# 保存为JSON文件
with open(file_name.replace('.csv','.json'), 'w') as json_file:
    json.dump(coco_format, json_file, indent=4)

print("转换完成，已保存为"+file_name.replace('.csv','.json'))


