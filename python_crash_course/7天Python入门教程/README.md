# 7天Python入门教程

## 课程结构
📂 7天Python入门教程/
│
├── day1_basic/
│   ├── examples/       # 基础语法示例
│   ├── exercises/      # 配套练习题
│   └── 学习指南.md
├── day2_data_structure/
│   ├── examples/       # 数据结构示例
│   ├── exercises/      
│   └── 学习指南.md
├── ...
└── final_project/      # 综合实战项目
    ├── weather_app/    # 天气查询系统
    └── stock_analysis/ # 股市数据分析

## 每日学习计划

### Day 1: 基础语法
```python
# 示例：温度转换器
def celsius_to_fahrenheit(c):
    """摄氏转华氏温度
    
    Args:
        c (float): 摄氏温度
    
    Returns:
        float: 华氏温度
    """
    return c * 9/5 + 32
```

### Day 2: 数据结构
```python
# 练习：通讯录管理
contacts = {
    "李明": {"phone": "13800138000", "email": "liming@example.com"},
    "王芳": {"phone": "13912345678", "email": "wangfang@example.com"}
}
```

...（后续天数内容）...

## 综合实战项目
### 天气查询系统
使用requests库和开放API实现实时天气查询：
```python
import requests

# 从AKShare获取股票数据 <mcreference link="https://akshare.akfamily.xyz/index.html" index="1">1</mcreference>
def get_stock_data(symbol):
    """获取股票实时数据
    
    Args:
        symbol (str): 股票代码（如：sh600000）
    """
    import akshare as ak
    stock_zh_a_spot = ak.stock_zh_a_spot()
    return stock_zh_a_spot[stock_zh_a_spot['代码'] == symbol]
```

## 环境配置
```bash
# requirements.txt
requests==2.31.0
pandas==2.1.4
akshare==1.12.70
```