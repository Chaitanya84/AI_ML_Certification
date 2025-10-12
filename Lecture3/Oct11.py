# WHat percentage of catalog are Movies vs TV Shows
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('archive'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


df = pd.read_csv('archive/netflix_titles.csv')
#what percentage of catalog are Movies vs TV Shows
type_counts = df['type'].value_counts()
total_count = df.shape[0]
movie_percentage = (type_counts['Movie'] / total_count) * 100
tvshow_percentage = (type_counts['TV Show'] / total_count) * 100   
print(f"Percentage of Movies: {movie_percentage:.2f}%")
print(f"Percentage of TV Shows: {tvshow_percentage:.2f}%")

#which 10 genre apprears most in the dataset
# first we need to split the 'listed_in' column by comma and explode it
df_exploded = df.assign(listed_in=df['listed_in'].str.split(', ')).explode('listed_in')
genre_counts = df_exploded['listed_in'].value_counts().head(10)
print("Top 10 genres:")
print(genre_counts) 

#in whcih years most number of movies were released
#movie_year_counts = df[df['type'] == 'Movie']['release_year'].value_counts().head(10)
movie_year_counts = df['release_year'].value_counts().head(10)
print("Years with most number of movie releases:")
print(movie_year_counts)    

#top 5 countries producing most number of ttitles
df['country'] = df['country'].fillna('Unknown')
country_counts = df['country'].value_counts().head(5)
print("Top 5 countries producing most number of titles:")
print(country_counts)