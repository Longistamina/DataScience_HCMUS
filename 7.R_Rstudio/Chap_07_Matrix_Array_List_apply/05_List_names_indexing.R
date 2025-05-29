# List is a 1D object storing heterogeneous data (different datatypes)

# list()

list_data <- list("hello", "R", 12, 25.5, c(21, 32, 11), TRUE)
print(list_data) #Each element of list is indexed as [[i]], with double brackets


#----------------------------------------------#
#------------ naming list's elements ----------#
#----------------------------------------------#

# names(list_name) <- c(name_1, name_2, name_3, ...)

list_mix <- list(c("Red", "Green", "Yellow"), matrix(c(1:8), nrow=2),
                 list("green", TRUE, 12.5), TRUE)
print(list_mix)


names(list_mix) <- c("Traffic_light", "Matrix", "Inner_list", "Pass")
print(list_mix)


# list(name1 = element1, name2 = element2, ...)

list_date = list("year"=c(1998, 1999, 2000), "month"=c("Dec", "Nov"), "day"=c(1, 2, 3))
print(list_date)

x <- c(1, 3, 4, 7, 10)
list_cal = list("x"=x, "x*2" = x*2, "x/3" = x/3, "sqrt(x)" = sqrt(x))
print(list_cal)

#-------------------------------------------#
#------------- list indexing ---------------#
#-------------------------------------------#

# list_name[index]

# list_name[[big_element_index]][small_element_index]

# list_name$element_name

# list_name$big_element_name[small_element_index]

list_mix <- list(c("Red", "Green", "Yellow"), matrix(c(1:8), nrow=2),
                 list("green", TRUE, 12.5), TRUE)

names(list_mix) <- c("Traffic_light", "inner_Matrix", "inner_List", "Pass")


print(list_mix[1]) #  "Red"    "Green"  "Yellow"

print(list_mix[[1]][1]) # "Red"

print(list_mix$inner_Matrix) # print out all the inner_Matrix in list

print(list_mix$inner_Matrix[2,3]) # print out 2nd row, 3rd column of inner_Matrix in list
                                  # 6