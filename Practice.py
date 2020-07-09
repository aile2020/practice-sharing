#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[34]:


import pandas_datareader
import datetime


# In[35]:


import pandas_datareader.data as web


# In[36]:


start = datetime.datetime(2012,1,1)
end = datetime.datetime(2019,2,1)
tesla = web.DataReader('TSLA', 'yahoo', start, end)


# In[37]:


tesla.head()


# In[38]:


ford = web.DataReader('FORD', 'yahoo', start, end)
ford.head()


# In[39]:


gm = web.DataReader('GM', 'yahoo', start, end)
gm.head()


# In[40]:


tesla['Open'].plot(label='Tesla', figsize=(16,8), title='Open Price')
ford['Open'].plot(label='FORD')
gm['Open'].plot(label='GM')
plt.legend();


# In[41]:


tesla['Volume'].plot(label='Tesla', figsize=(16,8), title='Volume')
ford['Volume'].plot(label='FORD')
gm['Volume'].plot(label='GM')
plt.legend();


# In[42]:


ford['Volume'].idxmax()


# In[43]:


gm['Volume'].idxmax()


# In[44]:


tesla['Volume'].idxmax()


# In[45]:


tesla['Total Traded'] = tesla['Open'] * tesla['Volume']
ford['Total Traded'] = ford['Open'] * ford['Volume']
gm['Total Traded'] = gm['Open'] * gm['Volume']


# In[46]:


tesla['Total Traded'].plot(label='Tesla', figsize=(16,8))
ford['Total Traded'].plot(label='FORD')
gm['Total Traded'].plot(label='GM')
plt.legend()
plt.ylabel('Total Traded')


# In[47]:


tesla['Total Traded'].idxmax()


# In[48]:


gm['MA50'] = gm['Open'].rolling(50).mean()
gm['MA200'] = gm['Open'].rolling(200).mean()
gm[['Open', 'MA50', 'MA200']].plot(label='GM', figsize=(20,15));


# In[49]:


from pandas.plotting import scatter_matrix


# In[50]:


car_comp = pd.concat([tesla['Close'], ford['Close'], gm['Close']], axis=1)
car_comp.columns= ['Tesla Close', 'Ford Close', 'GM Close']


# In[51]:


scatter_matrix(car_comp, figsize=(10,10), alpha=0.1, hist_kwds={'bins':50});


# In[52]:


pip install mpl_finance


# In[53]:


from mpl_finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DateLocator, MONDAY


# In[54]:


pip install --upgrade mplfinance


# In[55]:


from mpl_finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DateLocator, MONDAY


# In[56]:


ford_reset = ford.loc['2018-12':'2019-02'].reset_index()
ford_reset['date_ax']= ford_reset['Date'].apply(lambda date: date2num(date))


# In[58]:


ford_reset.head()


# In[59]:


list_of_cols = ['date_ax', 'Open', 'High', 'Low', 'Close']
ford_values = [tuple(vals) for vals in ford_reset[list_of_cols].values]


# In[60]:


mondays = WeekdayLocator(MONDAY)
alldays = DateLocator()
weekFormatter = DateFormatter('%b %d')
dayFormatter = DateFormatter('%d')


# In[61]:


fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_major_formatter(weekFormatter)

candlestick_ohlc(ax, ford_values, width = 0.6, colorup='g', colordown='r');


# In[62]:


tesla['returns'] = tesla['Close'].pct_change(1)
ford['returns'] = ford['Close'].pct_change(1)
gm['returns'] = gm['Close'].pct_change(1)


# In[63]:


tesla.head()


# In[64]:


ford.head()


# In[65]:


gm.head()


# In[66]:


ford['returns'].hist(bins=100);


# In[67]:


gm['returns'].hist(bins=100);


# In[68]:


tesla['returns'].hist(bins=50);


# In[70]:


tesla['returns'].hist(bins=50, label='Tesla', figsize=(10,8), alpha = 0.5)
gm['returns'].hist(bins=50, label= 'GM', alpha = 0.5)
ford['returns'].hist(bins=50, label= 'FORD', alpha = 0.5)
plt.legend();


# In[79]:


pip install --upgrade --force-reinstall scipy


# In[80]:


tesla['returns'].plot(kind='kde', label='Tesla', figsize=(10,8), alpha = 0.5)
gm['returns'].plot(kind='kde', label='GM', alpha = 0.5)
ford['returns'].plot(kind='kde', label='FORD', alpha = 0.5)
plt.legend();


# In[81]:


box_df = pd.concat([tesla['returns'],gm['returns'],ford['returns']],axis=1)
box_df.columns = ['Tesla Returns', 'GM Returns', 'Ford Returns']
box_df.plot(kind='box', figsize=(8,11), colormap= 'jet');


# In[82]:


scatter_matrix(box_df, figsize=(8,8), alpha=0.2, hist_kwds={'bins':50});


# In[83]:


box_df.plot(kind='scatter', x= 'GM Returns', y='Tesla Returns', alpha=0.4, figsize=(10,8));


# In[84]:


tesla['Cumulative Return'] = (1+ tesla['returns']).cumprod()
ford['Cumulative Return'] = (1+ ford['returns']).cumprod()
gm['Cumulative Return'] = (1+ gm['returns']).cumprod()


# In[85]:


tesla.head()


# In[86]:


ford.head()


# In[87]:


gm.head()


# In[88]:


tesla['Cumulative Return'].plot(label='Tesla', figsize=(16,8), title = 'Cumulative Return')
ford['Cumulative Return'].plot(label='Ford')
gm['Cumulative Return'].plot(label='GM')
plt.legend();


# In[ ]:




