import json
import random

# 文件路径
coco_annotation_file = "./COCO/annotations/instances_val2017.json"  # 原始 COCO 注释文件路径
output_annotation_file = "./coco_small/small_coco_dataset.json"  # 输出的小数据集注释文件路径
num_images = 6  # 选择图片数量

# 加载原始 COCO 注释
with open(coco_annotation_file, 'r') as f:
    coco_data = json.load(f)

# 随机选择 num_images 张图片
selected_images = random.sample(coco_data['images'], num_images)
selected_image_ids = {img['id'] for img in selected_images}

# 筛选与所选图片相关的注释
selected_annotations = [
    ann for ann in coco_data['annotations'] if ann['image_id'] in selected_image_ids
]

# 筛选相关类别
selected_category_ids = {ann['category_id'] for ann in selected_annotations}
selected_categories = [
    cat for cat in coco_data['categories'] if cat['id'] in selected_category_ids
]

# 构建小数据集 JSON
small_coco_data = {
    'images': selected_images,
    'annotations': selected_annotations,
    'categories': selected_categories
}

# 保存小数据集注释文件
with open(output_annotation_file, 'w') as f:
    json.dump(small_coco_data, f, indent=4)

print(f"小数据集已生成，保存在 {output_annotation_file}")