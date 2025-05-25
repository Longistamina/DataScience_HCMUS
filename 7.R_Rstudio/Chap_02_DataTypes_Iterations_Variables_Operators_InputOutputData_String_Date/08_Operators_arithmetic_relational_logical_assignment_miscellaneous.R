#-----------------------------------------------------#
#--------------- Arithmetic Operators ----------------#
#-----------------------------------------------------#
v <- c(2, 5.5, 6)
t <- c(8, 3, 4)

# + plus
print(v+t)

# - subtract
print(v-t)

# * multiply
print(v*t)

# / divide
print(v/t)

# %% modulo - get the remainder
print(v%%t)

# %/% quotient - get the integer division
print(v%/%t)

# ^ exponential
print(v^t)

# %/% dot product (tich vo huong)
print(v %*% t)

#-----------------------------------------------------#
#--------------- Relational Operators ----------------#
#-----------------------------------------------------#
v <- c(2, 5.5, 6, 7)
t <- c(8, 3, 4, 7)

# > greater than
print(v > t)

# < less than
print(v < t)

# == equal
print(v == t)

# >= greater or equal
print(v >= t)

# <= less or equal
print(v <= t)

# != not equal
print(v != t)


#--------------------------------------------------#
#--------------- Logical Operators ----------------#
#--------------------------------------------------#

#All numeric values >= 1 are considered TRUE in logical operators

v <- c(2, 1, TRUE, 0)
t <- c(8, 1, FALSE, 2)

# & - AND, element-wise, compare all elements, return many logical results
# & returns TRUE when all are TRUE
print(v & t)

# && - AND, compare only the first pair of values, return ONE logical result
print(v[1] && t[1])

# | - OR, element-wise, compare all elements, return many logical results
# | returns FALSE when all are FALSE
print(v | t)

# || - OR, compare only the first pair of values, return ONE logical result
print(v[1] || t[1])

# ! Negative, if x is TRUE, then !x is FALSE
print(!v)
print(!t)


#-----------------------------------------------------#
#--------------- Assignment Operators ----------------#
#-----------------------------------------------------#

## Method 1: x <- values
colors <- c("red", "green", "blue")
print(paste("colors =", paste(colors, collapse = ", ")))

## Method 2: x = values
numbers = c(19, 14.2, 15.4)
print(paste("numbers =", paste(numbers, collapse = ", ")))

## Method 3: values -> x
c(TRUE, FALSE, TRUE, TRUE) -> pass
print(paste("pass =", paste(pass, collapse = ", ")))


#--------------------------------------------------------#
#--------------- Miscellaneous Operators ----------------#
#--------------------------------------------------------#

# : - create a vector of numbers from start to end value
v <- 1:10
print(v)

# %in% - check if any specific value is in a vector
print(11 %in% v)
print(8 %in% v)

# %*% - produce a matrix dot product multiplication, NxM %*% MxP = NxP
M = matrix(c(1, 1, 1, 2, 2, 2), nrow = 2, ncol = 3, byrow = TRUE)
print(M)
print(t(M)) #transpose of M
print(M %*% t(M))