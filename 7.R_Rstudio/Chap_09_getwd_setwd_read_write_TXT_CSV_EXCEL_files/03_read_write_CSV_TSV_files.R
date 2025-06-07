# csv = Comma Separated Values
# tsv = Tab Separated Values

# These file types store data in sheet format like excel, but in plaintext
# => much lighter and faster to read

data_path <- "data_chap_09/demo_data/"

#------------------------------------------#
#---------- use read.csv() ----------------#
#------------------------------------------#

emp_csv <- read.csv(
    paste(data_path, "emp.csv", sep = ""), 
    sep = ","
)
head(emp_csv)

#highest salary
print(emp_csv[which.max(emp_csv$salary), ])


# check if the read data is dataframe
print(is.data.frame(emp_csv)) #TRUE


#------------------------------------------#
#---------- use write.csv() ---------------#
#------------------------------------------#

# write.csv() help write a given data into a .csv or .tsv type

library(tidyverse)

# get the employees from IT department and store into emp_it
emp_it <- emp_csv %>% 
    filter(dept == "IT")
head(emp_it)

# write.csv()
write.csv(
    emp_it,
    file = paste(data_path, "emp_it.csv", sep = ""),
    append = FALSE, #Means overwrite
    quote = TRUE, #Enclose string type in quotes " "
    sep = ",",
    row.names = FALSE #to avoid writing row names as a separate column.
)


#--------------------------------------------#
#---------- use write.table() ---------------#
#--------------------------------------------#

# write.table() for .tsv
write.table(
    emp_it,
    file = paste(data_path, "emp_it.tsv", sep = ""),
    append = FALSE, #Means overwrite
    quote = TRUE, #Enclose string type in quotes " "
    sep = "\t",
    row.names = FALSE #to avoid writing row names as a separate column.
)