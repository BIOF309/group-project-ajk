NCHS Data Analysis
==============================

[Slides](https://biof309.github.io/group-project-ajk/slides.html)

This dataset from ([CDC](https://catalog.data.gov/dataset/age-adjusted-death-rates-for-the-top-10-leading-causes-of-death-united-states-2013)) presents the age-adjusted death rates for the 10 leading causes of death in the United States beginning in 1999. Data are based on information from all resident death certificates filed in the 50 states and the District of Columbia using demographic and medical characteristics. Age-adjusted death rates (per 100,000 population) are based on the 2000 U.S. standard population. Populations used for computing death rates after 2010 are postcensal estimates based on the 2010 census, estimated as of July 1, 2010. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for non-census years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published. Causes of death classified by the International Classification of Diseases, Tenth Revision (ICD–10) are ranked according to the number of deaths assigned to rankable causes. Cause of death statistics are based on the underlying cause of death. SOURCES CDC/NCHS, National Vital Statistics System, mortality data (see http://www.cdc.gov/nchs/deaths.htm); and CDC WONDER (see http://wonder.cdc.gov). REFERENCES

National Center for Health Statistics. Vital statistics data available. Mortality multiple cause files. Hyattsville, MD: National Center for Health Statistics. Available from: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm.

Murphy SL, Xu JQ, Kochanek KD, Curtin SC, and Arias E. Deaths: Final data for 2015. National vital statistics reports; vol 66. no. 6. Hyattsville, MD: National Center for Health Statistics. 2017. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_06.pdf.

Project Organization
------------

Goals
- Upload dataset 
- Manipulate dataset
- Produce graphs to understand relationships in dataset


Directions
- (1) Download dataset from CDC link
- (2) Examine the data and analyze columns
- (3) Select the column names of interest
- (4) Group this new dataset by year and by cause name to create the x-axis and different types in each bar in bar plot
- (5) Sum this new group to create the y-axis in bar plot
- (6) Create & save bar graph
     

Code | Data Processing.py

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
    plt.savefig('#deathsbycausenameyear_bargraph.png')




--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #coo>kiecutterdatascience</small></p
