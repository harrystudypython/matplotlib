import seaborn as sns
import matplotlib
import matplotlib.pyplot as p
sns.set_style('whitegrid')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False
#matplotlib.fontsize='15'
 

x=range(len(gsbf['date']))
y1=gsbf['all_money']
y2=gsbf['rate(%)']
 
plt.rcParams['figure.figsize'] = (12.0,5.0) 
 
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.bar(x, y1,alpha=.7,color='g')
ax1.set_ylabel('all_money_y(yuan)',fontsize='15')
ax1.set_title("here_is_title",fontsize='20')  
plt.yticks(fontsize=15)
plt.xticks(x,gsbf['summary_date'])
plt.xticks(fontsize=15)

ax2 = ax1.twinx()  
ax2.plot(x, y2, 'r',marker='*',ms=10)
 
ax2.set_xlim([-0.5,3.5])
ax2.set_ylim([0,45])
ax2.set_ylabel('rate_of_increase(%)',fontsize='15')
ax2.set_xlabel('rate_pf_increase(%)')
plt.yticks(fontsize=15)
plt.xticks(x,gsbf['date_of_summary'])
plt.xticks(fontsize=15)
plt.grid(False)
for x, y ,z in zip(x,y2,y1):
        plt.text(x, y+0.3, str(y), ha='center', va='bottom', fontsize=20,rotation=0)
        plt.text(x, z-z, str(int(z)), ha='center', va='bottom', fontsize=21,rotation=0)
plt.savefig('d:/tj/month/fx1806/generate_by_python.png',dpi=600,bbox_inches = 'tight')
plt.show()














