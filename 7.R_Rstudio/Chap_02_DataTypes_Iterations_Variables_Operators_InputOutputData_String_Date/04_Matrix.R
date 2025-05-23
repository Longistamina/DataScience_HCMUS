#Matrix is 2D a iteration that have many rows, many columns
#Matrix has ONLY numeric values

#Create matrix byrow = TRUE
m_row = matrix(c(1,2,3,4,5,6,7,8), nrow=2, byrow = TRUE)
print(m_row)

#Create matrix byrow = FALSE
m_col = matrix(c(1,2,3,4,5,6,7,8,9), nrow=3, byrow = FALSE)
print(m_col)