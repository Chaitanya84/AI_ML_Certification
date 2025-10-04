# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('archive'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


df = pd.read_csv('archive/netflix_titles.csv')
#df.head()
# print(df.head())
# print(df.info())
# print(df.tail())

print(df[['title','country']].head(10))

#  Finding missing values in a dataframe
print(df.isnull().sum())
print(df['country'].isnull().sum())

#handling missing values
#Fill missing values with a specific value
df['country'] = df['country'].fillna('Unknown')
print(df['country'].isnull().sum()) # it should be 0 now

# Filtering for TV shows produced in india
india_tvshows = df[(df['country'] == 'India') & (df['type'] == 'TV Show')]
#write to a csv file
india_tvshows.to_csv('india_tvshows.csv', index=False)

#Filter for movies released after 2015
recent_movies = df[(df['type'] == 'Movie') & (df['release_year'] > 2015)]
#Write to a csv file
recent_movies.to_csv('recent_movies.csv', index=False)


# count the number of movies and TV shows in the dataset
print("Number of movies: ", df[df['type'] == 'Movie'].shape[0])
print("Number of TV shows: ", df[df['type'] == 'TV Show'].shape[0])
#print(df['type'].value_counts())

# Numpy operation on dataframe column
release_years = df['release_year'].values  # convert to numpy array
print("Release years: ", release_years)
print("Mean release year: ", np.mean(release_years))
print("Max release year: ", np.max(release_years))
print("Min release year: ", np.min(release_years)) 
print("Standard deviation of release years: ", np.std(release_years)) 
#print(recent_movies[['title', 'release_year']].head(10))    # You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session