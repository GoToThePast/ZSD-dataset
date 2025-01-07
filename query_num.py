import pandas as pd
print("开始")
# 读取 CSV 文件，假设文件名为 'data.csv'
# df = pd.read_csv('./ZSD/train_coco_seen_all.csv') # 61598
df = pd.read_csv('./ZSD/validation_coco_seen_all.csv')
# df = pd.read_csv('./ZSD/validation_coco_unseen_all.csv') # 10097
# df = pd.read_csv('./ZSD/validation_coco_unseen_seen_all_gzsd.csv')
# df = pd.read_csv('./ZSD/VOC/train_voc07_12_seen.csv')
# df = pd.read_csv('./ZSD/VOC/testval_voc07_unseen.csv')
# df = pd.read_csv('./ZSD/VOC/testval_voc07_seen.csv')

print("读取csv完毕")
# 获取第一列数据 (A列)，并去除重复的路径
unique_paths = df.iloc[:, 0].drop_duplicates()
# 获取第六列数据 (F列)，并去除重复的路径
# unique_paths = df.iloc[:, 5].drop_duplicates()

# 返回去重后的数目
unique_count = len(unique_paths)

# 打印去重后的路径数目
print(f'去重后的路径数目是: {unique_count}')

# 将unique_paths中的值转换为集合
# unique_paths_set = set(unique_paths)

# x={'person', 'bicycle', 'car', 'motorcycle', 'bus', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'bench',
#     'bird', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'skis',
#     'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass',
#     'cup', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'orange', 'broccoli', 'carrot', 'pizza', 'donut', 'cake', 'chair', 'couch',
#     'potted plant', 'bed', 'dining table', 'tv', 'laptop', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'sink',
#     'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'toothbrush',
#     'airplane', 'train', 'parking meter', 'cat', 'bear', 'suitcase', 'frisbee', 'snowboard', 'fork', 'sandwich', 'hot dog',
#     'toilet', 'mouse', 'toaster', 'hair drier'}
#
# print(unique_paths_set)
# print("-----")
# print(x.difference(unique_paths_set))
# print(unique_paths_set.difference(x))

# import csv
#
# # 设置文件路径
# file_path = './ZSD/validation_coco_unseen_all.csv'
#
# # 打开文件并读取数据
# with open(file_path, newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#
#     # 跳过表头，如果有的话
#     next(reader, None)
#
#     # 使用集合去重第一列数据
#     first_column = {row[0] for row in reader}
#
# # 输出去重后的数目
# print(f"去重后的第一列11数据数目: {len(first_column)}")
