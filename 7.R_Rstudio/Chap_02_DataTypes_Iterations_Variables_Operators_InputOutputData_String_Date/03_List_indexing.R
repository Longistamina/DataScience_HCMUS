#List is a 1D or multidimensional iteration, can contain values from different datatypes

#Create list
lst <- list(c(2,3), 12.4, "spring")
print(lst)
print(class(lst))

#Indexing (the index in R starts with 1, not 0 like Python)
print(lst[1])
print(lst[2])
print(lst[-1]) #the last one