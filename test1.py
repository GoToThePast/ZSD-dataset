import json

print('start')
# 读取train.json文件
with open('coco/ZSDAnnotations/48_17/csv/mscoco_train_list.json', 'r') as file:
    train_data = json.load(file)
# 集合
img_names=set()
image_save=[]
annotations=[]
synsets=set()
# 提取img_name和synset
for entry in train_data:
    if not img_names.__contains__(entry['img_name']):
        image_save.append(entry['img_name'].split('/')[-1])
    img_names.add(entry['img_name'])
    annotations.append(str(entry))
    synsets.add(entry['synset'])
# 输出去重后的数目
print("annotations数量:", len(annotations))
print("去重后的annotations数量:", len(set(annotations)))
print("去重后的img_name数量:", len(img_names))
print("image_save数量:", len(image_save))
print("去重后的synset数量:", len(synsets))

synsets={i.split('.')[0] for i in synsets}
print(synsets)
seen_classes={'toilet', 'bicycle', 'apple', 'train', 'laptop', 'carrot', 'motorcycle', 'oven', 'chair', 'mouse', 'boat',
              'kite', 'sheep', 'horse', 'sandwich', 'clock', 'tv', 'backpack', 'toaster', 'bowl', 'microwave', 'bench',
              'book', 'orange', 'bird', 'pizza', 'fork', 'frisbee', 'bear', 'vase', 'toothbrush', 'spoon', 'giraffe',
              'handbag', 'broccoli', 'refrigerator', 'remote', 'surfboard', 'car', 'bed', 'banana', 'donut', 'skis',
              'person', 'truck', 'bottle', 'suitcase', 'zebra', 'background'}
print(synsets.difference(seen_classes))
print(seen_classes.difference(synsets))

# 保存image_save为txt文件
with open('./image_save.txt', 'w') as file:
    for img_name in image_save:
        file.write(img_name+'\n')
