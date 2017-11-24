"""
Putting data in a dictionary and then building a DataFrame works, 
but it's not very efficient. What if you're dealing with millions
of observations? In those cases, the data is typically available as
files with a regular structure. One of those file types is the CSV file, 
which is short for "comma-separated values".

To import CSV data into Python as a Pandas DataFrame you can use read_csv().

Let's explore this function with the same cars data from the previous exercises.
This time, however, the data is available in a CSV file, named cars.csv.
It is available in your current working directory, so the path to the file is
 simply 'cars.csv'.

Instructions
To import CSV files you still need the pandas package: import it as pd.
Use pd.read_csv() to import cars.csv data as a DataFrame. Store this dataframe
as cars. Print out cars. Does everything look OK?

Hint
Use read_csv('cars.csv') to import the data. Make sure to store the resulting
DataFrame as cars. To print out a variable x, you write print(x).

"""



# Import pandas as pd

import pandas as pd

#variable
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco',
         'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(dict)
# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
print(cars)
# Import the cars.csv data: cars
#the data is available in a CSV file, named cars.csv.
#It is available in your current working directory, so the path to the file 
#is simply 'cars.csv'.

cars = pd.read_csv('car.csv')
## Print out cars
print(cars)




"""
Your read_csv() call to import the CSV data didn't generate an error,
but the output is not entirely what we wanted. The row labels were imported 
as another column without a name.

Remember index_col, an argument of read_csv(), that you can use to specify 
which column in the CSV file should be used as a row label? Well, that's
exactly what you need here!

Python code that solves the previous exercise is already included; can you
make the appropriate changes to fix the data import?

Instructions
Run the code with Submit Answer and assert that the first column should 
actually be used as row labels.
Specify the index_col argument inside pd.read_csv(): set it to 0, so that the 
first column is used as row labels.
Has the printout of cars improved now?

Hint
Use pd.read_csv(cars, index_col = ...); can you fill in the ...?
"""

# Fix import by including index_col
cars = pd.read_csv('car.csv', index_col = 0)
#work changing the index number by the row_labels list
#cars = pd.read_csv('cars.csv')
#cars.index =row_labels
# Print out cars
print(cars)