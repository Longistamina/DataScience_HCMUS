# DataFrame is a 2D table composed of many columns and rows
# Each column is a variable of one unique datatype, must not leave the column name blank
# Each row is an observation, containing a set of values of all columns
# The datatype can be varied across all columns (i.e. can be heterogeneous)
# The datatype of each column can be numeric, factor or character

## Note: all the columns/variables must share the same length

#----------------------------------------------------------#
#------- create dataframe with data.frame() ---------------#
#----------------------------------------------------------#

df_students <- data.frame(
  "name" = c("Hellen", "Jolie", "Kiwi", "John", "Mark", "Tom"),
  "age" = c(17, 16, 17, 18, 19, 16),
  "mark" = c(9, 9, 8, 7.5, 7.5, 8),
  stringsAsFactors = FALSE
)
## Note: "column_name" = c(....) NOT "column_name" <- c(....)

# Though the column "name" here is character, it is not a categorical variable
# => set stringAsFactors = FALSE so that R won't treat it as factor datatype

print(df_students)


##### create dataframe from vectors #####

name <- c("Harry", "Ron", "Hermione")
sex <- c("Male", "Male", "Female")
age <- rep(17, 3)
mark <- c(8.0, 6.5, 10.0)

df_wizards <- data.frame(name, sex, age, mark,
                     stringsAsFactors = FALSE)
df_wizards$sex <- as.factor(df_wizards$sex)

# There are 2 character-type columns in df_wizards
# But only "sex" is categorical, while "name" is not.
# Therefore, cannot use stringsAsFactors = TRUE
# because it will convert all character-type column into factor datatype
# => set stringsAsFactors = FALSE
# => then convert the "sex" into factor later on.

print(df_wizards)
print(class(df_wizards$sex)) #Check if df_wizards$sex is factor


#---------------------------------------------------------------------#
#------- row.names = ... define column to be index ... ---------------#
#---------------------------------------------------------------------#

# row.names = col_name / variable_name
# this will make that col_name column become the index column
# meaning all its values will become the row names (or index), can be used for indexing
# the column chosen to be the index col MUST NOT HAVE OVERLAP VALUES

df_students <- data.frame(
  "name" = c("Hellen", "Jolie", "Kiwi", "John", "Mark", "Tom"),
  "age" = c(17, 16, 17, 18, 19, 16),
  "mark" = c(9, 9, 8, 7.5, 7.5, 8),
  row.names = "name",
  stringsAsFactors = FALSE
)

print(df_students) # The "name" column now becomes the index colum


#---------------------------------------------#
#--------- dim() nrow() ncol() ---------------#
#---------------------------------------------#

dim(df_wizards) # 3 4: means 3 rows and 4 columns

dim(df_wizards)[1] # 3 rows
nrow(df_wizards)   # 3 rows

dim(df_wizards)[2] # 4 columns
ncol(df_wizards)   # 4 columns

#---------------------------------------------------------------#
#--------- str() to show the dataframe structure ---------------#
#---------------------------------------------------------------#

# like df.info() in Python

str(df_wizards)

# 3 obs: means 3 observations or 3 rows
# 4 variables: means 4  columns


#-------------------------------------------------------#
#-------------- head() and tail() ----------------------#
#-------------------------------------------------------#

head(df_students, n = 3) #show the first 3 rows (default is 6)

tail(df_students, n = 2) #show the last 2 rows (default is 6)


#--------------------------------------------#
#---------------- summary() -----------------#
#--------------------------------------------#

# like df.describe() in Python
# summary() displays the basic descriptive statistics of all variables

summary(df_wizards)