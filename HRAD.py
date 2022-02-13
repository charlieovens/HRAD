#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('cd', '/Users/charlieovens/Desktop/v1')
get_ipython().run_line_magic('pwd', '')

HRAD = pd.read_excel('HRAD stats.xlsx')

qyear = HRAD['Year ']
Quarts = HRAD['Quarter']
alllessthan250 = HRAD['All liable transactions under £250K']
allbetween250_500 = HRAD['All liable transactions between £250K and £500K']
allliable500_1mn = HRAD['All liable transactions between £500K and £1 million.']
HRAD250 = HRAD['HRAD transactions under £250K']
HRAD250_500 = HRAD['HRAD transactions between £250K and £500K']
HRAD500_1mn =HRAD['HRAD transactions between £500K and £1 million.']
Allhrad = HRAD['All liable HRAD transactions']

fig, (ax1, ax2) = plt.subplots(1,2, figsize= (18,8))

ax1.plot(Quarts, alllessthan250, 'r')
ax1.plot(Quarts, allbetween250_500, 'y')
ax1.plot(Quarts, allliable500_1mn, 'g')
ax1.legend(['< £250k', '£250k to £500k', '£500k to £1mn'])
ax1.set_xlabel('Years')
ax1.set_ylabel('Transaction Volume')
ax1.set_xticks(['2008 Q2', '2009 Q1', '2010 Q1', '2011 Q1', '2012 Q1', '2013 Q1', '2014 Q1', '2015 Q1', '2016 Q1', '2017 Q1', '2018 Q1', '2019 Q1', '2020 Q1', '2021 Q1'])
ax1.set_xticklabels(['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'])


ax2.plot(Quarts, HRAD250_500, 'r')
ax2.plot(Quarts, HRAD250, 'y')
ax2.plot(Quarts, HRAD500_1mn, 'g')
ax2.plot(Quarts, Allhrad, 'b')
ax2.set_xlabel('Years')
ax2.set_ylabel('Transaction Volume')
ax2.legend(['< £250k', '£250k to £500k', '£500k to £1mn', 'All HRAD Transactions'])
ax2.set_xticks(['2016 Q1', '2017 Q1', '2018 Q1', '2019 Q1', '2020 Q1', '2021 Q1'])
ax2.set_xticklabels(['2016', '2017', '2018', '2019', '2020', '2021'])

plt.savefig('HRAD Reciepts1.pdf')


# In[ ]:




