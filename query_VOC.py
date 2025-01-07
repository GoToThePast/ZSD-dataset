import os
import xml.etree.ElementTree as ET
import shutil

def query_voc():
    # 设置PASCAL VOC路径
    voc_root = './VOCdevkit/VOC2007'  # 修改为你自己的VOC路径

    # 目标类别
    target_classes = [['person', 'tvmonitor', 'dog'],
                      ['bicycle', 'sofa'],
                      ['bicycle', 'person','car'],
                      ['diningtable', 'bottle','sofa']]

    # 获取所有的xml文件路径
    annotations_path = os.path.join(voc_root, 'Annotations')
    annotation_files = [f for f in os.listdir(annotations_path) if f.endswith('.xml')]

    # 存储符合条件的图像
    valid_images = []

    # 遍历所有xml文件，检查是否包含目标类别
    for annotation_file in annotation_files:
        # 解析XML文件
        annotation_path = os.path.join(annotations_path, annotation_file)
        tree = ET.parse(annotation_path)
        root = tree.getroot()

        # 获取所有物体类别
        objects = root.findall('object')
        classes_found = {obj.find('name').text.lower() for obj in objects}

        # 检查是否同时包含目标类别
        for target_class in target_classes:
            if all(cls in classes_found for cls in target_class):
                image_name = root.find('filename').text
                valid_images.append(image_name)
                break

    # 输出符合条件的图像
    print(f"符合条件的图像：{len(valid_images)} 张")
    # 保存valid_images
    with open('./valid_images.txt', 'w') as f:
      for image in valid_images:
        f.write(image + '\n')
    for image in valid_images:
        print(image)


def compare():
    # 读取 valid_images.txt 中的图像数据
    with open('./valid_images.txt', 'r') as f:
        # 读取所有行并去掉每行末尾的".jpg"
        valid_images = {line.strip().replace('.jpg', '') for line in f.readlines()}

    # 读取 trainval.txt 中的图像数据
    with open('./VOCdevkit/VOC2007/ImageSets/Main/trainval.txt', 'r') as f:
        # 读取所有行并去掉每行末尾的".jpg"
        trainval_images = {line.strip() for line in f.readlines()}

    # 读取 trainval.txt 中的图像数据
    with open('./VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'r') as f:
        # 读取所有行并去掉每行末尾的".jpg"
        test_images = {line.strip() for line in f.readlines()}
    # 找到 valid_images 中存在于 trainval 中的数据和不在其中的数据
    intersection = valid_images.intersection(trainval_images)  # 存在于 trainval 中的图片
    difference = valid_images.difference(trainval_images)  # 不存在于 trainval 中的图片

    # 输出结果
    print(f"共计 {len(valid_images)} 张 valid_images 图像")
    print(f"共计 {len(trainval_images)} 张 trainval 图像")
    print(f"在 trainval 中存在的 valid_images 图像：{len(intersection)} 张")
    print(f"不在 trainval 中的 valid_images 图像：{len(difference)} 张")

    # 打印出部分结果
    print("\n在 trainval 中存在的 valid_images 图像（示例）：")
    print(list(intersection)[:10])  # 输出前10个示例

    print("\n不在 trainval 中的 valid_images 图像（示例）：")
    print(list(difference))  # 输出前10个示例

    x=[]
    for i in list(intersection):
        x.append(i + '.jpg')
    for i in x:
        shutil.copy('./VOCdevkit/VOC2007/JPEGImages/'+i, './训练集中的GZSD图片'+i)

if __name__ == '__main__':
    compare()
    # x=[]
    # for i in ['001177', '007937', '001431', '003746', '007447', '006113', '007583', '000584', '008560', '008895', '009564', '004101', '008464', '007237', '002920', '001403', '003928']:
    #     x.append(i+'.jpg')
    #
    # # 复制JPEG文件夹中与x中相同的文件到当前文件夹
    # for i in x:
    #     shutil.copy('./VOCdevkit/VOC2007/JPEGImages/'+i, './'+i)
    # print('done')