#Variable is an object that stores value
#Ex: x = 1, then x is the variable storing an integer value = 1


## Method 1: x <- values
colors <- c("red", "green", "blue")
print(paste("colors =", paste(colors, collapse = ", ")))

## Method 2: x = values
numbers = c(19, 14.2, 15.4)
print(paste("numbers =", paste(numbers, collapse = ", ")))

## Method 3: values -> x
c(TRUE, FALSE, TRUE, TRUE) -> pass
print(paste("pass =", paste(pass, collapse = ", ")))


#Don't use these keywords in R (shown by ?reserved) to name a variable
?reserved
          #if else repeat while function for in next break
          #TRUE FALSE NULL Inf NaN NA NA_integer_ NA_real_ NA_complex_ NA_character
          #1, 2, 3, 4,.... 


#Shown all created variables
print(ls())