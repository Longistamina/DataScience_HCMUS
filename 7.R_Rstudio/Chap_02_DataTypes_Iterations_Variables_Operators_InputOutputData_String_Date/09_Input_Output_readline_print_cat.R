#------------------------------------------------#
#------- Input data using readline() ------------#
#------------------------------------------------#

name <- readline(prompt = "Enter name: ")

age <- as.integer(age)

#--------------------------------------------------------#
#------- Output data using print() and cat() ------------#
#--------------------------------------------------------#

print(paste("Hi", name, "next year you will be", age+1, "years old!"))

colors <- c('red', 'green', 'blue')
cat("colors are", colors, "\n")