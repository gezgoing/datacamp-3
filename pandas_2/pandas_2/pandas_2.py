"""
In the video, you saw that you can index and select Pandas DataFrames in many different ways.
The simplest, but not the most powerful way, is to use square brackets.

In the sample code on the right, the same cars data is imported from a CSV files as a Pandas DataFrame.
To select only the cars_per_cap column from cars, you can use:

cars['cars_per_cap']
cars[['cars_per_cap']]
The single bracket version gives a Pandas Series, the double bracket version gives a Pandas DataFrame.

Instructions
Use single square brackets to print out the country column of cars as a Pandas Series.
Use double square brackets to print out the country column of cars as a Pandas DataFrame.
Use double square brackets to print out a DataFrame with both the country 
and drives_right columns of cars, in this order.

 brics.loc [["RU","IN","CH"],["country ","capital"]
 brics.loc [ : ,["country ","capital"]]
 brics.iloc [ : ,[0,1]]

"""


import pandas as pd
#cars = pd.read_csv('cars.csv', index_col = 0)
cars = pd.read_csv('cars.csv')
# Print out country column as Pandas Series

print(cars['country'])
# Print out country column as Pandas DataFrame

print(cars[['country']])
# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

"""
Square brackets can do more than just selecting columns. You can also use them to get rows,
or observations, from a DataFrame. The following call selects the first five rows from the cars DataFrame:

cars[0:5]
The result is another DataFrame containing only the rows you specified.

Pay attention: You can only select rows using square brackets if you specify a slice, like 0:4.
Also, you're using the integer indexes of the rows here, not the row labels!

Instructions
Select the first 3 observations from cars and print them out.
Select the fourth, fifth and sixth observation, corresponding to row indexes 3, 4 and 5, and print them out.

Hint
For the first instruction, use [0:3]. Don't forget to wrap your code in a print() statement.
For the second instruction, use [3:6]. Don't forget to wrap your code in a print() statement.

"""

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])
