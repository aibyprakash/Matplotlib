import numpy as np
import matplotlib.pyplot as plt


x_data = np.random.random(1000)*100
y_data = np.random.random(1000)*100

#y_data

#plt.scatter(x_data,y_data,c='#00f',marker="*",alpha=0.3,s=150)
#plt.show()



years = [2006 + x for x in range(16)]

years


weights = [80,83,84,85,86,82,81,79,83,80,82,82,83,81,80,79]
#plt.plot(years,weights,c='b',lw=2,linestyle='--')
#plt.plot(years,weights,"r--",lw=2)
#plt.show()


x=["C++","JAVA","PYTHON","C#","GO"]
y=[20,50,140,45,1]

#plt.bar(x,y,color="r",align='edge',edgecolor="green")
#plt.show()


# Mean of 20 ,standerd deviation of 1.5 
ages = np.random.normal(20,1.5,1000)
#ages
#plt.hist(ages,bins=20,cumulative=True)
         #bins=[ages.min(),18,21,ages.max()])
#plt.show()

langs = ["C++","JAVA","PYTHON","C#","GO"]
votes = [20,50,140,45,17]
explodes = [0,0,0,0.2,0]


plt.pie(votes,labels=langs,explode=explodes,autopct="%.2f%%",pctdistance=1.5,startangle=90)