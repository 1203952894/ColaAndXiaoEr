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

# 获取省内确诊数据
for province_data in china_data:
    if province_data["name"] == "山西":
        province_shanxi_data = province_data["children"]

# 定义一个空列表
city_list = []
# 获取城市信息
for city_data in province_shanxi_data:
    city_list.append(
        (city_data["name"] + "市", city_data["total"]["confirm"])
    )

# 创建地图对象
shanxi_virus_map = Map()

# 添加数据
shanxi_virus_map = shanxi_virus_map.add("山西省疫情地图", city_list, "山西")

# 配置
shanxi_virus_map.set_global_opts(visualmap_opts=opts.VisualMapOpts(
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
shanxi_virus_map.render("省内疫情地图.html")
