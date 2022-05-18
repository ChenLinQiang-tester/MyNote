import json

json_str = '{"name":"Felix","age":18,"None":null}'
print(json_str, type(json_str))

# json字符串 反序列化 为python对象(dict)-->loads()
jsonStr_to_dict = json.loads(json_str)  # {"name":"Felix","age":18,"None":None}
print(jsonStr_to_dict, type(jsonStr_to_dict))

# 读取json文件 反序列化 为python对象(dict)-->load()
with open("data.json", 'r', encoding='utf-8') as f:
    json_to_dict = json.load(f)

# python对象 序列化为 json字符串-->dumps()
dict_data = {'name': 'Felix', 'age': 18, 'hobby': ['运动', '游戏'], 'friends': [{'name': '小明'}, {'name': '小刚'}]}
dict_to_jsonStr = json.dumps(dict_data)
dict_to_jsonStr_1 = json.dumps(dict_data, ensure_ascii=False)   # ensure_ascii=False，中文字符不被转义
dict_to_jsonStr_2 = json.dumps(dict_data, ensure_ascii=False, indent=4)  # indent=4，漂亮缩进打印，空格填充，若为字符，则字符填充
dict_to_jsonStr_3 = json.dumps(dict_data, ensure_ascii=False, indent=4, sort_keys=True)  # sort_keys=True，根据key名称首字母排序
print(dict_to_jsonStr_2)
print(dict_to_jsonStr_3)


# python对象(dict) 序列化 为json文件-->dump()
with open('write.json', 'w', encoding='utf-8') as f:
    json.dump(dict_data, f, ensure_ascii=False, indent=4)