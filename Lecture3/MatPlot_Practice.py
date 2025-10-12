import matplotlib.pyplot as plt
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv) 

df = pd.read_csv('archive/netflix_titles.csv')
#counts = df[['country','type']].value_counts().head(5)
#counts.plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'])
#plt.title('Number of Movies vs TV Shows on Netflix')
#plt.xlabel('Type')
#plt.ylabel('Count')
#plt.show() 

#top 5 primary genre in the dataset
df_exploded = df.assign(listed_in=df['listed_in'].str.split(', ')).explode('listed_in')
genre_counts = df_exploded['listed_in'].value_counts().head(5)
genre_counts.plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'])
plt.title('Top 5 Genres on Netflix')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show()  