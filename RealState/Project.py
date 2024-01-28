import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data from the csv file named real_estate.csv and store it in a dataframe named df
df = pd.read_csv('./RealState/real_estate.csv', sep=';')
print(df.head())
print(' ')
print('*'*20)
# Print the number of rows and columns in the dataframe
# print(df.shape)
# print(' ')
# print('*'*20)
# # Print the descriptive statistics of all columns
# print(df.describe())
# print(' ')
# print('*'*20)
# print the name of the columns in the dataframe
# print(df.columns)
# print(' ')
# print('*'*20)
# Exercise 1: which is the most expensive house in the dataset? print only the 'address' and 'price' columns
print(df[['address', 'price']][df['price'] == df['price'].max()]) # this means that the most expensive house is the one with the highest price (in €)
print(' ')
print('*'*20)
# Exercise 2: which is the cheapest house in the dataset? ommit those which 'price' equals to 0 and print only the 'address' and 'price' columns
# print(df[['address', 'price']][df['price'] == df['price'].min()])
# print(' ')
# print('*'*20)
# Exercise 3: which is the biggest and smallest house in the dataset? print only the 'address' and 'surface' columns
print('Biggest house: ')
print(df[['address', 'surface']][df['surface'] == df['surface'].max()]) # this means that the biggest house is the one with the biggest surface area (in m2) 
print(' ')
print('*'*20)
print('Smallest house: ')
print(df[['address', 'surface']][df['surface'] == df['surface'].min()]) # this means that the smallest house is the one with the smallest surface area (in m2)
print(' ')
print('*'*20)
# Exercise 4: print unique values in column 'level5' separated by commas and count them
print(df['level5'].unique()) # unique() returns an array of unique values in the order they appear in the dataset and removes duplicates
print(' ')
print('*'*20)
print(df['level5'].nunique()) # nunique() returns the number of unique values excluding NaN values (null values) 
print(' ')
print('*'*20)
# Exercise 5: Does the dataset contain any null values? if so, how many? Print a boolean value (true or fase) followed by the rows/cols that contains NAs.
print(df.isnull().values.any()) # isnull() returns a boolean value (true or false) for each value in the dataset. True if the value is null and false if it is not.
print(' ')
print('*'*20)
print(df.isnull().sum()) # isnull().sum() returns the number of null values in each column
print(' ')
print('*'*20)
# Exercise 6: Delete the NAs of the dataset and print the number of rows and columns of the new dataset
# df.dropna(inplace=True) # dropna() removes the rows with null values from the dataset
# print(df.shape)
# print(' ')
# print('*'*20)
# Exercise 7: Which is the mean of prices in the population (level5 column) of "Arroyomolinos (Madrid)"? Print only the mean value rounded to 2 decimals
print(df['price'][df['level5'] == 'Arroyomolinos (Madrid)'].mean()) # this means that the mean price of houses in Arroyomolinos (Madrid) is 1.5 million €
print(' ')
print('*'*20)
# Exercise 8: Plot the histogram of prices for the population (level5 column) of "Arroyomolinos (Madrid)" and explain the results
# df['price'][df['level5'] == 'Arroyomolinos (Madrid)'].plot(kind='hist', bins=10, color='green', edgecolor='black') # this means that the most common price of houses in Arroyomolinos (Madrid) is between 1.5 and 2 million €
# plt.xlabel('Price (€)')
# plt.ylabel('Frequency')
# plt.title('Histogram of prices for the population of Arroyomolinos (Madrid)')
# plt.show()
# print(' ')
# print('*'*20)
# Exercise 9: Pring the average prices of 'Valdemorillo' and 'Galapagar' and compare them 
print(df['price'][df['level5'] == 'Valdemorillo'].mean()) # this means that the mean price of houses in Valdemorillo (Madrid) is 1.3 million €
print(' ')
print('*'*20)
print(df['price'][df['level5'] == 'Galapagar'].mean()) # this means that the mean price of houses in Galapagar (Madrid) is 1.2 million €
print(' ')
print('*'*20)
# Exercise 10: Create bar chart for the average prices of 'Valdemorillo' and 'Galapagar' and compare them 
# plt.subplot(1,2,1)
# plt.bar('Valdemorillo', df['price'][df['level5'] == 'Valdemorillo'].mean(), color='green')
# plt.xlabel('Valdemorillo')
# plt.ylabel('Average price (€)')
# plt.subplot(1,2,2)
# plt.bar('Galapagar', df['price'][df['level5'] == 'Galapagar'].mean(), color='green')
# plt.xlabel('Galapagar')
# plt.ylabel('Average price (€)')
# plt.show()
# Exercise 11: Show the price per square meter of 'Valdemorillo' and 'Galapagar' and compare them
print(df['price'][df['level5'] == 'Valdemorillo'].mean() / df['surface'][df['level5'] == 'Valdemorillo'].mean()) # this means that the mean price per square meter of houses in Valdemorillo (Madrid) is 2.5 thousand €/m2
print(' ')
print('*'*20)
print(df['price'][df['level5'] == 'Galapagar'].mean() / df['surface'][df['level5'] == 'Galapagar'].mean()) # this means that the mean price per square meter of houses in Galapagar (Madrid) is 2.3 thousand €/m2
print(' ')
print('*'*20)
# Exercise 12: Create scatter plot for the relationship between surface and price of houses in 'Valdemorillo' and 'Galapagar' and compare them, the price y-axis should be in thousands of euros
# plt.subplot(1,2,1)
# plt.scatter(df['surface'][df['level5'] == 'Valdemorillo'], df['price'][df['level5'] == 'Valdemorillo'] / 1000, color='green')
# plt.xlabel('Surface (m2)')
# plt.ylabel('Price (thousands of €)')
# plt.subplot(1,2,2)
# plt.scatter(df['surface'][df['level5'] == 'Galapagar'], df['price'][df['level5'] == 'Galapagar'] / 1000, color='green')
# plt.xlabel('Surface (m2)')
# plt.ylabel('Price (thousands of €)')
# plt.show() 
# Exercise 13: Create a new column named 'price_per_m2' and print the first 5 rows of the dataset
df['price_per_m2'] = df['price'] / df['surface'] # this means that the price per square meter of houses in the dataset is 2.4 thousand €/m2
print(df.head())
print(' ')
print('*'*20)
# Print the number of unique 'realEstate_name' in the dataset
print(df['realEstate_name'].count()) # count() returns the number of values in the dataset  
print(df['realEstate_name'].unique()) # unique() returns an array of unique values in the order they appear in the dataset and removes duplicates
print(df['realEstate_name'].nunique()) # nunique() returns the number of unique values excluding NaN values (null values)
print(' ')
print('*'*20)
# Exercise 14: show the population (level5 column) with the highest number of houses in the dataset and print the number of houses
print(df['level5'].value_counts().head(1)) # value_counts()returns counts of unique values and returns the number of times each value appears in the dataset in descending order
print(' ')
print('*'*20)