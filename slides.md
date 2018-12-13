Alexander Kim

    12 December 2018


# NCHS Leading Causes of Death in US From 1999-2016

-  This dataset from (CDC) presents the age-adjusted death rates for the 10 leading causes of death in the United States beginning in 1999. Data are based on information from all resident death certificates filed in the 50 states and the District of Columbia using demographic and medical characteristics. Age-adjusted death rates (per 100,000 population) are based on the 2000 U.S. standard population. Populations used for computing death rates after 2010 are postcensal estimates based on the 2010 census, estimated as of July 1, 2010. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for non-census years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published. Causes of death classified by the International Classification of Diseases, Tenth Revision (ICD–10) are ranked according to the number of deaths assigned to rankable causes. Cause of death statistics are based on the underlying cause of death.

# Research Question

- What were the leading causes of death each year in the past two decades? 

# Goals 
- Import csv data from link 
- Organize data
- Create bar graph

# Code

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    NCHS = pd.read_csv('NCHS_-_Leading_Causes_of_Death__United_States.csv')
    
    NCHS.info()
    
    year = NCHS[['Cause Name', 'Year', 'Deaths']]
    year_group = year.groupby(['Year','Cause Name'])
    year_group_total = year_group.sum()
    
    barplot = year_group_total.unstack().plot(kind='bar',stacked=True,title='Number of Deaths by Cause Name each year (1999-2016)',figsize=(9,7))
    barplot.set_xlabel('Year')
    barplot.set_ylabel('Deaths')
    barplot.set_ylim((0,10000000))
    barplot.legend(["All causes","Alzheimer's disease","CLRD","Cancer", "Diabetes","Heart disease", "Influenza and pneumonia", "Kidney disease", "Stroke", "Suicide", "Unintentional injuries"])
    
    plt.show()


# Results 

![img](https://raw.githubusercontent.com/BIOF309/group-project-ajk/master/%23deathsbycausenameyear_bargraph.png)


# Conclusion

- Cancer and heart disease has been the two leading causes of death in the past two decades.

# Future Directions

- Create a more user friendly step-by-step program where researchers can insert variables and quickly perform data visualization.
 
