#Array is a 3D iteration, meaning it contains many 2D matrices

#Create array
#dim = c(nrows, ncols, nmatrices) (python is nmatrices, nrows, ncols)
colors <- array(c('red', 'green', 'blue'), dim = c(3,2,2))
print(colors)