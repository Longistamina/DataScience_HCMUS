# ifelse() is a vectorized function used to perform conditional operations on vectors

# ifelse(test, yes, no)
## test: A logical condition (can be a single value or a vector)
## yes: Value(s) returned if the condition is TRUE
## no: Value(s) returned if the condition is FALSE

####### Example 1 #######
x <- c(5, 10, 15)

check_high_low = ifelse(x > 10, "High", "Low")
print(check_high_low)


####### Example 2 #######
x <- c(1, NA, 3)

na_to_zero = ifelse(is.na(x), 0, x)
print(na_to_zero)


#### Nested ifelse() ###

scores <- c(85, 67, 45, 90, 72, 30)

categories <- ifelse(scores >= 80, "High", ifelse(scores >= 50, "Medium", "Low"))

print(categories)
