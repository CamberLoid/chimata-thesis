import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas

prop = fm.FontProperties(fname="/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc")

file = "Bench_CreateTransferJobByReceiptPK.csv"

data = pandas.read_csv(file)

seq = data['seq']
cycles = data["cycles"]
overall_in_s = data["overall_in_s"]
single_in_ms = data["single_in_ms"]

# 创建图形和轴对象
fig, ax1 = plt.subplots()

# 绘制左侧轴（overall_in_s）
ax1.plot(seq, overall_in_s, 'b-', marker='o')
ax1.set_xlabel('交易笔数', fontproperties=prop)
ax1.set_ylabel('总消耗时间 (s)', color='b', fontproperties=prop)
ax1.tick_params('y', colors='b')

# 创建右侧轴对象
ax2 = ax1.twinx()

# 绘制右侧轴（single_in_ms）
ax2.plot(seq, single_in_ms, 'r-', marker='x')
ax2.set_ylabel('平均每次操作消耗时间 (KB)', color='r', fontproperties=prop)
ax2.tick_params('y', colors='r')

ax2_ylim = ax2.get_ylim()
ax2.set_ylim(ax2_ylim[0]-5, ax2_ylim[1]+5)

# 设置横轴刻度
x_ticks = [1, 2, 3, 4, 5, 6, 7]
x_labels = cycles
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(x_labels)

for i in range(len(seq)):
    ax1.annotate(str(overall_in_s[i]), xy=(seq[i], overall_in_s[i]), xytext=(seq[i]-0.3, overall_in_s[i]+1),
                 ha='center', color='b')
    ax2.annotate(str(single_in_ms[i]), xy=(seq[i], single_in_ms[i]), xytext=(seq[i]+0.2, single_in_ms[i]+1),
                 ha='center', color='r')

# 添加图例  
legend1 = ax1.legend(['测试总时间开销 (s)'], loc='upper left', prop=prop)
legend2 = ax2.legend(['平均每笔交易时间开销 (ms)'], loc='upper left', prop=prop)

legend1.set_bbox_to_anchor((0, 1))
legend2.set_bbox_to_anchor((0, 0.92))


# 显示图形
plt.savefig("Bench_CreateTransferJobByReceiptPK.png", bbox_inches='tight', pad_inches=0.2)
