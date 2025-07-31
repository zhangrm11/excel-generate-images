import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('table1.xlsx', header=1)
#df.columns获取DataFrame的所有列名，是一个列表
df.columns = df.columns.str.strip()#数据清洗，去除了前后空格

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False #用于解决中文环境下负号显示异常的问题

months = df.iloc[:, 0]
beef = df['牛肉'] #返回列名为‘牛肉’的列，是Series对象
corn = df['玉米']
soy = df['豆粕']
wheat = df['小麦麸']

#创建一个图形窗口和坐标轴对象
#fig是创建的图形对象，代表整个绘图窗口；ax1是创建的坐标轴对象，用于实际绘制图像，比如折线图、柱状图
fig, ax1 = plt.subplots(figsize=(12, 6))

ln1 = ax1.plot(months, beef, marker='o', linestyle='-', color='brown', label='牛肉')
ax1.set_ylabel('牛肉价格（元/公斤）', fontsize=14)
ax1.set_ylim(60, 88)

for x, y in zip(months, beef):
    ax1.text(x, y-1.5, f'{y:.2f}', color='brown', fontsize=10, ha='center', va='bottom')

ax2 = ax1.twinx()
ln2 = ax2.plot(months, corn, marker='^', linestyle='--', color='orange', label='玉米')
ln3 = ax2.plot(months, soy, marker='s', linestyle='--', color='green', label='豆粕')
ln4 = ax2.plot(months, wheat, marker='D', linestyle='--', color='red', label='小麦麸')
ax2.set_ylabel('饲料价格（元/公斤）', fontsize=14)
ax2.set_ylim(1.5, 4.5)

for x, y in zip(months, corn):
    ax2.text(x, y+0.10, f'{y:.2f}', color='orange', fontsize=10, ha='center', va='top')
for x, y in zip(months, soy):
    ax2.text(x, y-0.08, f'{y:.2f}', color='green', fontsize=10, ha='center', va='top')
for x, y in zip(months, wheat):
    ax2.text(x, y-0.08, f'{y:.2f}', color='red', fontsize=10, ha='center', va='top')

# 合并
lns = ln1 + ln2 + ln3 + ln4
labels = [l.get_label() for l in lns]
ax1.legend(lns, labels, loc='upper right', fontsize=12)

plt.title('我国2024年牛肉及牛饲料平均价格情况', fontsize=18)
plt.xlabel('时间', fontsize=14)
plt.xticks(months, rotation=45, fontsize=10)
ax1.tick_params(axis='y', labelsize=10)
ax2.tick_params(axis='y', labelsize=10)
plt.tight_layout()
plt.grid(True, axis='x')
plt.show()
