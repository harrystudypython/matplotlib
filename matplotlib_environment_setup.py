from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

x = range(11, 31)

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y_1, label="myself", color="#F08080")
plt.plot(x, y_2, label="desk_mate", color="#DB7093", linestyle="--")

_xtick_labels = ["{}".format(i) for i in x]
plt.xticks(x, _xtick_labels)#, fontproperties=my_font)
plt.grid(alpha=0.4, linestyle=':')

#plt.legend( loc="upper left")
num1=1
num2=0
num3=3
num4=0
plt.legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4)
plt.show()
