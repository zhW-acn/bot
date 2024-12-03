import json
import os


class User:
    def __init__(self, id=None, age=None, city=None):
        self.id = id
        self.age = age

    def to_json(self, file_path):
        """将类的属性保存到 JSON 文件。"""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.__dict__, f, indent=4, ensure_ascii=False)

    @classmethod
    def from_json(cls, file_path):
        """从 JSON 文件加载数据并创建类的实例。"""
        if not os.path.exists(file_path):
            return cls()
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls(**data)
