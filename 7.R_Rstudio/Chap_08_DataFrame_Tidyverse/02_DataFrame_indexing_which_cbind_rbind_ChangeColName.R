#----------------------------------#
#------------- indexing -----------#
#----------------------------------#

df_students <- data.frame(
  "name" = c("Hellen", "Jolie", "Kiwi", "John", "Mark", "Tom"),
  "age" = c(17, 16, 17, 18, 19, 16),
  "mark" = c(9, 9, 8, 7.5, 7.5, 8),
  stringsAsFactors = FALSE
)

# df["col_name"] results in a single-column dataframe
df_students["name"]

# df[["col_name"]] or df$col_name results in a vector
df_students[["name"]]
df_students$name

# df[1,] get the 1st row => vector
df_students[1,]

# df[3:5,] get 3 rows from 3rd to 5th => dataframe
df_students[3:5,]

# df[, 3] get the 3rd column => vector
df_students[, 3]

# df[, 2:3] get the 2 columns 2nd and 3rd => dataframe
df_students[, 2:3]

# df[c(3, 5), c(1, 2)] get the 3rd and 5th rows, with the 1st and 2nd columns => dataframe
df_students[c(3, 5), c(1, 2)]



#-----------------------------------------------#
#--------- indexing with df[condition, ] -------#
#-----------------------------------------------#

# get all rows where age > 17
df_students[df_students$age > 17, ]

# get all rows where age < 18 and mark = 9.0
df_students[(df_students$age < 18 ) & (df_students$mark == 9.0), ]


#----------------------------------------------------------------------------#
#--------- indexing with which(condition) which.max() and which.min() -------#
#----------------------------------------------------------------------------#

# get the row/student having highest mark
df_students[which.max(df_students$mark), ]

# get the row/student having highest mark, display 2nd column only
df_students[which.max(df_students$mark), 2]

# get the row/student having highest mark, display 1st and 2nd columns
df_students[which.max(df_students$mark),1:2]

# get the row/student having smallest age
df_students[which.min(df_students$age), ]


########  df[which(condition), ] ##############

df_students[which(df_students$age > 17), ]

df_students[which((df_students$age < 18 ) & (df_students$mark == 9.0)), ]


######## difference: df[condition, ] and df[which(condtion), ] ############

df <- data.frame(name = c("Alice", NA, "Carol"),
                 age = c(25, 30, 22))

df[which(df$name == "Bob"), ]
# Returns an empty data frame without an error

df[df$name == "Bob", ]
# Returns a row of NAs where df$name is NA



#------------------------------------#
#---------- add new column ----------#
#------------------------------------#

df_students <- data.frame(
  "name" = c("Hellen", "Jolie", "Kiwi", "John", "Mark", "Tom"),
  "age" = c(17, 16, 17, 18, 19, 16),
  "mark" = c(9, 9, 8, 7.5, 7.5, 8),
  stringsAsFactors = FALSE
)

######## add new column using VECTOR and c()
## Note: length of vector must be equal to the number of observations/rows of df

df_students$class <- c("class_a", "class_b", "class_a", "class_c", "class_d", "class_b")

print(df_students)


######### add new column using cbind() and another DATAFRAME (cbind = column bind)
## Note: dataframes must share the SAME NROWs or number of observations/rows to use cbind()

df_PoB = data.frame("PoB" = c("UK", "FR", "US", "DE", "CA", "NZ"))
# PoB = place of birth

df_students = cbind(df_students, df_PoB)
print(df_students)


#----------------------------------#
#--------- add new round ----------#
#----------------------------------#

df_students <- data.frame(
  "name" = c("Hellen", "Jolie", "Kiwi", "John", "Mark", "Tom"),
  "age" = c(17, 16, 17, 18, 19, 16),
  "mark" = c(9, 9, 8, 7.5, 7.5, 8),
  stringsAsFactors = FALSE
)

######## use rbind() to add new rows of a dataframe to another dataframe (rbind = row bind)
## Note: the dataframes must share the SAME STRUCTURE for rbind() to work
## Note: if there are identical rows between dataframes, the rbind() will keep only one

new_students = data.frame(
  "name" = c("Lancelot", "Galahad"),
  "age" = c(20, 21),
  "mark" = c(8.5, 9.5)
)

df_students = rbind(df_students, new_students)
print(df_students)


#------------------------------------#
#-------- change column name --------#
#------------------------------------#

df_students <- data.frame(
  "name" = c("Hellen", "Jolie", "Kiwi", "John", "Mark", "Tom"),
  "age" = c(17, 16, 17, 18, 19, 16),
  "mark" = c(9, 9, 8, 7.5, 7.5, 8),
  "PoB" = c("UK", "FR", "US", "DE", "CA", "NZ"),
  stringsAsFactors = FALSE
)

names(df_students)    # Return a vector of df_students column names
colnames(df_students) # "name" "age"  "mark" "PoB"

# Change column name "PoB" into "Place_of_birth"
names(df_students)[names(df_students) == "PoB"] <- "Place_of_birth"

print(df_students)
