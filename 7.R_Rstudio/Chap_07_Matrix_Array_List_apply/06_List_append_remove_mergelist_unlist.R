#---------------------------------------------------------#
#------------ append new element to list -----------------#
#---------------------------------------------------------#

list_append <- list("a", 2, FALSE)

# Append new element
list_append[length(list_append) + 1] = 14.9

print(list_append)


#-------------------------------------------------#
#------------ remove element from list -----------#
#-------------------------------------------------#

# list[index] = NULL
list_remove <- list("b", 8, TRUE)
list_remove[2] = NULL
print(list_remove)


# list$element_name = NULL
list_mix <- list(c("Red", "Green", "Yellow"), matrix(c(1:8), nrow=2),
                 list("green", TRUE, 12.5), TRUE)
names(list_mix) <- c("Traffic_light", "Matrix", "Inner_list", "Pass")

list_mix$Traffic_light = NULL
print(list_mix)


#-----------------------------------------------#
#------------ update element of list -----------#
#-----------------------------------------------#

list_update <- list(FALSE, "asbc", 2)

list_update[1] = TRUE

print(list_update)


#-----------------------------------------------#
#------------ merge list with c(...) -----------#
#-----------------------------------------------#

list_1 = list(c("a", "b"), 2)
list_2 = list(TRUE, 14.5)

merge_list = c(list_1, list_2)
print(merge_list) # The elements of list_1 will come first, then list_2's


#------------------------------------#
#-------- unlist() to vector --------#
#------------------------------------#

# List does not support mathematical calculation, even if all its data are numeric
# To do so, must use unlist() to convert a list into a vector, then calculate

list_a <- list(1:5)
list_b <- list(6:10)

# print(list_a + list_b) => this will raise error

vec_a <- unlist(list_a)
print(vec_a)

vec_b <- unlist(list_b)
print(vec_b)

print(vec_a + vec_b)

####
print(unlist(list_a) + unlist(list_b))