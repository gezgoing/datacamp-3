# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index(countries[2])

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

"""
The countries and capitals lists are again available in the script.
It's your job to convert this data to a dictionary where the country 
names are the keys and the capitals are the corresponding values.
As a refresher, here is a recipe for creating a dictionary:

my_dict = {
   "key1":"value1",
   "key2":"value2",
}
"""
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {str(countries[i]): str(capitals[i]) for i in range(len(countries)) }

# Print europe
print(europe)