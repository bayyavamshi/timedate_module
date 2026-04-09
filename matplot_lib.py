import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('population.csv')
# plt.plot(df['Year'],df['India'],marker='s',color='green',linestyle='-.')
# plt.plot(df['Year'],df['China'],marker='o',color='red',linestyle='--')
# plt.title('Population Growth')
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.legend(['India','China'])
# plt.grid(True)
#-----------------------------------------------
# year2020 = df[df['Year'] == 2020].iloc[0]
# print(year2020)
# countries = ['India', 'China', 'USA', 'Brazil']
# populations = [year2020['India'], year2020['China'], year2020['USA'], year2020['Brazil']]

# # plt.bar(countries, populations, color=['green', 'red', 'blue', 'orange'])
# # plt.title("Population Comparison in 2020")
# plt.pie(populations, labels=countries, autopct='%1.1f%%', colors=['green', 'red', 'blue', 'orange'])

# plt.xlabel("Country")
# plt.ylabel("Population (in millions)")
# plt.grid(True)
# size=[50,100,150,200]
# sectors=['IT','Finance','Sales','HR']
# plt.figure(figsize=(8,6))
# plt.scatter(size,sectors,color='purple',marker='*',alpha=0.1,s=500,edgecolor='black')
x=[1,2,3,4,5]
y=[10,20,25,30,40]
y1=[12,18,28,35,45]
# plt.plot(x,y,linestyle='--',marker='o',color='b',label='Line 1')
# plt.plot(x,y1,linestyle='-.',marker='s',color='r',label='Line 2')
# plt.legend(loc='upper right')
plt.style.use('seaborn-v0_8')
fig,axes=plt.subplots(2,2)
axes[0][0].plot(x,y,linestyle='--',marker='o',color='b',label='Line 1')
axes[0][0].set_title('Line Plot 1')
axes[0][0].text(3,25,'Peak',color='red')
axes[0][0].annotate('Mid Point',xy=(3,25),xytext=(4,15),arrowprops=dict(facecolor='black',arrowstyle='->'))
axes[0][0].legend()
axes[0][1].plot(x,y1,linestyle='-.',marker='s',color='r',label='Line 2')
axes[0][1].set_title('Line Plot 2')
axes[0][1].legend()
axes[1][0].bar(['A','B','C'],[5,10,15],color='g')
axes[1][0].set_title('Bar Plot')
axes[1][1].pie([30,40,30],labels=['X','Y','Z'],autopct='%1.1f%%',colors=['c','m','y'])
axes[1][1].set_title('Pie Chart')
plt.tight_layout()
plt.show()
