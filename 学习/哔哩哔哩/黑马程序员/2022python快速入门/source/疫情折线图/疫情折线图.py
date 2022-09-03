import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts
"""
处理数据
"""
# 打开文件
fr_us = open("美国.txt", "r", encoding="UTF-8")
fr_jp = open("日本.txt", "r", encoding="UTF-8")
fr_in = open("印度.txt", "r", encoding="UTF-8")
# 获取全部内容
us_data = fr_us.read()
jp_data = fr_jp.read()
in_data = fr_in.read()
# 格式化 json 数据
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]

jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
jp_data = jp_data[:-2]

in_data = in_data.replace("jsonp_1629350745930_63180(", "")
in_data = in_data[:-2]
# 转换为 python 字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取 trend key
us_trend_data = us_dict["data"][0]["trend"]
jp_trend_data = jp_dict["data"][0]["trend"]
in_trend_data = in_dict["data"][0]["trend"]

# 获取 x 轴数据并进行处理(截止到 314)
us_x_data = us_trend_data["updateDate"][:314]
jp_x_data = jp_trend_data["updateDate"][:314]
in_x_data = in_trend_data["updateDate"][:314]
# 获取 y 轴数据并进行处理(截止到 314)
us_y_data = us_trend_data["list"][0]["data"][:314]
jp_y_data = jp_trend_data["list"][0]["data"][:314]
in_y_data = in_trend_data["list"][0]["data"][:314]


# 构建折线图对象
line = Line()

# 添加 x 轴(公用)
line.add_xaxis(us_x_data)

# 添加 y 轴数据
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局选项
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2022年美日印三国确诊人口对比折线图", pos_right="center", pos_bottom="1%")
)

# 生成折线图
line.render("疫情折线图.html")

# 关闭文件
fr_us.close()
fr_jp.close()
fr_in.close()