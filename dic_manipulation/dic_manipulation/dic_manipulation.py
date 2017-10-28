"""
To add a new key-value pair to europe you can use something like this:

europe['iceland'] = 'reykjavik'
"""

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print(europe['italy'])

# Add poland to europe
europe['polan'] = 'warsaw'

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany

europe ['germay' ]= 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)