import json

# 文件路径
coco_annotations_path = "./coco/annotations/instances_train2014.json"  # 官方COCO注释文件路径
img_list_path = "./coco/ZSDAnnotations/48_17/csv/mscoco_train_list.txt"  # 包含目标图片文件名的文件路径
output_coco_path = "mscoco_train_list.json"  # 输出的COCO注释文件路径
categories = set()
print("start")
# 读取train_list.txt中的目标图片文件名
with open(img_list_path, "r") as f:
    target_filenames = [line.strip() for line in f if line.strip()]

# 读取COCO注释文件
with open(coco_annotations_path, "r") as f:
    coco_data = json.load(f)

# 初始化新的COCO注释集
filtered_coco_data = {
    "images": [],
    "annotations": [],
    "categories": coco_data["categories"]
}

# 创建目标图片的ID集合
target_image_ids = set()
for img in coco_data["images"]:
    if img["file_name"] in target_filenames:
        filtered_coco_data["images"].append(img)
        target_image_ids.add(img["id"])

print("图片ID集合创建成功")

# 提取目标图片ID相关的标注信息
for ann in coco_data["annotations"]:
    # if ann["image_id"] in target_image_ids and ann["category_id"] in [28, 21, 47, 6, 76, 41, 18, 63, 32, 36, 81, 22, 61, 87, 5, 17, 49]:
    if ann["image_id"] in target_image_ids:
        filtered_coco_data["annotations"].append(ann)
        categories.add(ann["category_id"])

print("标注ID集合创建成功")

# 保存新的COCO注释文件
with open(output_coco_path, "w") as f:
    json.dump(filtered_coco_data, f, indent=4)

print(f"生成新的COCO注释文件成功: {output_coco_path}")

# 根据categories中的id,输出对应的类别名称
for id in categories:
    for category in filtered_coco_data["categories"]:
        if category["id"] == id:
            print(category["name"])
# 输出类别数量
print("categories=", len(categories))
