import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from ./WHO-COVID-19-global-data.csv
df = pd.read_csv('./Covid19/WHO-COVID-19-global-data.csv')
print(df.head())
print('*********************') 
# Print the number of rows and columns
print(df.shape)
print('*********************')