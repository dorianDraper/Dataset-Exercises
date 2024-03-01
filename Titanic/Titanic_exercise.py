import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('Exercises with Pandas')
print('*********************')

titanic_df = pd.read_csv('https://raw.githubusercontent.com/mrBronnWow/Curso_Beginners/main/1_Dataset_titanic/train.csv')
print(titanic_df.head())
print(' ')
print('*********************')
# show columns of the dataframe
print('Exercise 01: Show the columns of the dataframe')
print(titanic_df.columns)
print(' ')
print('*********************')
# describe the dataframe
print('Exercise 02: Describe the dataframe')
print(titanic_df.describe())
print(' ')
print('*********************')
# drop columns 'Ticket', 'Cabin', 'PassengerId'
print('Exercise 03: Drop columns Ticket, Cabin, and PassengerId')
titanic_df.drop(['Ticket', 'Cabin', 'PassengerId'], axis=1, inplace=True)
print(titanic_df.head())
print(' ')
print('*********************')
# plot bar with the number of survivors and deads
print('Exercise 04: Plot bar with the number of survivors and deads')
survived = pd.value_counts(titanic_df['Survived']).plot.bar()
plt.show()
print(' ')
print('*********************')
# mean of survivors
print('Exercise 05: Mean of survivors')
print(titanic_df['Survived'].mean()) 
print(' ')
print('*********************')
# given the number of survivors and deads, calculate the percentage of survivors by class and sex
print('Exercise 06: Given the number of survivors and deads, calculate the percentage of survivors by class and sex')
print(' ')
print('*********************')
# calculate the mean of the age of the survivors
print('Exercise 07: Calculate the mean of the age of the survivors')
print(titanic_df.loc[titanic_df['Survived'] == 1]['Age'].mean())
print(' ')
print('*********************')
# calculate the mean of the age of the deads
print('Exercise 08: Calculate the mean of the age of the deads')
print(titanic_df.loc[titanic_df['Survived'] == 0]['Age'].mean())
print(' ')
print('*********************')
# calculate the mean of the age of the survivors by class
print('Exercise 09: Calculate the mean of the age of the survivors by class')
print(titanic_df.loc[titanic_df['Survived'] == 1].groupby('Pclass')['Age'].mean())
print(' ')
print('*********************')
