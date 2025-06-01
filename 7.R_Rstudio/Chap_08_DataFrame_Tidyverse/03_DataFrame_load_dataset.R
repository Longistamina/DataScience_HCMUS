3#--------------------------------------#
#----------- built-in dataset ----------#
#---------------------------------------#

# R has many built-in datasets for practicing

# ls() displays all current loaded or created dataframes in current environment
ls()

# data() displays all built-in datasets of R
data()

# data(dataset_name) to load a specific dataset into the environment
data("mtcars")

print(mtcars)

summary(mtcars)
