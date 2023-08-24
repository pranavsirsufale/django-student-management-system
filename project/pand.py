import numpy
import pandas as pd
'''
---- pandas stands for panel data 
---- pandas is aan opensource library that is built on top numpy 
----- pandas is widely used in data analysis, machine learning , data visualisation etc...
----- pands has two data structure one is series and dataframes 


-                           series is a one dimensional labelled array , which can holds datatype
                            DAta frame is a two-timesional labelled datastructure , with colums and rows indexing 
                            It is very much similar to my excel sheet 




'''

data = [21,54,545,5,5,584,5,8]
series = pd.Series(data)
print(series)


dict1 = { 'Name':['pranav','pallavi','pushpa'],
          'Age':[54,5,54],
          'city':['ghansawangi','ghansawngi','jalna']}
df = pd.DataFrame(dict1)
print(df)
df1 = pd.read_csv('xyz.')


# reading to excel file
df2 = pd.read_excel('exel.xlsx')
print(df2)


#Data manipulation sorting , selection , visualisation , indexing ,

# index or selection col1
col1 = df1['salary']


# multiple columns
cols = df1[['salary','earsExperience']]

# selecting rows
# conditional row selection

