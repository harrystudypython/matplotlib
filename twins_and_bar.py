import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
 
#设置字体、图形样式
sns.set_style("whitegrid")
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False
#matplotlib.fontsize='15'
 
#取做图数据
x=range(len(gsbf['统计日期']))
y1=gsbf['累计保费']
y2=gsbf['同比(%)']
 
#设置图形大小
plt.rcParams['figure.figsize'] = (12.0,5.0) 
 
fig = plt.figure()
 
#画柱子
ax1 = fig.add_subplot(111)
ax1.bar(x, y1,alpha=.7,color='g')
ax1.set_ylabel('累计保费（万元）',fontsize='15')
ax1.set_title("近年同期公司累计保费收入与同比增速",fontsize='20')  
plt.yticks(fontsize=15)
plt.xticks(x,gsbf['统计日期'])
plt.xticks(fontsize=15)
 
 
#画折线图
ax2 = ax1.twinx()  # 这个很重要噢
ax2.plot(x, y2, 'r',marker='*',ms=10)
 
ax2.set_xlim([-0.5,3.5])
ax2.set_ylim([0,45])
ax2.set_ylabel('同比增速（%）',fontsize='15')
ax2.set_xlabel('同比增速（%）')
 
 
#纵轴标签
plt.yticks(fontsize=15)
plt.xticks(x,gsbf['统计日期'])
plt.xticks(fontsize=15)
plt.grid(False)
 
#添加数据标签
for x, y ,z in zip(x,y2,y1):
        plt.text(x, y+0.3, str(y), ha='center', va='bottom', fontsize=20,rotation=0)
        plt.text(x, z-z, str(int(z)), ha='center', va='bottom', fontsize=21,rotation=0)
     
 
#保存图片 dpi为图像分辨率
plt.savefig('e:/tj/month/fx1806/公司保费增速与同比.png',dpi=600,bbox_inches = 'tight')
#显示图片
plt.show()














