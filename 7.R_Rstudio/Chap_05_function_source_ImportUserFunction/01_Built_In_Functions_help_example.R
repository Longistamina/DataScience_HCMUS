# built-in functions are the functions that are already built by R developers
# they can be a basic function or package-denpendent function

numbers <- c(1:100)

summary(numbers)
# summary() is a built-in function
# it is a generic function used to produce result summaries 
# of the results of various model fitting functions

print(sum(numbers))
# print() and sum() are also built-in functions (and many others)

help(mean) # help(function_name) displays information about a function

example(mean) # example(function_name) displays examples about how a function works

##################

# Some popular packages in R

## ggplot2:   data visualization
## foreign:   read data from spss, stata,...
## tidyverse: dataframe processing and manipulation
## rms:       regression models
## cluster:   cluster analysis