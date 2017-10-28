"""
loc and iloc also allow you to select both rows and columns from a DataFrame.
To experiment, try out the following commands in the IPython Shell. 
Again, paired commands produce the same result.

cars.loc['IN', 'cars_per_cap']
cars.iloc[3, 0]

cars.loc[['IN', 'RU'], 'cars_per_cap']
cars.iloc[[3, 4], 0]

cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
cars.iloc[[3, 4], [0, 1]]
Instructions
Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
Print out a sub-DataFrame, containing the observations for Russia 
and Morocco and the columns country and drives_right.

Hint
For the first instruction, use .loc['MOR', 'drives_right'] or .iloc[5, 2].
Don't forget to wrap your code in a print() statement.
For the second instruction, use .loc[['RU', 'MOR'], ['country', 'drives_right']] or .iloc[[4,5] , [1,2]].
Don't forget to wrap your code in a print() statement.

"""
# Import cars data
#import pandas as pd
#cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])
