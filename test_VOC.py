import os
import xml.etree.ElementTree as ET

def remove_images_by_classes(voc_path, classes_to_remove):
    # 路径到Annotations文件夹
    annotations_path = os.path.join(voc_path, 'Annotations')
    image_sets_path = os.path.join(voc_path, 'ImageSets', 'Main')

    # 获取训练集（train.txt）中的所有图片ID
    train_file = os.path.join(image_sets_path, 'train.txt')
    image_ids = set()
    with open(train_file, 'r') as f:
        for line in f:
            image_ids.add(line.strip())

    # 记录去除的图片数
    removed_count = 0

    # 遍历所有训练集图片ID并检查类别
    remaining_image_ids = set()
    for image_id in image_ids:
        annotation_file = os.path.join(annotations_path, image_id + '.xml')
        if not os.path.exists(annotation_file):
            continue

        tree = ET.parse(annotation_file)
        root = tree.getroot()

        # 获取所有object标签
        found = False
        for obj in root.iter('object'):
            class_name = obj.find('name').text
            if class_name in classes_to_remove:
                found = True
                break

        if not found:
            remaining_image_ids.add(image_id)
        else:
            removed_count += 1

    # 返回剩余的图片数量
    return len(remaining_image_ids), removed_count

# PASCAL VOC 2007和2012的路径
voc2007_path = './VOCdevkit/VOC2007'
voc2012_path = './VOCdevkit/VOC2012'

# 我们要去除的类别
classes_to_remove = {'car', 'dog', 'sofa', 'train'}

# 计算去除后的图片数
remaining_2007, removed_2007 = remove_images_by_classes(voc2007_path, classes_to_remove)
remaining_2012, removed_2012 = remove_images_by_classes(voc2012_path, classes_to_remove)

# 输出去除后的总和
print(f"VOC2007剩余图片数量: {remaining_2007}")
print(f"VOC2012剩余图片数量: {remaining_2012}")
print(f"总共去除的图片数量: {removed_2007 + removed_2012}")
