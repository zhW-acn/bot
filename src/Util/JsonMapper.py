import json
import os

class JsonMapper:
    def __init__(self, file_path):
        """
        初始化 JsonMapper 类。
         file_path: JSON 文件路径。
        """
        self.file_path = file_path
        self.data = {}  # 用于存储映射的数据

    def load(self):
        """从 JSON 文件加载数据到实例中。"""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)  # 读取 JSON 数据并存储到 data 中
        else:
            self.data = {}  # 文件不存在时，初始化为空字典

    def save(self):
        """将当前实例数据保存到 JSON 文件。"""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)  # 保存 JSON 数据

    def set_value(self, key, value):
        """
        设置一个键值对到数据中。
        :param key: 键。
        :param value: 值。
        """
        self.data[key] = value

    def get_value(self, key, default=""):
        """
        获取数据中某个键的值。
        :param key: 键。
        :param default: 如果键不存在，则返回默认值。
        :return: 键对应的值或默认值。
        """
        return str(self.data.get(key, default))
