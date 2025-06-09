# -*- coding: utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt



# %%
firsrt = np.linspace(0, 10,25)
second= np.linspace(10, 200,25)
third = np.linspace(200, 210,25)
fourth = np.linspace(210, 230,25)


data = np.concatenate((firsrt,second,third,fourth))

plt.boxplot(data)
plt.show()


# %%

years = [2014,2015,2016,2017,2018,2019,2020,2021]
income = [55,56,62,61,72,72,73,75]

income_ticks = list(range(50,81,2))
plt.plot(years,income)

plt.title("Income of  John (in USD)",fontsize=30,fontname="Times New Roman")
plt.xlabel("Year")
plt.ylabel("Income in USD")
plt.yticks(income_ticks,[f"${x}K" for x in income_ticks])
plt.show()


# %%


stock_a = [100,102,99,101,100,102]
stock_b = [90,95,102,104,105,103,109]
stock_c = [110,115,100,105,100,98,95]