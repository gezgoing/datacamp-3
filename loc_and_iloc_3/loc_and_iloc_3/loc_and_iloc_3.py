"""
It's also possible to select only columns with loc and iloc.
In both cases, you simply put a slice going from beginning to end in front of the comma:

cars.loc[:, 'country']
cars.iloc[:, 1]

cars.loc[:, ['country','drives_right']]
cars.iloc[:, [1, 2]]
Instructions
Print out the drives_right column as a Series using loc or iloc.
Print out the drives_right column as a DataFrame using loc or iloc.
Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc.

Hint
For the first instruction, use .loc[:, 'drives_right'] or .iloc[:, 2].
Don't forget to wrap your code in a print() statement.
For the second instruction, use .loc[:, 'drives_right'] or cars.iloc[:, 2].
Don't forget to wrap your code in a print() statement.
For the third instruction, use .loc[:, ['cars_per_cap', 'drives_right']] or .iloc[:, [0, 2]].
Don't forget to wrap your code in a print() statement.
"""

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])
#print(cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame

print(cars.loc[:, ['cars_per_cap', 'drives_right']])