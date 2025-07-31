一个用于从 Excel 数据生成可视化图像的 Python 项目，支持将表格数据转换为直观的图表，帮助快速理解数据趋势和分布。
功能介绍
读取 Excel 文件中的数据并进行清洗处理
生成多种类型的可视化图表（目前包含折线图、饼图等示例）
支持中文显示及个性化图表样式设置
为图表添加数据标签，提升数据可读性
示例展示
牛肉及饲料价格趋势图
通过table1.py生成，展示了 2024 年我国牛肉及各类牛饲料的价格变化趋势，使用双 Y 轴分别展示不同量级的价格数据。
区域分布饼图
通过table3.py中的辅助函数支持生成带有自定义标签的饼图，可用于展示不同区域的占比情况。
代码结构
table1.py：生成牛肉及饲料价格趋势折线图的示例代码
table3.py：包含饼图标签自定义生成函数的工具代码
核心代码解析
数据读取与处理
python
运行
import pandas as pd

# 读取Excel文件
df = pd.read_excel('table1.xlsx', header=1)
# 数据清洗，去除列名前后空格
df.columns = df.columns.str.strip()
图表绘制（折线图示例）
python
运行
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建图形和坐标轴
fig, ax1 = plt.subplots(figsize=(12, 6))

# 绘制主坐标轴数据
ln1 = ax1.plot(months, beef, marker='o', linestyle='-', color='brown', label='牛肉')

# 创建次坐标轴并绘制数据
ax2 = ax1.twinx()
ln2 = ax2.plot(months, corn, marker='^', linestyle='--', color='orange', label='玉米')

# 添加图例、标题和标签
ax1.legend(lns, labels, loc='upper right', fontsize=12)
plt.title('我国2024年牛肉及牛饲料平均价格情况', fontsize=18)
自定义饼图标签（table3.py）
python
运行
def autopct_generator(regions, values):
    def inner_autopct(pct):
        total = sum(values)
        idx = inner_autopct.idx
        # 自定义标签内容
        if regions.iloc[idx] == '辽宁':
            label = f'{regions.iloc[idx]}\n4.21%'
        else:
            label = f'{regions.iloc[idx]}\n{pct:.2f}%'
        inner_autopct.idx += 1
        return label
    inner_autopct.idx = 0
    return inner_autopct
使用说明
确保安装必要的依赖库：

bash
pip install pandas matplotlib openpyxl

将 Excel 数据文件放入项目目录
运行对应脚本生成图表：

bash
python table1.py

扩展建议
可根据需要扩展支持更多图表类型（柱状图、散点图等）
可添加命令行参数支持，实现更灵活的文件输入输出控制
可增加数据筛选和预处理功能，提升对不同格式 Excel 的兼容性
