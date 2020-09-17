#!/usr/bin/env python
# coding: utf-8

# # User Engagement Analysis using Python and Tableau

# In[ ]:


#importing Libraries 
import pandas as pd 
import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


#Creating a Dataframe 
data = pd.read_csv('/Users/vaardanchennupati/Desktop/showwcase/showwcase_sessions.csv')


# ## Data Statistics 

# In[ ]:


# Column name in the dataset
data.columns


# In[ ]:


#Lets get the shape of the DataFrame
data.shape


# In[ ]:


data.head()


# In[ ]:


data.tail()


# In[ ]:


# Structure of the DataFrame
data.info()


# In[ ]:


# Now lets look into some Statistics of the dataset
data.describe()


# ## Data Cleaning
# (Checking for Missing values in the dataset)
# 

# In[ ]:


#checking for missing values
data.isnull().sum()


# In[ ]:



data[data.isna().any(axis=1)]


# In[ ]:


#droping column with nan
data = data.drop([300,301],axis=0)


# In[ ]:


#after removing the (Columns with null values)
data.tail()


# From the above table we can confirm that there are three rows that has Null values(NaN),So we will be droping it. 

# In[ ]:


#checking again
data[data.isna().any(axis=1)]


# We can observe that there is one value missing in the column session_likes_given, and from the column likes_given we can see that the boolean value is False which mean the customer has not given any likes in this session. So we replace the NaN with zero

# In[ ]:


#replacing the value with zero
data['session_likes_given'] = data['session_likes_given'].fillna(0)


# In[ ]:


#cross- checking agian for null values
data.isnull().sum()


# In[ ]:


#converting Boolen to INT
data = np.multiply(data, 1)


# In[ ]:


#Converting date
data['login_date']=pd.to_datetime(data['login_date'])


# In[ ]:


# converting the data farme to int 
data['session_id']=data['session_id'].astype(int)
data['customer_id']=data['customer_id'].astype(int)
data['projects_added']=data['projects_added'].astype(int)
data['likes_given']=data['likes_given'].astype(int)
data['comment_given']=data['comment_given'].astype(int)
data['inactive_status']=data['inactive_status'].astype(int)
data['bug_occured']=data['bug_occured'].astype(int)
data['session_projects_added']=data['session_projects_added'].astype(int)
data['session_likes_given']=data['session_likes_given'].astype(int)
data['session_comments_given']=data['session_comments_given'].astype(int)
data['inactive_duration']=data['inactive_duration'].astype(int)
data['bugs_in_session']=data['bugs_in_session'].astype(int)
data['session_duration']=data['session_duration'].astype(int)


# In[ ]:



data.info()


# In[ ]:


#exporting the datafram for visulization in tableau
data.to_csv(r'/Users/vaardanchennupati/Desktop/showwcase/showwcase.csv', index = False)


# ## Data Visualization 

# ### Data Visualization Is done By using python and Tableau
# I have also attached the link to Tableau Dashboard for more Visualization. 
#     Tableau Dashboard Link: https://public.tableau.com/profile/vardan.chennupati#!/vizhome/Showwcase_16003069170040/Dashboard1?publish=yes
#     
#    Coming to Visulaization using python I have Created 5 Bar plot using Seaborn Library and Matplotlib.
#    

# In[ ]:


by_customer = data.groupby("customer_id")


# In the above Code we Use GROUPBY Function to group all Unique customer Id and sum them up.

# In[ ]:


by_customer=by_customer.sum()


# In[ ]:


# Creating a new column called CUSTOMER_SESSION_TOTALTIME Which show the total session login of the customer
by_customer['customer_session_totaltime']=by_customer['session_duration']+by_customer['inactive_duration']


# In[ ]:


top_projects=by_customer.sort_values(by='session_projects_added', ascending=False).head(10).reset_index()
top_projects


# In[ ]:


#top 10 Customer_Id with Most projects
plt.figure(figsize=(12,5),dpi= 100)

ax = sns.barplot(y="session_projects_added", x = "customer_id", data =top_projects, palette=("Blues_d"),order=top_projects.sort_values('session_projects_added',ascending = False).customer_id)
ax.set(xlabel="Customer_ID", ylabel='Number of Projects added By the customer',title='Top 10 customer_id with most projects')
for i, v in enumerate(top_projects["session_projects_added"].iteritems()):        
    ax.text(i ,v[1], "{:,}".format(v[1]), color='black', va ='bottom')
plt.tight_layout()
plt.show()


# In[ ]:


# Top likes given by customers
top_likes=by_customer.sort_values(by='session_likes_given', ascending=False).head(10).reset_index()


# In[ ]:


plt.figure(figsize=(12,5),dpi= 100)

ax = sns.barplot(y="session_likes_given", x = "customer_id", data =top_likes, palette=("spring"),order=top_likes.sort_values('session_likes_given',ascending = False).customer_id)
ax.set(xlabel="Customer_ID", ylabel='Number of Likes given by customer',title='Top 10 customers with most likes given')
for i, v in enumerate(top_likes["session_likes_given"].iteritems()):        
    ax.text(i ,v[1], "{:,}".format(v[1]), color='black', va ='bottom')
plt.tight_layout()
plt.show()


# In[ ]:


# Top 10 customer with most comments given

top_comments=by_customer.sort_values(by='session_comments_given', ascending=False).head(10).reset_index()


# In[ ]:


plt.figure(figsize=(12,5),dpi= 100)

ax = sns.barplot(y="session_comments_given", x = "customer_id", data =top_comments, palette=("summer"),order=top_comments.sort_values('session_comments_given',ascending = False).customer_id)
ax.set(xlabel="Customer_ID", ylabel='Number of comments given out by customer',title='Top 10 Customers with most comments given')
for i, v in enumerate(top_comments["session_comments_given"].iteritems()):        
    ax.text(i ,v[1], "{:,}".format(v[1]), color='black', va ='bottom')
plt.tight_layout()
plt.show()


# In[ ]:


#top 10 customer with most bugs in session
top_bugs=by_customer.sort_values(by='bugs_in_session', ascending=False).head(10).reset_index()


# In[ ]:


plt.figure(figsize=(12,5),dpi= 100)

ax = sns.barplot(y="bugs_in_session", x = "customer_id", data =top_bugs, palette=("ocean"),order=top_bugs.sort_values('bugs_in_session',ascending = False).customer_id)
ax.set(xlabel="Customer_ID", ylabel='Number of bugs',title='Top 10 Customers with most bug in the session')
for i, v in enumerate(top_bugs["bugs_in_session"].iteritems()):        
    ax.text(i ,v[1], "{:,}".format(v[1]), color='black', va ='bottom')
plt.tight_layout()
plt.show()


# Observation:
#     Comparing the bar graphs( Comments given and bug in session) we can see a pattern where both the graph have same customer ID but when we look closely in both the graphs we can assume that customer who gave comments are the one who had more bug in the sessions. For example Let take the customer id 23404 he had given 64 comments but he had also encountered 33 bugs in his session i.e. 50%. lets take the second highest that is 29375 comments given by this customer is 44 and the bug encountered by this customer is 26 i.e. 59%

# In[ ]:


#top 10 customers with active session usage
top_users=by_customer.sort_values(by='customer_session_totaltime', ascending=False).head(10).reset_index()


# In[ ]:


plt.figure(figsize=(12,5),dpi= 100)

ax = sns.barplot(y="customer_session_totaltime", x = "customer_id", data =top_users, palette=("inferno"),order=top_users.sort_values('customer_session_totaltime',ascending = False).customer_id)
ax.set(xlabel="Customer_ID", ylabel='Total Seconds(Sec)',title='Comparsion of Total usage of session vs Active usage of session')

ax = sns.barplot(y="session_duration", x = "customer_id", data =top_users, palette=("summer_r"),order=top_users.sort_values('customer_session_totaltime',ascending = False).customer_id)



for i, v in enumerate(top_users["session_duration"].iteritems()):        
    ax.text(i ,v[1], "{:,}".format(v[1]), color='white', va ='bottom')

for i, v in enumerate(top_users["customer_session_totaltime"].iteritems()):        
    ax.text(i ,v[1], "{:,}".format(v[1]), color='black', va ='bottom')
plt.tight_layout()
plt.show()


# Observation:
#      The Above Figure shows the comparison of total usage of session and active usaage of session by customers.
#         only Few customers are arround 70% active but most of them are arround 50% - 65% active 

# In[ ]:




