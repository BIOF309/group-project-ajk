# import packages

import pandas as pd
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# import excel file and create dataframe called NCHS

df = 'NCHS_-_Leading_Causes_of_Death__United_States.csv'
NCHS = pd.read_csv(df)

# view NCHS columns
NCHS_columns1 = pd.read_csv(df, index_col=0)
print(NCHS_columns1.head(10296))

# view number of rows and columns
NCHS_columns1.shape
print(NCHS_columns1.shape)

# Pie chart for distribution by activity code
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red','green','blue','orange','white','brown']
NCHS['Actv'].value_counts().plot(kind='pie',title='Activity',colors=colors)
plt.show()






