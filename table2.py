import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('table2.xlsx', header=1)
df.columns = df.columns.str.strip()

years = df['年份/存栏及出栏'].astype(str)
stock = df['存栏数量']
slaughter = df['出栏数量']

bar_width = 0.35
x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 6), facecolor='white')


main_blue = '#4A90E2'   
main_orange = '#F5A623' 
main_gray = '#7B7D7D'   
main_silver = '#BDC3C7' 

bars1 = ax1.bar(x - bar_width/2, stock, width=bar_width, label='存栏数量', color=main_blue, edgecolor='black', alpha=0.92)
ax1.set_ylabel('存栏数量（万头）', fontsize=14, color=main_blue, fontweight='bold')
ax1.tick_params(axis='y', labelcolor=main_blue)


ax2 = ax1.twinx()
bars2 = ax2.bar(x + bar_width/2, slaughter, width=bar_width, label='出栏数量', color=main_orange, edgecolor='black', alpha=0.92)
ax2.set_ylabel('出栏数量（万头）', fontsize=14, color=main_orange, fontweight='bold')
ax2.tick_params(axis='y', labelcolor=main_orange)

# 设置y轴范围
ax1.set_ylim(4000,8500)
ax2.set_ylim(4000,5500)


for bar in bars1:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20, f'{bar.get_height():.1f}',
             ha='center', va='bottom', fontsize=10, color=main_blue, fontweight='bold')

for bar in bars2:
    ax2.text(bar.get_x() + bar.get_width()/2 + 0.07, bar.get_height() + 20, f'{bar.get_height():.1f}',
             ha='center', va='bottom', fontsize=10, color=main_orange, fontweight='bold')

plt.xlabel('年份', fontsize=14, fontweight='bold', color=main_gray, labelpad=10)
plt.title('我国2012-2021年肉牛年存栏及出栏数量', fontsize=18, fontweight='bold', color=main_blue, pad=20)
plt.xticks(x, years, rotation=45, fontsize=11, color=main_gray)

ax1.grid(axis='y', linestyle='--', alpha=0.4, color=main_silver)
ax1.set_axisbelow(True)

bars = [bars1[0], bars2[0]]
labels = ['存栏数量', '出栏数量']
legend = ax1.legend(bars, labels, fontsize=12, loc='upper left', frameon=False)
for text in legend.get_texts():
    text.set_color(main_gray)

plt.tight_layout()
plt.show()
