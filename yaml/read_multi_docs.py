# yaml文件中含有多个文档时，分别获取文档中数据
import yaml


def get_yaml_load_all(yaml_file):
    # 打开yaml文件
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    all_data = yaml.load_all(file_data, Loader=yaml.FullLoader)  # <generator object load_all at 0x0000018234D46820>
    for data in all_data:
        print(data)


get_yaml_load_all("multi_docs.yaml")