import pandas as pd
import numpy as np

"""Reads/looks for an xls file named test"""
df = pd.read_excel("messyData.xlsx")
df.set_index('id')


print('--------------------------------------------Print df before changes-----------------------------------------------')
print(df)
print('------------------------------------------------------------------------------------------------------------\n\n\n')

print('-----------------------------------------------Find blank names-----------*---------------------------------------')
nullNamesCheck = df.loc[(df['name'].isna())]
print('Search for blank names')

print(nullNamesCheck)
print('------------------------------------------------------------------------------------------------------------\n\n\n')


print('-----------------------------------Fill missing value from df for name column-------------------------------------')
newName = df.loc[(df['id'] == 25) & (df['name'].isna()), 'name'] = 'Jarel'
newName = df.loc[(df['id'] == 45) & (df['name'].isna()),  'name'] = 'Sammy'

print('Fill missing value from name column to specific names and show results')
print(df.loc[df['id'].isin([25, 45])])
print('------------------------------------------------------------------------------------------------------------\n\n\n')

# print('----------------------------------------sort df2 by id ------------------------------------------------------------')
df2 = df.sort_values(by=['id'])
# print('------------------------------------------------------------------------------------------------------------\n\n\n')


print('-------------------------------------Check null age column -------------------------------------------------------')
print('Before changing NaN age \n', df2.loc[(df2['age'].isnull())])

newAge = df2.loc[(df2['id'] == 14) & (df2['age'].isna()), 'age'] = 22
newAge2 = df2.loc[(df2['id'] == 29) & (df2['age'].isna()), 'age'] = 51

print('\nAfter changing NaN age to  \n', df.loc[df['id'].isin([22, 51])])
print('------------------------------------------------------------------------------------------------------------\n\n\n')

print('-----------------------------------Change age dtype from float to int---------------------------------------------')
df2['age'] = df2['age'].astype(int)
print('------------------------------------------------------------------------------------------------------------\n\n\n')

print('-----------------------------------Change age dtype from int to float---------------------------------------------')
# df2['salary'] = df2['salary'].astype(float)
print('------------------------------------------------------------------------------------------------------------\n\n\n')


print('-------------------------------------Check negative age column -------------------------------------------------------')
a = df2.loc[df2['id'] == 14]
b = df2.loc[(df2['id'] == 12)]
print('14 id \n', a)
print()
print('-5 value:\n', b)
print('------------------------------------------------------------------------------------------------------------\n\n\n')

print('-------------------------------Change -5 age value to non-negtive---------------------------------------------------')
newAge3 = df2.loc[(df2['id'] == 12) & (df2['age'] == -5), 'age'] = 35
print('-5 value changed 35:\n', df2.loc[(df2['id'] == 12)])
print('------------------------------------------------------------------------------------------------------------\n\n\n')

print('--------------------------------------Check for ages gt 66--------------------------------------------------------')
print('Age gt 66 \n ', df2.loc[df2['age'] > 66])
print('------------------------------------------------------------------------------------------------------------\n\n\n')

print('--------------------------------------Change all ages to 43--------------------------------------------------------')
newAge4 = df2.loc[(df2['age'] > 66), 'age'] = 43
print(df2.loc[df2['id'].isin([15, 42, 45])])
print('------------------------------------------------------------------------------------------------------------\n\n\n')


# print('----------------------------Making sure department names are consistent----------------------------------------')
# df2["department"] = df2["department"].str.replace(
#     "Marketng", "Marketing", regex=False)
# df2["department"] = df2["department"].str.replace(
#     "marketing", "Marketing", regex=False)
# .astype(float)

df2['department'] = df2['department'].replace(to_replace=['Marketng', 'marketing', 'hr', 'sales', 'engineering'],
                                              value=['Marketing', 'Marketing', 'HR', 'Sales', 'Engineering'])
# print('------------------------------------------------------------------------------------------------------------\n\n\n')


# print('--------------------------------Making sure active column is consistent--------------------------------------------')

df2['active'] = df2['active'].replace(to_replace=['no', 'yes', 'TRUE', 'FALSE'
                                                  ],
                                      value=['False', 'True', 'False', 'True'])
# print('------------------------------------------------------------------------------------------------------------\n\n\n')

print('-------------------------------------Send df3 to renameDFR.xlsx---------------------------------------------------')
df2.to_excel('renameDF.xlsx', sheet_name='workers', index=False)
print('------------------------------------------------------------------------------------------------------------\n\n\n')


print('-----------------------------------Null values summary count------------------------------------------------------')
print('Null values summary count: \n\n', df2.isnull().sum())
print('------------------------------------------------------------------------------------------------------------\n\n\n')

print('-------------------------------------Columns data types-----------------------------------------------------------')
print(df2.dtypes)
print('------------------------------------------------------------------------------------------------------------\n\n\n')


print('Pandas version:', pd.__version__)
