# To do calculations with array, can use apply(array, c(index), function_name)
# Note: function_name NOT function_name() (sum not sum())

# about c(index):
## c(1) => row-wise
## c(2) => column-wise
## c(3) => matrix

rownames <- c("row1", "row2", "row3")
colnames <- c("col1", "col2", "col3", "col4")
matnames <- c("matrix1", "matrix2")

v1 <- c(1:6)
v2 <- c(7:15)

arr3D <- array(c(v1, v2), dim = c(3, 4, 2), dimnames = list(rownames, colnames, matnames))
print(arr3D)


###################

# sum row-wise
# row1 = sum all elements on row 1 of matrix 1 + sum all elements on row 1 of matrix 2
# row2 = ........................2.......................................2............
# row3 = ........................3.......................................3............
print(apply(arr3D, c(1), sum))
# row1 row2 row3 
# 47   55   63 

# min column-wise
print(apply(arr3D, c(2), min))
# col1 col2 col3 col4 
# 1    1    4    7 

# mean matrix-wise
print(apply(arr3D, c(3), mean))
# matrix1 matrix2 
# 6.50    7.25

# prod() (tich tat ca cac elements)
print(prod(arr3D[,2,2]))
# multiply a elements on column 2nd of matrix 2nd
# 1*2*3 = 6