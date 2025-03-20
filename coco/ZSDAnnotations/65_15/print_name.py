def read_txt_to_list(file_path):
    """
    读取 txt 文件，将每一行作为字符串存入列表并返回
    :param file_path: txt 文件路径
    :return: 包含文件所有行的列表
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip().split(',')[0] for line in file.readlines()]
        return lines
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到！")
        return []
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return []

file_path = "./all_classes.csv"
result = read_txt_to_list(file_path)
print("./all_classes.txt= " ,result)

file_path = "./unseen_classes.csv"
result = read_txt_to_list(file_path)
print("./unseen_classes.txt= " ,result)

file_path = "./seen_classes.csv"
result = read_txt_to_list(file_path)
print("./seen_classes.txt= " ,result)