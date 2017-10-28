"""
It's perfectly possible to chain square brackets to select elements. To fetch the population for Spain from europe, for example, you need:

europe['spain']['population']

instrutions:
Use chained square brackets to select and print out the capital of France.
Create a dictionary, named data, with the keys 'capital' and 'population'. Set them to 'rome' and 59.83, respectively.
Add a new key-value pair to europe; the key is 'italy' and the value is data, the dictionary you just built.
"""
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France

print(europe['france']['capital'])
# Create sub-dictionary data

europe ['data']= {'capital': 'rome', 'population' : 59.83}
# Add data to europe under key 'italy'
europe ['italy'] = europe['data']
#europe.key()

# Print europe
#print(europe.keys())
print(europe)