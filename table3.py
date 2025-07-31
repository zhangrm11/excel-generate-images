import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('table3.xlsx', header=0)

regions = df.iloc[:, 0].dropna()
values = df.iloc[:, 1].dropna()

fig, ax = plt.subplots(figsize=(8, 8))

def autopct_generator(regions, values):
    def inner_autopct(pct):
        total = sum(values)
        idx = inner_autopct.idx
        if regions.iloc[idx] == '辽宁':
            label = f'{regions.iloc[idx]}\n4.21%'
        else:
            label = f'{regions.iloc[idx]}\n{pct:.2f}%'
        inner_autopct.idx += 1
        return label
    inner_autopct.idx = 0
    return inner_autopct

colors = plt.cm.tab20(np.linspace(0, 1, len(values)))
wedges, texts, autotexts = ax.pie(
    values, labels=None, autopct=autopct_generator(regions, values), startangle=140, textprops={'fontsize': 12}, colors=colors
)

plt.title('我国2022年各地区牛年出栏量分布情况', fontsize=16, fontweight='bold')

info = '单位：万头 \n' + '\n'.join([f'{region}: {value:,.1f}' for region, value in zip(regions, values)])
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
plt.gcf().text(0.98, 0.98, info, fontsize=12, va='top', ha='right', bbox=props)

plt.tight_layout()
plt.show()