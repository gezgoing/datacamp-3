# Both the dplyr and hflights packages are loaded
library(dplyr, hflights)
# Convert the hflights data.frame into a hflights tbl

hflights = tbl_df(hflights)


# Display the hflights tbl
print(hflights)

# Create the object carriers
carriers = hflights$UniqueCarrier
