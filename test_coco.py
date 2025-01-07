import json


def load_coco_annotations(json_file):
    """
    读取 COCO 数据集的标注文件（JSON 格式）
    :param json_file: 标注文件的路径
    :return: 标注数据字典
    """
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data


def get_bboxes_and_labels(image_id, coco_data):
    """
    获取给定图片 ID 对应的所有边界框和标签
    :param image_id: 图像的 ID
    :param coco_data: COCO 数据集的标注数据
    :return: (bboxes, labels) 其中 bboxes 为边界框坐标列表，labels 为类别标签列表
    """
    # 获取所有标注
    annotations = coco_data['annotations']

    # 筛选出当前图像的所有标注
    bboxes = []
    labels = []
    for ann in annotations:
        if ann['image_id'] == image_id:
            bboxes.append(ann['bbox'])  # 获取边界框
            labels.append(ann['category_id'])  # 获取类别 ID

    return bboxes, labels


def get_category_names(category_ids, coco_data):
    """
    将类别 ID 转换为类别名称
    :param category_ids: 类别 ID 列表
    :param coco_data: COCO 数据集的标注数据
    :return: 类别名称列表
    """
    # 获取所有类别
    categories = coco_data['categories']

    # 创建类别 ID 到名称的映射
    category_map = {category['id']: category['name'] for category in categories}

    # 转换 ID 为名称
    category_names = [category_map[cat_id] for cat_id in category_ids]

    return category_names


def get_image_bboxes_and_labels(image_id, coco_json_file):
    """
    获取给定图像 ID 对应的所有边界框（bbox）和标签（label）
    :param image_id: 图像的 ID
    :param coco_json_file: COCO 数据集的标注文件路径
    :return: (bboxes, labels) 其中 bboxes 为边界框坐标列表，labels 为类别名称列表
    """
    # 读取 COCO 标注数据
    coco_data = load_coco_annotations(coco_json_file)

    # 获取给定图像 ID 的所有边界框和标签
    bboxes, labels = get_bboxes_and_labels(image_id, coco_data)

    # 获取类别名称
    category_names = get_category_names(labels, coco_data)

    return bboxes, category_names


# 示例使用：
if __name__ == '__main__':
    coco_json_file = './coco/annotations/instances_val2014.json'  # COCO 标注文件的路径
    image_id = 569618  # 假设图像 ID 为 123456

    bboxes, labels = get_image_bboxes_and_labels(image_id, coco_json_file)

    print(f"Image ID: {image_id}")
    print("Bounding boxes:", bboxes)
    print("Labels:", labels)

"""
"categories": [{"supercategory": "person","id": 1,"name": "person"},
{"supercategory": "vehicle","id": 2,"name": "bicycle"},{"supercategory": "vehicle","id": 3,"name": "car"},{"supercategory": "vehicle","id": 4,"name": "motorcycle"},{"supercategory": "vehicle","id": 5,"name": "airplane"},{"supercategory": "vehicle","id": 6,"name": "bus"},{"supercategory": "vehicle","id": 7,"name": "train"},{"supercategory": "vehicle","id": 8,"name": "truck"},{"supercategory": "vehicle","id": 9,"name": "boat"},{"supercategory": "outdoor","id": 10,"name": "traffic light"},{"supercategory": "outdoor","id": 11,"name": "fire hydrant"},{"supercategory": "outdoor","id": 13,"name": "stop sign"},{"supercategory": "outdoor","id": 14,"name": "parking meter"},{"supercategory": "outdoor","id": 15,"name": "bench"},{"supercategory": "animal","id": 16,"name": "bird"},{"supercategory": "animal","id": 17,"name": "cat"},{"supercategory": "animal","id": 18,"name": "dog"},{"supercategory": "animal","id": 19,"name": "horse"},{"supercategory": "animal","id": 20,"name": "sheep"},{"supercategory": "animal","id": 21,"name": "cow"},{"supercategory": "animal","id": 22,"name": "elephant"},{"supercategory": "animal","id": 23,"name": "bear"},{"supercategory": "animal","id": 24,"name": "zebra"},{"supercategory": "animal","id": 25,"name": "giraffe"},{"supercategory": "accessory","id": 27,"name": "backpack"},{"supercategory": "accessory","id": 28,"name": "umbrella"},{"supercategory": "accessory","id": 31,"name": "handbag"},{"supercategory": "accessory","id": 32,"name": "tie"},{"supercategory": "accessory","id": 33,"name": "suitcase"},{"supercategory": "sports","id": 34,"name": "frisbee"},{"supercategory": "sports","id": 35,"name": "skis"},{"supercategory": "sports","id": 36,"name": "snowboard"},{"supercategory": "sports","id": 37,"name": "sports ball"},{"supercategory": "sports","id": 38,"name": "kite"},{"supercategory": "sports","id": 39,"name": "baseball bat"},{"supercategory": "sports","id": 40,"name": "baseball glove"},{"supercategory": "sports","id": 41,"name": "skateboard"},{"supercategory": "sports","id": 42,"name": "surfboard"},{"supercategory": "sports","id": 43,"name": "tennis racket"},{"supercategory": "kitchen","id": 44,"name": "bottle"},{"supercategory": "kitchen","id": 46,"name": "wine glass"},{"supercategory": "kitchen","id": 47,"name": "cup"},{"supercategory": "kitchen","id": 48,"name": "fork"},{"supercategory": "kitchen","id": 49,"name": "knife"},{"supercategory": "kitchen","id": 50,"name": "spoon"},{"supercategory": "kitchen","id": 51,"name": "bowl"},{"supercategory": "food","id": 52,"name": "banana"},{"supercategory": "food","id": 53,"name": "apple"},{"supercategory": "food","id": 54,"name": "sandwich"},{"supercategory": "food","id": 55,"name": "orange"},{"supercategory": "food","id": 56,"name": "broccoli"},{"supercategory": "food","id": 57,"name": "carrot"},{"supercategory": "food","id": 58,"name": "hot dog"},{"supercategory": "food","id": 59,"name": "pizza"},{"supercategory": "food","id": 60,"name": "donut"},{"supercategory": "food","id": 61,"name": "cake"},{"supercategory": "furniture","id": 62,"name": "chair"},{"supercategory": "furniture","id": 63,"name": "couch"},{"supercategory": "furniture","id": 64,"name": "potted plant"},{"supercategory": "furniture","id": 65,"name": "bed"},{"supercategory": "furniture","id": 67,"name": "dining table"},{"supercategory": "furniture","id": 70,"name": "toilet"},{"supercategory": "electronic","id": 72,"name": "tv"},{"supercategory": "electronic","id": 73,"name": "laptop"},{"supercategory": "electronic","id": 74,"name": "mouse"},{"supercategory": "electronic","id": 75,"name": "remote"},{"supercategory": "electronic","id": 76,"name": "keyboard"},{"supercategory": "electronic","id": 77,"name": "cell phone"},{"supercategory": "appliance","id": 78,"name": "microwave"},{"supercategory": "appliance","id": 79,"name": "oven"},{"supercategory": "appliance","id": 80,"name": "toaster"},{"supercategory": "appliance","id": 81,"name": "sink"},{"supercategory": "appliance","id": 82,"name": "refrigerator"},{"supercategory": "indoor","id": 84,"name": "book"},{"supercategory": "indoor","id": 85,"name": "clock"},{"supercategory": "indoor","id": 86,"name": "vase"},{"supercategory": "indoor","id": 87,"name": "scissors"},{"supercategory": "indoor","id": 88,"name": "teddy bear"},{"supercategory": "indoor","id": 89,"name": "hair drier"},{"supercategory": "indoor","id": 90,"name": "toothbrush"}]}
"""