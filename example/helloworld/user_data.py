from dataclasses import dataclass
from cyclonedds.idl import IdlStruct


# This class defines user data consisting of a float data and a string data
# 这个类定义了由一个浮点数据和一个字符串数据组成的用户数据。
# 使用Python中的dataclass装饰器，用于定义数据结构
@dataclass
# UserData类继承自IdlStruct类，并且指定了typename为"UserData"
class UserData(IdlStruct, typename="UserData"):
    string_data: str
    float_data: float
