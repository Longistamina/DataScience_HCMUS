#----------------------------------------------------#
#---------- same dimension calculations -------------#
#----------------------------------------------------#

M1 <- matrix(seq(1,15,2), nrow = 2, byrow = TRUE)
print(M1)

M2 <- matrix(seq(0,14,2), nrow = 2, byrow = TRUE)
print(M2)

# Add
print(M1+M2)

# Subtract
print(M1-M2)

# Multiply element-wise (not dot product)
print(M1*M2)

# Divide element-wise (not multiply the inverse matrix)
print(M1 / M2)


#--------------------------------------------------------------#
#------------ dot product (nxm) %*% (mxp) = (nxp) -------------#
#--------------------------------------------------------------#

mat1 <- matrix(c(1:12), ncol = 4) # 3x4
mat2 <- matrix(c(1:8), nrow = 4)  # 4x2
print(mat1)
print(mat2)

# dot product matrix - matrix
print(mat1 %*% mat2) # 3x2

# dot product matrix - vector
vec <- c(4:6) # 1x3
print(vec)

print(vec %*% mat1) # 1x3 %*% 3x4 = 1x4


#------------------------------------#
#------------ transpose -------------#
#------------------------------------#

mat <- matrix(c(1:10), nrow = 2, byrow = FALSE)
print(mat)
print(dim(mat)) #dim() to check dimension
                # 2x5

# t(matrix) to transpose matrix m.n => n.m
print(t(mat))
print(dim(t(mat))) # 5x2

# matrix %*% t(matrix) always results in a square matrix
print(mat %*% t(mat))
print(dim(mat %*% t(mat))) # 2x2