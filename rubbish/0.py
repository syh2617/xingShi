import json

# 创建一个包含数据的字典
data = {
    "name": "苏玉恒",
    "age": 30,
    "city": "New York"
}

# 指定要写入的文件名
filename = "data.json"

# 打开文件并写入数据
with open(filename, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print("JSON文件已创建：", filename)
