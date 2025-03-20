import json

# 1. 加载JSON文件
with open('testval_voc07_seen.json', 'r') as f:
    seen_data = json.load(f)
with open('testval_voc07_unseen.json', 'r') as f:
    unseen_data = json.load(f)

# 2. 合并类别
# seen_data类别ID保持1-16
# unseen_data类别ID调整为17-20
for cat in unseen_data['categories']:
    cat['id'] += 16
merged_categories = seen_data['categories'] + unseen_data['categories']

# unseen_data类别ID调整为17-20
for img in unseen_data['images']:
    img['id'] += len(seen_data['images'])# 4836

merged_images = seen_data['images'] + unseen_data['images']

# 4. 合并标注
for ann in unseen_data['annotations']:
    ann['category_id'] += 16
    ann['image_id'] += len(seen_data['images'])
    ann['id'] += len(seen_data['annotations']) # 15099
merged_annotations = seen_data['annotations'] + unseen_data['annotations']

# 5. 创建合并数据
merged_data = {
    'images': merged_images,
    'annotations': merged_annotations,
    'categories': merged_categories
}

# 6. 保存到新文件
with open('testval_voc07_unseen_seen_all_gzsd.json', 'w') as f:
    json.dump(merged_data, f, indent=4)

print("合并完成，已保存为 'merged_testval_voc07.json'")