#Vector is a 1D iteration whose values belong to 1 datatype only
#If vector has one character type element, then the vector is also character type

#------- Vector character -----------------#
fruit <- c("apple", "pear", "pineaple", "strawberry")
print(fruit)
print(class(fruit))

#--------- Vector numeric -----------------#
nums <- c(1,2,3,4,5)
print(nums)
print(class(nums))

#-------- If vector has one character type element, then the vector is also character type -------#
mix <- c(2,"apple")
print(mix)
print(class(mix))

#--------------- Factor NLevels ----------------------#
apple_colors <- c("green", "green", "green", "yellow","green", "red", "red", "red", "white")

factor_apple <- factor(apple_colors) #Create factor object to define unique values
print(factor_apple)

print(nlevels(factor_apple)) #Count the number of numeric values