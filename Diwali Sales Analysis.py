#!/usr/bin/env python
# coding: utf-8

# ## Diwali Sales Analysis
# 
# #### Project by: Anish Deshpande

# In[1]:


# Importing necessary liraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Loading the dataset

df = pd.read_csv('Diwali Sales Data.csv',header=0,encoding='latin1')


# In[3]:


# Let's have a glance at our dataset

df.head()


# ## Data Exploring

# In[4]:


# checking the number of rows and columns in our dataset

df.shape


# In[5]:


# Check the overall entries

df.size


# In[6]:


# Let's inspect the dtypes for all olumns 

df.info()


# In[7]:


# Statistical view of the numerical columns

df.describe()


# ## Data Cleaning

# In[8]:


# First thing we can see is there are two empty columns that is Status and unnamed1. We need to drop them

df.drop(columns=['Status','unnamed1'],inplace=True)


# In[9]:


# Let's check for null values

df.isna().sum() /len(df)        # There are few null values in the Amount column. Let's look at them


# In[10]:


df[df["Amount"].isna()]         # These are Missing completely at random and since these null values constitutes 
                                # only upto 0.001%. Let's go ahead and drop them


# In[11]:


# Dropping the null values

df = df.dropna()


# In[12]:


# Let's check again for null values

df.isna().sum()


# Perfect!

# In[13]:


df.head(10)


# In[14]:


# Let's change the dtype of Amount column to int

df['Amount'] = df['Amount'].astype('int')


# ## Data Visualization

# ### Univariate Analysis

# Gender 

# In[15]:


sns.countplot(data=df,x='Gender')
plt.show()


# - Females shop more than men

# Age Group

# In[16]:


plt.figure(figsize=[15,5])

plt.subplot(1,2,1)
sns.countplot(data = df,x='Age Group',hue='Gender')

plt.subplot(1,2,2)
sns.histplot(df['Age'])
plt.show()


# - Maximum shopping is done by youngsters aged between 26 to 35, followerd by 36-45 and 18-25
# - People of age 29 can be considered as shopoholic

# Occupation

# In[17]:


sns.countplot(data=df,x='Occupation')
plt.xticks(rotation=90)
plt.show()


# State

# In[18]:


plt.figure(figsize=[15,5])
sns.countplot(data=df,x='State',hue='Gender')
plt.xticks(rotation=90)
plt.show()


# - Maximum shoppers are from Uttar pradesh followed by Maharashtra and Karnataka

# Zone

# In[19]:


sns.countplot(data=df,x='Zone',hue='Gender')
plt.show()


# - Central Zone and Southern regions have higher number of people who shop

# ### Bivariate Analysis

# Gender vs Amount

# In[20]:


df_gender = df.groupby(by="Gender")["Amount"].sum()

df_gender = df_gender.reset_index()

print(df_gender)

sns.barplot(data = df_gender,x='Gender',y='Amount')
plt.show()


# Product_category vs Amount

# In[21]:


df_category = df.groupby(by='Product_Category')['Amount'].sum()

df_category = df_category.reset_index().sort_values('Amount',ascending=False)

plt.figure(figsize=[10,5])
sns.barplot(data=df,x='Product_Category',y='Amount')
plt.xticks(rotation=90)
plt.show()


# State vs Orders

# In[22]:


df_state = df.groupby("State")["Orders"].sum()

df_state = df_state.reset_index()

df_state = df_state.sort_values("Orders",ascending=False)

plt.figure(figsize=[15,5])
sns.barplot(data=df_state,x='State',y='Orders')
plt.xticks(rotation=90)
plt.show()


# Product_ID vs Orders

# In[23]:


df_product = df.groupby(by='Product_ID')['Orders'].sum()

df_product = df_product.reset_index().sort_values('Orders',ascending=False)

df_product_top5 = df_product.iloc[0:5,:]

sns.barplot(data=df_product_top5,x='Product_ID',y='Orders')
plt.show()


# - P00265242,P00110942,P00237542,P00184942,P00114942 are the top 5 most popular products

# USER_ID vs Orders and USER_ID vs Amount

# In[24]:


df_users = df.groupby('User_ID')[["Orders","Amount"]].sum()

df_users = df_users.reset_index()

df_users = df_users.sort_values("Amount",ascending=False)

top_25_users = df_users.iloc[0:25,:]

plt.figure(figsize=[15,5])
sns.barplot(data=top_25_users,x='User_ID',y='Amount')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=[15,5])
sns.barplot(data=top_25_users,x='User_ID',y='Orders')
plt.xticks(rotation=90)
plt.show()


# ## Conclusion

# - Company should target people of age 26 to 35,36-45 and 18-25 as they are active shoppers
# - Uttar pradesh has the highest shoppers and highest number of orders followed by maharashtra and karnataka 
# - Central Zone and Southern regions have higher number of people who shop
# - Product Category named Auto has the highest sales
# - P00265242,P00110942,P00237542,P00184942,P00114942 are the 5 most popular products
# - We can see the top 25 customers with highest orders. The company can offer them some sort of premium cards that will make them to continue shopping  
