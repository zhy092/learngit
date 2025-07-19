"""
Day 1 基础语法示例
包含：变量类型、输入输出、类型转换
"""

# 1. 变量与打印
name = "张三"
age = 25
print(f"【个人信息】\n姓名：{name}\n年龄：{age}")

# 2. 温度转换函数
def convert_temperature(celsius):
    """摄氏温度转华氏温度
    
    Args:
        celsius (float): 摄氏温度值
    
    Returns:
        float: 华氏温度值
    """
    return celsius * 9/5 + 32

# 3. 用户输入处理
input_temp = float(input("请输入摄氏温度："))
print(f"{input_temp}℃ = {convert_temperature(input_temp):.1f}℉")

# 4. 类型转换练习
num_str = "123"
print(f"字符串转整数：{int(num_str) + 7}")