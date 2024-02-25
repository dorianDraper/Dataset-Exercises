import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# load the data
data = pd.read_csv('Week4\Wednesday\PRODUCT SALES.csv')
# display the first 5 rows
print(data.head())
# display columns
print(data.columns)
# display the shape of the data
print(data.shape)
# display the different Product_Category
print(data['Product_Category'].unique())
# display the different Country
print(data['Country'].unique())
print('*' * 50)
# given the columns 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit', 'Cost' and 'Revenue'
# calculate the 'Cost' and 'Revenue', what is the Country with the highest 'Revenue'? 
data['Cost'] = data['Order_Quantity'] * data['Unit_Cost']
data['Revenue'] = data['Order_Quantity'] * data['Unit_Price']
print(data.groupby('Country')['Revenue'].sum()) # display the sum of 'Revenue' for each 'Country' column
print('*' * 50)
# display total 'Profit' for each 'Country' column
print(data.groupby('Country')['Profit'].sum())
print('*' * 50)
# display the Country with the highest 'Profit' 
print('The Country with the highest Profit is: ', data.groupby('Country')['Profit'].sum().idxmax(), 'with a profit of: ', data.groupby('Country')['Profit'].sum().max())

# display the Country with the highest 'Revenue'
print('The Country with the highest Revenue is: ', data.groupby('Country')['Revenue'].sum().idxmax())
print('*' * 50)
# display the mean 'Profit' for each 'Country' column
print(data.groupby('Country')['Profit'].mean())
print('*' * 50)
print(' ')
# display the mean 'Profit' for each 'Age_Group' column
print(data.groupby('Age_Group')['Profit'].mean())
# display distribution total of 'Product_Category' by 'Country' 
print('Distribution of Product_Category by Country: ')
print(data.groupby(['Country', 'Product_Category'])['Order_Quantity'].sum())
# which Country has the highest 'Order_Quantity' for 'Product_Category' = 'Bikes'? 
print('The Country with the highest Order_Quantity for Product_Category = Bikes is: ', data[data['Product_Category'] == 'Bikes'].groupby('Country')['Order_Quantity'].sum().idxmax(), 'with a total Order_Quantity of: ', data[data['Product_Category'] == 'Bikes'].groupby('Country')['Order_Quantity'].sum().max())
print('*' * 50)
print('*' * 50)
print('*' * 50)
countries = data['Country'].unique()
print(countries)
countries_profit = {} # dictionary to store the profit for each country
for country in countries:
    countries_profit[country] = data[data['Country'] == country]['Profit']
# perform ANOVA test to compare the means of 'Profit' for each 'Country'
f_statistic, p_value = stats.f_oneway(*countries_profit.values())
print(f'F-Statistic: {f_statistic}, P-Value: {p_value}')
# make conclusions based on the p-value (alpha = 0.05)
if p_value < 0.05:
    print('Reject the null hypothesis: there is a significant difference between the means of the groups')
else:
    print('Fail to reject the null hypothesis: there is no significant difference between the means of the groups')

print('*' * 50)
# print 'Age_Group' unique values
print(data['Age_Group'].unique())
# perform ANOVA test to compare the means of 'Profit' for each 'Age_Group'
age_groups = data['Age_Group'].unique()
age_groups_profit = {} # dictionary to store the profit for each age group
for age_group in age_groups:
    age_groups_profit[age_group] = data[data['Age_Group'] == age_group]['Profit']

f_statistic, p_value = stats.f_oneway(*age_groups_profit.values())
print(f'F-Statistic: {f_statistic}, P-Value: {p_value}')
# make conclusions based on the p-value (alpha = 0.05)
if p_value < 0.05:
    print('Reject the null hypothesis: there is a significant difference between the means of the groups')
else:
    print('Fail to reject the null hypothesis: there is no significant difference between the means of the groups')

print('*' * 50)


