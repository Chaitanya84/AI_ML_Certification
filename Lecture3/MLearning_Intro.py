#introduction to Machine learning 
#train_test_split: helps us split our data set into a training set and a testing set
#logistic regression: a statistical method for analyzing a dataset in which there are one or more independent variables that determine an outcome

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score 

#loading the dataset
data = pd.read_csv('archive/netflix_titles.csv')
#print(data.head())

#Extract the numeric part of the 'duration' column and convert to integer
data['duration'] = data['duration'].str.extract(r'(\d+)').astype(float)  
data['duration'] = data['duration'].fillna(data['duration'].mean())
print(data['duration'].dtype)

#create a target variable Y: 1 for 'Movie' and 0 for 'TV Show'
data['target'] = data['type'].apply(lambda x: 1 if x == 'Movie' else 0) 
X = data[['duration']]  #feature
Y = data['target']      #target variable    
print(X.head())    

