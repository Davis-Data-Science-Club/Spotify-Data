#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd #RUN EVERYTIME
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


# In[8]:


get_ipython().system('pip install pandas #RUN EVERYTIME')


# In[9]:


df = pd.read_csv('/Users/eric/Documents/GitHub/Spotify-Data/songs_normalize.csv') #RUN EVERYTIME


# In[10]:


df.head()


# In[11]:


df.describe() #general stats


# In[12]:


df.columns


# In[13]:


df.shape # (rows,columns)


# In[14]:


df.loc[0:4] #indexing first 5 rows, remember cs index starts at 0


# In[15]:


df.loc[0:4, "artist":"explicit"] #first half is rows, second half is colums 


# In[16]:


df.loc[25:30]


# In[17]:


df.loc[:, "artist":"explicit"] # no index for the rows, gives us all the columns


# In[18]:


df.loc[100:105,["artist","song"]] #makes a list of two columns


# In[19]:


df.loc[100:105,["artist","explicit"]]


# In[20]:


df.loc[100:105,"artist"] #only look at 1 column


# In[21]:


df.iloc[0:5] #only accepts numbers as input #slice works differently, cuts off last value


# In[22]:


df.iloc[0:5,0] #We can still take the columns, just have to use numbers


# In[23]:


df[0:5] # slice and row of indexes without loc, cuts off last value like iloc, only take in one argument


# In[24]:


df[["artist","duration_ms"]] #just for rows


# In[25]:


df["song"]


# In[26]:


df["artist"]=='Britney Spears' # creates a boolean, true each time Artist is Britney Spears


# In[27]:


sum(df["artist"]=='Britney Spears') #Gives out the sum how many times Britney Spears is in dataset


# In[28]:


df.loc[df["artist"]=='Britney Spears'] # gives us a column and row for each time britney is the artist


# In[29]:


df[df["danceability"]>0.90] #finds every song wit value greater than


# In[30]:


df.loc[(df["year"]==2019) &  (df["danceability"]>0.90) ] #every song from 2019 where danceability>.90


# In[31]:


df.loc[df["artist"]=="Taylor Swift", ["artist", "song", "popularity", "year"]] #gets the specific songs and gives the columns


# In[32]:


artists_i_like=['Taylor Swift', 'Britney Spears']
df[df['artist'].isin(artists_i_like)]
#create a variable, creates a list with artists selected, second line 'isin' puts the dataset into the variable


# In[34]:


df['artist'].str.startswith('A') # returns boolean values for all the artists that start with A
df[df['artist'].str.startswith('B')] # returns all the artists thats start with the B


# In[35]:


df.query("artist=='Taylor Swift' and danceability>0.5") #filters, needs to input a string, 
#finds all taylor swift songs with danceability>0.5


# In[40]:


df.groupby('year')
df.groupby('year').mean()
#groups the dataset, first code only returns an object, needs an aggregate after like mean 

df.groupby('year').max()
df.groupby('year').sum()


# In[42]:


df.groupby('year')[['duration_ms', 'danceability']].mean()

#just a specific column


# In[46]:


df.groupby('genre')['popularity'].mean().sort_values(ascending=False)
#sort by a specific column, finds the most popular song, ascending=false means greatest to least


# In[48]:


df.groupby('year')[['popularity','loudness']].mean().sort_values(by='popularity', ascending=False)

# same thing as before, by populairty is to clairfy which column in our list to ascending


# In[49]:


df['artist'].value_counts()
#number of times an artist shows up in our dataset


# In[50]:


df['year'].value_counts()

#shows the amount of songs in the dataset


# In[51]:


df['genre'].value_counts()


# In[55]:


df['artist'].unique()
#finds how many unique artists, each time they show up

len(df['artist'].unique())
#finds the number of artists

len(df['genre'].unique())



# In[57]:


df.sort_values('artist')

# sorts the artists


df.sort_values('popularity')


# In[66]:


plt.figure(figsize=(15,8))
#matplotlib create different dimensions

plt.xticks(rotation=90)
#to see the values label on the x axis

sns.countplot(x='genre',data=df)
#seaborn, creates a plot


# In[72]:


fig=px.histogram(df,x='genre',title="Distribution of Genre") #creates a variable
#plotly histogram

fig.update_xaxes(categoryorder='total ascending') #put in order


fig.show() #to actually show the histogram


# In[74]:


plt.figure(figsize=(15,8))
sns.histplot(df['danceability'])
sns.histplot(x='danceability',data=df)
#creates a histogram for dancebility


# In[76]:


plt.figure(figsize=(15,8))
sns.histplot(x='danceability',data=df,binwidth=.05)
sns.histplot(x='danceability',data=df,bins=30)


# In[78]:


plt.figure(figsize=(15,8))

sns.histplot(x='danceability',data=df,bins=20,kde=True,stat='density')
#kernel density estimate


# In[82]:


fig=px.histogram(df,x='danceability', title="Distrubution of Density")
fig.update_layout(bargap=0.1)
fig.show()

#plotly histogram


# In[ ]:




