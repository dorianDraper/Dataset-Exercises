import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the csv file
df = pd.read_csv('./Starbucks_Customer_Data/profile.csv')

# Display the first few rows of the dataframe
print(df.head())
print(df.shape)