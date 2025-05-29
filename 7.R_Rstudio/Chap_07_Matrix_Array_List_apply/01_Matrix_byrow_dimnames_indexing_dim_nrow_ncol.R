# Matrix is a 2D object storing homogeneous data (same datatype)
# It is usually used to store numeric data

### byrow = TRUE ###
M1 <- matrix(c(1:12), nrow = 4, ncol = 3, byrow = TRUE)
print(M1)

#  1  2  3
#  4  5  6
#  7  8  9
# 10 11 12


### byrow = FALSE ###
M2 <- matrix(c(1:12), nrow = 4, ncol = 3, byrow = FALSE)
print(M2)

# 1  5  9
# 2  6  10
# 3  7  11
# 4  8  12


### create vector from matrix
v1 <- c(1, 2, 3)
v2 <- c(4, 5, 6)
v3 <- c(7, 8, 9)

M3 <- matrix(c(v1, v2, v3), nrow = 3, byrow = TRUE)
print(M3)

#-------------------------------------------------------#
#------------ Define column and row names --------------#
#-------------------------------------------------------#

rownames = c("row1", "row2", "row3", "row4")
colnames = c("col1", "col2", "col3")

M4 <- matrix(c(1:12), nrow = 4, ncol = 3, dimnames = list(rownames, colnames))
print(M4)

#       col1 col2 col3
#row1    1    5    9
#row2    2    6   10
#row3    3    7   11
#row4    4    8   12


#-------------------------------#
#--------- indexing ------------#
#-------------------------------#

rownames = c("row1", "row2", "row3", "row4")
colnames = c("col1", "col2", "col3")
m <- matrix(c(1:12), nrow = 4, ncol = 3, dimnames = list(rownames, colnames))
print(m)

# Access element at 1st row and 3rd column
m[1,3]

# Access all elements of 2nd row
m[2,]

# Access all elements of 3rd column
m[,3]

# Access first 2 rows of 3rd column
m[1:2,3]



#----------------------------------------#
#--------- dim - nrow - ncol ------------#
#----------------------------------------#

mat <- matrix(c(1:10), nrow = 2, byrow = FALSE)
print(mat)

# dim() returns dimension
dim(mat)

# nrow() returns the number of rows
nrow(mat)

# ncol() returns the number of columns
ncol(mat)