import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas

prop = fm.FontProperties(fname="/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc")

file = "Bench_DatabaseSize.csv"

data = pandas.read_csv(file)

seq = data['seq']
cycles = data["cycles"]
size_in_MB = data["size_in_MB"]
average_in_KB = data["average_in_KB"]

# 创建图形和轴对象
fig, ax1 = plt.subplots()

# 绘制左侧轴（size_in_MB）
ax1.plot(seq, size_in_MB, 'b-', marker='o')
ax1.set_xlabel('交易笔数', fontproperties=prop)
ax1.set_ylabel('总大小 (MB)', color='b', fontproperties=prop)
ax1.tick_params('y', colors='b')
ax1_ylim = ax1.get_ylim()
ax1.set_ylim(ax1_ylim[0], ax1_ylim[1]+35)

# 创建右侧轴对象
ax2 = ax1.twinx()

# 绘制右侧轴（average_in_KB）
ax2.plot(seq, average_in_KB, 'r-', marker='x')
ax2.set_ylabel('平均开销 (KB)', color='r', fontproperties=prop)
ax2.tick_params('y', colors='r')

ax2_ylim = ax2.get_ylim()
ax2.set_ylim(ax2_ylim[0], ax2_ylim[1]+155)

# 设置横轴刻度
x_ticks = [1, 2, 3, 4, 5, 6, 7, 8]
x_labels = cycles
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(x_labels)

for i in range(len(seq)):
    ax1.annotate(str(size_in_MB[i]), xy=(seq[i], size_in_MB[i]), xytext=(seq[i]-0.3, size_in_MB[i]+8),
                 ha='center', color='b')
    ax2.annotate(str(average_in_KB[i]), xy=(seq[i], average_in_KB[i]), xytext=(seq[i]+0.2, average_in_KB[i]+30),
                 ha='center', color='r')

# 添加图例  
ax1.legend(['总数据库大小 (MB)'], loc='upper left', prop=prop)
ax2.legend(['平均每笔交易空间开销 (KB)'], loc='upper right', prop=prop)

# 显示图形
plt.savefig("Bench_DatabaseSize.png")
