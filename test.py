import csv
from sortedcontainers import SortedSet
import json
#
# with open('coco/ZSDAnnotations/65_15/csv/cls_names_seen_coco.csv', 'r') as file:
#     reader = csv.reader(file)
#     x = {line[0].strip() for line in reader}
# with open('coco/ZSDAnnotations/65_15/csv/cls_names_test_coco.csv', 'r') as file:
#     reader = csv.reader(file)
#     y = [line[0].strip() for line in reader]
#
# import pandas as pd
#
# zsd = pd.read_csv('./ZSD/validation_coco_unseen_all.csv')
# zsd_unique_paths = zsd.iloc[:, 0].drop_duplicates()
#
# gzsd = pd.read_csv('./ZSD/validation_coco_unseen_seen_all_gzsd.csv')
# gzsd_unique_paths = gzsd.iloc[:, 0].drop_duplicates()
#


#
# with open('./coco/ZSDAnnotations/48_17/csv/mscoco_unseen_classes.json', 'r') as f:
#     coco_data = json.load(f)
#
# print(coco_data)
#
# seen_classes=['toilet', 'bicycle', 'apple', 'train', 'laptop', 'carrot', 'motorcycle', 'oven', 'chair', 'mouse', 'boat',
#              'kite', 'sheep', 'horse', 'sandwich', 'clock', 'tv', 'backpack', 'toaster', 'bowl', 'microwave', 'bench',
#              'book', 'orange', 'bird', 'pizza', 'fork', 'frisbee', 'bear', 'vase', 'toothbrush', 'spoon', 'giraffe',
#              'handbag', 'broccoli', 'refrigerator', 'remote', 'surfboard', 'car', 'bed', 'banana', 'donut', 'skis',
#              'person', 'truck', 'bottle', 'suitcase', 'zebra', 'background']
# unseen_classes=['umbrella', 'cow', 'cup', 'bus', 'keyboard', 'skateboard', 'dog', 'couch', 'tie', 'snowboard',
#                 'sink', 'elephant', 'cake', 'scissors', 'airplane', 'cat', 'knife']
#
# print(len(seen_classes))
# print(len(unseen_classes))
# print(seen_classes.intersection(unseen_classes))
# print(unseen_classes.intersection(seen_classes))
# 读取'./coco/ZSDAnnotations/48_17/seen_classes.txt'
with open('./coco/ZSDAnnotations/48_17/seen_classes.txt', 'r') as f:
    seen_classes = f.read().splitlines()
print(seen_classes)
