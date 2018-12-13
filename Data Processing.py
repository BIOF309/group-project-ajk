# import packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import excel file and create dataframe called NCHS

NCHS = pd.read_csv('NCHS_-_Leading_Causes_of_Death__United_States.csv')

# examine the data

NCHS.info()

'''
Select the column names of interest.
Group this new dataset by year and by cause name to create the x-axis and different types in each bar in bar plot
Sum this new group to create the y-axis in bar plot
'''
year = NCHS[['Cause Name', 'Year', 'Deaths']]

year_group = year.groupby(['Year','Cause Name'])

year_group_total = year_group.sum()

"""

print(year_group_total)
print(year_group_total.unstack())           -> Print this code to see what the individual statistics that is being summarized in graph


"""


"""
Create a bar graph of the group of deaths due to cause names in each year

"""

barplot = year_group_total.unstack().plot(kind='bar',stacked=True,title='Number of Deaths by Cause Name each year (1999-2016)',figsize=(9,7))
barplot.set_xlabel('Year')
barplot.set_ylabel('Deaths')
barplot.set_ylim((0,10000000))
barplot.legend(["All causes","Alzheimer's disease","CLRD","Cancer", "Diabetes","Heart disease", "Influenza and pneumonia", "Kidney disease", "Stroke", "Suicide", "Unintentional injuries"])

plt.show()



