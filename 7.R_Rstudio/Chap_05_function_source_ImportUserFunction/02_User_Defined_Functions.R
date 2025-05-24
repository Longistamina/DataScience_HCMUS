# user-defined functions are the ones that created by users for their specific tasks

# function_name <- function(arg1, arg2, ...) {
#   function_body
#   return(value)
# }

sum_even_func <- function(start, end) {
  sum_even = 0
  for (i in c(start:end)) {
    if ((i %% 2) == 0) {
      sum_even = sum_even + i
    }
  }
  return(sum_even)
}


x = sum_even_func(start = 1,  end = 20)
print(x)

y = sum_even_func(5,  15)
print(y)


######## Set constant values for argument #######

drink_func <- function(price, type = "Tea") {
  print(paste("With ", price, "you can drink ", type))
}

drink_func(1000)
drink_func(1000, type = "Coffee")

#If user does not announce value for type, it will get "Tea" as the value