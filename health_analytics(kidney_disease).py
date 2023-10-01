#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


data = pd.read_csv("kidney_disease.csv")
data.head()


# In[3]:


# summary statistics

data.describe()


# In[4]:


# display all the column names in the data

data.columns


# In[9]:


# Display the counts of each value in the bp column

data['bp'].value_counts()


# In[12]:


# plot the value counts of bp 
data['bp'].value_counts().plot.bar()


# In[10]:


# Display the counts of each value in the sugar column

data['sugar'].value_counts()


# In[11]:


# plot the value counts of sugar 
data['sugar'].value_counts().plot.bar()


# In[18]:


# plot the value counts of classification (chronical kidney disease or not) 
data['classification'].value_counts().plot.bar()


# In[5]:


# mean, median and mode of the age distribution
print("Mean: {}".format(data['age'].mean()))
print("Median: {}".format(data['age'].median()))
print("Mode: {}".format(data['age'].mode()))


# In[6]:


# top 10 ages
data['age'].value_counts().head(10)


# In[7]:


# better looking boxplot (using seaborn) for age variable
sns.boxplot(data['age'])


# In[13]:


# subset involving only records of normal pus cells
data[data['pus_cells']=='normal'].head()


# In[14]:


# subset involving only records of abnormal pus cells
data[data['pus_cells']=='abnormal'].head()


# In[16]:


# Most common bp by age
for i in data['age'].unique():
    print("Age: {} Count: {}".format(i,data[data['age']==i]['bp'].value_counts().head(1)))


# In[17]:


# group by classification to get mean statistics
data.groupby('classification').mean()


# In[ ]:




