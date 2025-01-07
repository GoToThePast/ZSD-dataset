import json
import os
from PIL import Image

# 类别列表
categories = [
    'toilet', 'bicycle', 'apple', 'train', 'laptop', 'carrot', 'motorcycle', 'oven', 'chair', 'mouse', 'boat',
    'kite', 'sheep', 'horse', 'sandwich', 'clock', 'tv', 'backpack', 'toaster', 'bowl', 'microwave', 'bench',
    'book', 'orange', 'bird', 'pizza', 'fork', 'frisbee', 'bear', 'vase', 'toothbrush', 'spoon', 'giraffe',
    'handbag', 'broccoli', 'refrigerator', 'remote', 'surfboard', 'car', 'bed', 'banana', 'donut', 'skis',
    'person', 'truck', 'bottle', 'suitcase', 'zebra', 'background'
]

# 创建类别映射（类别名称 -> 类别ID）
category_map = {category: idx + 1 for idx, category in enumerate(categories)}

# 读取CSV注释文件
file_name='mscoco_train_list.json'
json_file = './coco/ZSDAnnotations/48_17/csv/'+file_name
images = []
annotations = []
image_id = 0
count = 0
annotation_id = 0
print(json_file)
# 打开并读取json文件
with open(json_file, 'r') as file:
    train_data = json.load(file)
    for entry in train_data:
        is_exist = False
        image_info=entry['img_name']
        # 处理类别（去除.n.01）
        category_name = entry['synset'].split('.')[0]
        x_min, y_min, x_max, y_max = entry['box']
        # 转化为整数
        x_min, y_min, x_max, y_max = map(int, [x_min, y_min, x_max, y_max])
        # 图片名称
        image_filename = os.path.basename(image_info)
        # 图片路径
        image_path ="./coco/train2014/" + image_filename


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
with open("raw_"+file_name, 'w') as json_file:
    json.dump(coco_format, json_file, indent=4)

print("转换完成，已保存为"+file_name)
