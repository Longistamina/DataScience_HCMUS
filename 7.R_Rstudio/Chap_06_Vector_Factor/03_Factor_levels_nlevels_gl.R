# Factor: is an R object that stores data as level
# it facilitates classification tasks

# Factor has level, ascending for numeric or A-Z for character

# factor(vector)

gender <- c("Male", "Female", "Female", "Male", "Female", "Male")
is.factor(gender) #FALSE
print(gender)

gender_factor <- factor(gender)
is.factor(gender_factor) #TRUE
print(gender_factor)          

print(levels(gender_factor))  # levels() returns the levels of a factor
                              # here, levels are Female Male (A-Z)

print(nlevels(gender_factor)) # nlevels() returns the number of levels of a factor
                              # here nlevels() returns 2


#------------------------------------#
#------ change factor levels --------#
#------------------------------------#

# Use factor(vector, levels = )
gender <- c("Male", "Female", "Female", "Male", "Female", "Male")
gender_factor <- factor(gender, levels = c("Male", "Female"))
print(gender_factor) #Now levels are Male Female

# Use gl(n, k, labels)      (gl means Generate factor Levels)
## n: the number of labels
## k: the number of repeats
## labels: the values of labels

## lenght of gl(n, k, labels) = n*k

colors_factor <- gl(n = 3, k = 2, labels = c("red", "green", "blue"))
print(colors_factor) # red red green green blue blue
                     # Levels: red green blue