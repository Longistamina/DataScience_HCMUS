# Array is a multidimensional object in R, comprising many matrices
# Generally, array is created in 3D

# array(data, dim = c(nrow, ncol, nmat))

# arr3D <- array(1:24, dim = c(2, 3, 4))
# arr4D <- array(1:120, dim = c(2, 3, 4, 5))


#### 3D array ###
v1 <- c(1:6)
v2 <- c(7:15)

arr3D <- array(c(v1, v2), dim = c(3, 4, 2)) # dim = 3x4x2
print(arr3D)

### 4D array ###
arr4D <- array(1:120, dim = c(2, 3, 4, 5))
print(arr4D)


#---------------------------------------------------------------------#
#---------- define row names, col names and matrix names -------------#
#---------------------------------------------------------------------#

rownames <- c("row1", "row2", "row3")
colnames <- c("col1", "col2", "col3", "col4")
matnames <- c("matrix1", "matrix2")

v1 <- c(1:6)
v2 <- c(7:15)

arr3D <- array(c(v1, v2), dim = c(3, 4, 2), dimnames = list(rownames, colnames, matnames))
print(arr3D)


#---------------------------------------#
#---------- array indexing -------------#
#---------------------------------------#

# array_name[row_index, column_index, matrix_index]

v1 <- c(1:6)
v2 <- c(7:15)

arr3D <- array(c(v1, v2), dim = c(3, 4, 2))
print(arr3D)

# Access element at 3rd row, 2nd column, from 1st matrix
arr3D[3, 2, 1]

# Access all elements on 1st row, from 2nd matrix
arr3D[1,,2]

# Access only matrix 2nd
arr3D[,,2]