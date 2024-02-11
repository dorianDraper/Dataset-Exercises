import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data from the csv file named real_estate.csv and store it in a dataframe named df
df = pd.read_csv('./RealEstate/real_estate.csv', sep=';')
print(df.head())
print(' ')
print('*'*20)
# print the most expensive house in the dataset, print only the address and the price columns in a sentence like "the most expensive house is located at <address> and costs <price> dollars"
print('The most expensive house is located at', df.loc[df['price'].idxmax()]['address'], 'and costs', df['price'].max(), 'dollars')
print(' ')
print('*'*20)
# print the cheapest house in the dataset, print only the address and the price columns in a sentence like "the cheapest house is located at <address> and costs <price> dollars"
print('The cheapest house is located at', df.loc[df['price'].idxmin()]['address'], 'and costs', df['price'].min(), 'dollars')
print(' ')
print('*'*20)
# print biggest house in dataset in terms of 'surface' column and print only the address and the surface columns in a sentence like "The biggest house is located at <address> and has <surface> square meters"
print('The biggest house is located at', df.loc[df['surface'].idxmax()]['address'], 'and has', df['surface'].max(), 'square meters')
print(' ')
print('*'*20)
# print the smallest house in dataset in terms of 'surface' column and print only the address and the surface columns in a sentence like "The smallest house is located at <address> and has <surface> square meters"
print('The smallest house is located at', df.loc[df['surface'].idxmin()]['address'], 'and has', df['surface'].min(), 'square meters')
print(' ')
print('*'*20)
# # how many populations 'level5' column? print name of populations with comma as separator
# print('The populations in level5 are:', ', '.join(df['level5'].unique()))
# print(' ')
# print('*'*20)
# # count number of populations from prevuios question
# print('The number of populations in level5 are:', df['level5'].nunique())
# print(' ')
# print('*'*20)
# Does the dataset contain NAs? Print a boolean value (true or fase) followed by the rows/cols that contains NAs. 
print('Does the dataset contain NAs?', df.isnull().values.any())
print(' ')
print('*'*20)
print('The rows and columns that contains NAs are:')
print(df.isnull().sum())
print(' ')
print('*'*20)
# # Delete the NAs from the dataset and print a comparison between the dimensions of the original dataset versus the new dataset after the deletion
# print('The original dataset dimensions are:', df.shape)
# df = df.dropna()
# print('The new dataset dimensions are:', df.shape)
# print(' ')
# print('*'*20)
# Which is the mean of prices in the population (level5 column) of "Arroyomolinos (Madrid)"? prrint the result in a sentence like "The mean of prices in the population of Arroyomolinos (Madrid) is <mean>"
# print('The mean of prices in the population of Arroyomolinos (Madrid) is', df[df['level5'] == 'Arroyomolinos (Madrid)']['price'].mean())
# print(' ')
# print('*'*20)
# # Plot the histogram of prices for the population (level5 column) of "Arroyomolinos (Madrid)" and explain the results
# df[df['level5'] == 'Arroyomolinos (Madrid)']['price'].hist()
# plt.show()
# Print the average prices for the populations 'Valdemorillo' and 'Galapagar' and compare them in a sentence like "The average price in Valdemorillo is <mean1> and the average price in Galapagar is <mean2>"
print('The average price in Valdemorillo is', df[df['level5'] == 'Valdemorillo']['price'].mean(), 'and the average price in Galapagar is', df[df['level5'] == 'Galapagar']['price'].mean())
print(' ')
print('*'*20)
# Print the price per square meter of 'Valdemorillo' in a sentence like "The price per square meter in Valdemorillo is <price>"
print('The price per square meter in Valdemorillo is', df[df['level5'] == 'Valdemorillo']['price'].mean() / df[df['level5'] == 'Valdemorillo']['surface'].mean())
print(' ')
# Print the price per square meter of 'Galapagar' in a sentence like "The price per square meter in Galapagar is <price>"
print('The price per square meter in Galapagar is', df[df['level5'] == 'Galapagar']['price'].mean() / df[df['level5'] == 'Galapagar']['surface'].mean())
print(' ')
# # print a column named 'price_per_m2' to compare the price per square meter of Valdemorillo and Galapagar
# df['price_per_m2'] = df['price'] / df['surface']
# print(df.head())
# print(' ')
# # Create scatter plot for the relationship between surface and price of houses in 'Valdemorillo' and 'Galapagar' and subplots for each population
# fig, ax = plt.subplots(1, 2, figsize=(10, 5))
# df[df['level5'] == 'Valdemorillo'].plot.scatter(x='surface', y='price', ax=ax[0])
# df[df['level5'] == 'Galapagar'].plot.scatter(x='surface', y='price', ax=ax[1])
# plt.show()
# print the number of unique real estate agencies in the dataset
print('The number of unique real estate agencies in the dataset is:', df['realEstate_name'].nunique())
print(' ')
print('*'*20)
# print the population (level5 column) that contains the most houses
print('The population that contains the most houses is:', df['level5'].value_counts().idxmax())
print(' ')
print('*'*20)
# Make a subset of the original DataFrame that contains the following populations (level5 column): "Fuenlabrada","Leganés","Getafe","Alcorcón"
df_subset = df[df['level5'].isin(["Fuenlabrada","Leganés","Getafe","Alcorcón"])]
print(df_subset)
print(' ')
print('*'*20)
# Make a bar plot of the median of the prices for the subset of the previous question
# df_subset.groupby('level5')['price'].median().plot(kind='bar')
# plt.show()
# print(' ')
# print('*'*20)
# Calculate the sample mean and variance of the variables price, rooms, surface and bathrooms for the subset of the previous question
print('The sample mean of the variables price, rooms, surface and bathrooms for the subset of the previous question are:')
print(df_subset[['price', 'rooms', 'surface', 'bathrooms']].mean())
print(' ')
print('*'*20)
print('The sample variance of the variables price, rooms, surface and bathrooms for the subset of the previous question are:')
print(df_subset[['price', 'rooms', 'surface', 'bathrooms']].var())
print(' ')
print('*'*20)
# print the most expensive house for each population in the subset of the previous question in a sentence like "The most expensive house in <population> is located at <address> and costs <price> dollars"
print('The most expensive house in Fuenlabrada is located at', df_subset[df_subset['level5'] == 'Fuenlabrada'].loc[df_subset[df_subset['level5'] == 'Fuenlabrada']['price'].idxmax()]['address'], 'and costs', df_subset[df_subset['level5'] == 'Fuenlabrada']['price'].max(), 'dollars')
print('The most expensive house in Leganés is located at', df_subset[df_subset['level5'] == 'Leganés'].loc[df_subset[df_subset['level5'] == 'Leganés']['price'].idxmax()]['address'], 'and costs', df_subset[df_subset['level5'] == 'Leganés']['price'].max(), 'dollars')
print('The most expensive house in Getafe is located at', df_subset[df_subset['level5'] == 'Getafe'].loc[df_subset[df_subset['level5'] == 'Getafe']['price'].idxmax()]['address'], 'and costs', df_subset[df_subset['level5'] == 'Getafe']['price'].max(), 'dollars')
print('The most expensive house in Alcorcón is located at', df_subset[df_subset['level5'] == 'Alcorcón'].loc[df_subset[df_subset['level5'] == 'Alcorcón']['price'].idxmax()]['address'], 'and costs', df_subset[df_subset['level5'] == 'Alcorcón']['price'].max(), 'dollars')
print(' ')
print('*'*20)
# # print normalization of the variable 'price' for each population and plot 4 histograms in the same plot for the subset of the previous question
# print('The normalization of the variable price for each population is:')
# print(df_subset.groupby('level5')['price'].apply(lambda x: (x - x.min()) / (x.max() - x.min())))
# print(' ')
# print('*'*20)
# df_subset.groupby('level5')['price'].apply(lambda x: (x - x.min()) / (x.max() - x.min())).hist()
# plt.show()
# print(' ')
# print('*'*20)
# # using the previous subset, do the normalization of prices for each population and plot 4 histograms in the same plot
# Compare the price per square meter between the populations 'Getafe' and 'Alcorcón' from the subset of the previous question, print the values in a new column named 'price_per_m2'
df_subset['price_per_m2'] = df_subset['price'] / df_subset['surface']
print(df_subset)
print(' ')
print('*'*20)
# print the price per square meter of 'Getafe' and 'Alcorcón' from the subset of the previous question
print('The price per square meter of Getafe is', df_subset[df_subset['level5'] == 'Getafe']['price_per_m2'].mean(), 'and the price per square meter of Alcorcón is', df_subset[df_subset['level5'] == 'Alcorcón']['price_per_m2'].mean())
print(' ')
print('*'*20)
# create new subset of the original dataset with 4 populations from level5 column
df_subset2 = df[df['level5'].isin(["Navalcarnero","Parla","Madrid Capital","San Sebastián de los Reyes"])]
print(df_subset2)
print(' ')
print('*'*20)
# using df_subset2, make a bar plot of the median of the prices
df_subset2.groupby('level5')['price'].median().plot(kind='bar')
plt.show()
# using df_subset make a plot of the coordinates (latitude and longitude columns) by color of each population (level5 column)
df_subset.plot.scatter(x='latitude', y='longitude', c='level5')
plt.show()


