import json
from pyecharts.charts import Map
from pyecharts import options as opts

"""
处理数据
"""

# 获取全国疫情数据
with open("../疫情.txt") as f:
    china_data = f.read()

# 对数据进行处理
china_data = json.loads(china_data)
china_data = china_data["areaTree"][0]["children"]

# 创建一个空列表存储数据
data_list = []

# 遍历 china_data 的元素，将数据封装到元组中,然后将每一个元组作为列表的元素
for province_data in china_data:
    # 省名称
    province_name = province_data["name"]
    # 确诊人数
    province_value = province_data["total"]["confirm"]
    # 将数据添加到 list 中
    data_list.append((province_name, province_value))

# 创建地图对象
virus_map = Map()

# 添加数据
virus_map = virus_map.add("疫情地图", data_list, "china")

# 配置
virus_map.set_global_opts(visualmap_opts=opts.VisualMapOpts(
    is_piecewise=True,
    pieces=[
        {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
        {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
        {"min": 100, "max": 499, "label": "99-499人", "color": "#FF9966"},
        {"min": 500, "max": 999, "label": "499-999人", "color": "#FF6666"},
        {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
        {"min": 1000, "label": "1000万人以上", "color": "#990033"},

    ]
))

# 生成地图
virus_map.render("国内疫情地图.html")
