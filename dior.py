import os
import xml.etree.ElementTree as ET


# 读取./dior/ImageSets/Main/trainval.txt所有数据，并根据读取的数据加上.xml作为文件名,从./dior/Annotations中加载xml

def read_txt(txt_path):
    with open(txt_path, 'r') as f:
        lines = f.readlines()
    return lines


def read_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    return root


# 划分可见类与未见类
def main():
    txt_path = './dior/ImageSets/Main/test.txt'
    unseen_classes = ['airport', 'basketballcourt', 'groundtrackfield', 'windmill']
    lines = read_txt(txt_path)
    seen_list = []
    unseen_list = []
    for line in lines:
        xml_path = os.path.join('./dior/Annotations/Horizontal Bounding Boxes', line.strip() + '.xml')
        root = read_xml(xml_path)
        classes_found = [obj.find('name').text.lower() for obj in root.findall('object')]
        # 检查classes_found是否有unseen_classes中的至少一个类别
        if any([c in classes_found for c in unseen_classes]):
            unseen_list.append(line.strip())
        else:
            seen_list.append(line.strip())
    print('len seen_list=' + str(len(seen_list)))
    print('len unseen_list=' + str(len(unseen_list)))
    # 保存seen_list和unseen_list到txt文件
    with open('./seen_list.txt', 'w') as f:
        f.write('\n'.join(seen_list))
    with open('./unseen_list.txt', 'w') as f:
        f.write('\n'.join(unseen_list))


# 从未见类中划分出zsd和gzsd
def main2():
    txt_path = './unseen_list.txt'
    unseen_classes = ['airport', 'basketballcourt', 'groundtrackfield', 'windmill']
    lines = read_txt(txt_path)
    zsd_list = []
    gzsd_list = []
    for line in lines:
        xml_path = os.path.join('./dior/Annotations/Horizontal Bounding Boxes', line.strip() + '.xml')
        root = read_xml(xml_path)
        classes_found = [obj.find('name').text.lower() for obj in root.findall('object')]
        # 检查classes_found中的所有类别是否都在unseen_classes中
        if all([c in unseen_classes for c in classes_found]):
            zsd_list.append(line.strip())
        else:
            gzsd_list.append(line.strip())
    print('len zsd_list=' + str(len(zsd_list)))
    print('len gzsd_list=' + str(len(gzsd_list)))
    # 保存zsd_list和gzsd_list到txt文件
    with open('./zsd_list.txt', 'w') as f:
        f.write('\n'.join(zsd_list))
    with open('./gzsd_list.txt', 'w') as f:
        f.write('\n'.join(gzsd_list))


# 统计list中的标注数量,涉及的类别数量,涉及的类别
def main3():
    txt_path = './dior/ZSDAnnotations/csv/Test/seen_list.txt'
    lines = read_txt(txt_path)
    # 统计seen_list中的标注数量
    annotations_nums = 0
    categories = set()
    for line in lines:
        xml_path = os.path.join('./dior/Annotations/Horizontal Bounding Boxes', line.strip() + '.xml')
        root = read_xml(xml_path)
        all_object = root.findall('object')
        for obj in all_object:
            categories.add(obj.find('name').text)
        annotations_nums += len(all_object)

    print('总共的标注框数量=' + str(annotations_nums))
    print('涉及的类别数量=' + str(len(categories)))
    print('涉及的类别=', categories)


# 统计gzsd_list中的可见类别和未见类别的标注数量
def main4():
    txt_path = './dior/ZSDAnnotations/Test/gzsd_list.txt'
    lines = read_txt(txt_path)
    # 统计seen_list中的标注数量
    seen_annotations_nums = 0
    unseen_annotations_nums = 0
    for line in lines:
        xml_path = os.path.join('./dior/Annotations/Horizontal Bounding Boxes', line.strip() + '.xml')
        root = read_xml(xml_path)
        all_object = root.findall('object')
        for obj in all_object:
            if obj.find('name').text in ['airport', 'basketballcourt', 'groundtrackfield', 'windmill']:
                unseen_annotations_nums += 1
            else:
                seen_annotations_nums += 1
    print('可见类别的标注框数量=', seen_annotations_nums)
    print('未见类别的标注框数量=', unseen_annotations_nums)


def main5(path):
    txt_path = path
    lines = read_txt(txt_path)
    # 统计seen_list中的标注数量
    categories = []
    for line in lines:
        xml_path = os.path.join('./dior/Annotations/Horizontal Bounding Boxes', line.strip() + '.xml')
        root = read_xml(xml_path)
        all_object = root.findall('object')
        for obj in all_object:
            if obj.find('name').text not in categories:
                categories.append(obj.find('name').text)
        if len(categories) == 20:
            break
    print('涉及的类别数量=' + str(len(categories)))
    print('涉及的类别=', categories)
    # 保存为categories.txt
    with open('./categories.txt', 'w') as f:
        f.write('\n'.join(categories))


def main6():
    import os
    import json
    import xml.etree.ElementTree as ET

    # 类别列表，按照给定顺序创建类别 ID 映射
    # 可见类 16
    categories = [
        'golffield', 'Expressway-toll-station', 'vehicle', 'trainstation', 'chimney', 'storagetank', 'ship',
        'harbor', 'airplane', 'tenniscourt', 'dam', 'Expressway-Service-area', 'stadium', 'baseballfield', 'bridge',
        'overpass'
    ]
    # 未见类 4
    # categories = [
    #     'groundtrackfield', 'basketballcourt', 'airport', 'windmill'
    # ]
    # 所有类别 20 gzsd
    # categories = [
    #     'golffield', 'Expressway-toll-station', 'vehicle', 'trainstation', 'chimney', 'storagetank', 'ship',
    #     'harbor', 'airplane', 'tenniscourt', 'dam', 'Expressway-Service-area', 'stadium', 'baseballfield', 'bridge',
    #     'overpass',
    #     'groundtrackfield', 'basketballcourt', 'airport', 'windmill'
    # ]

    # 创建类别映射（类别名称 -> 类别ID）
    category_map = {category: idx + 1 for idx, category in enumerate(categories)}

    # 存储COCO格式的数据
    coco_data = {
        "images": [],
        "annotations": [],
        "categories": [{"id": category_map[category], "name": category} for category in categories]
    }

    # 读取seen_list.txt中的XML文件路径
    seen_list_path = "./dior/ZSDAnnotations/csv/Test/seen_list.txt"
    with open(seen_list_path, "r") as f:
        xml_files = [line.strip() for line in f if line.strip()]

    # 存储图片ID和注释ID的计数器
    image_id = 1
    annotation_id = 1

    # 遍历每个XML文件
    for xml_file in xml_files:
        xml_file = os.path.join('./dior/Annotations/Horizontal Bounding Boxes', xml_file + '.xml')

        # 解析XML文件
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # 获取图片信息
        filename = root.find('filename').text
        width = int(root.find('size/width').text)
        height = int(root.find('size/height').text)

        # 创建图片信息
        image_info = {
            "id": image_id,
            "file_name": filename,
            "width": width,
            "height": height
        }

        # 添加到COCO格式的图片列表
        coco_data["images"].append(image_info)

        # 遍历每个object（目标）
        for obj in root.findall('object'):
            # 获取目标类别名称并转换为ID
            category_name = obj.find('name').text
            category_id = category_map[category_name]

            # 获取边界框信息
            bndbox = obj.find('bndbox')
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)

            # 计算目标区域的面积
            area = (xmax - xmin) * (ymax - ymin)

            # 创建注释信息
            annotation_info = {
                "id": annotation_id,
                "image_id": image_id,
                "category_id": category_id,
                "bbox": [xmin, ymin, xmax - xmin, ymax - ymin],  # [xmin, ymin, width, height]
                "area": area,
                "iscrowd": 0
            }

            # 添加到COCO格式的注释列表
            coco_data["annotations"].append(annotation_info)
            annotation_id += 1
            if annotation_id % 10000 == 0:
                print(f"已处理 {annotation_id} 个注释")

        # 增加图片ID
        image_id += 1
        if image_id % 1000 == 0:
            print(f"已处理 {image_id} 张图片")

    # 保存为COCO格式的JSON文件
    output_json_path = "converted_coco_annotations.json"
    with open(output_json_path, "w") as output_file:
        json.dump(coco_data, output_file, indent=4)

    print(f"转换完成，输出文件为 {output_json_path}")


if __name__ == '__main__':
    print('start')
    main6()
