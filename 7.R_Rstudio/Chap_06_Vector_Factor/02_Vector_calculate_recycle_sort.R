#---------------------------------------------#
#------------ same-length vectors ------------#
#---------------------------------------------#

# Create two vectors
v1 <- c(5, 7, 4, 8, 0, 11)
v2 <- c(4, 10, 2, 8, 1, 2)


# Addition
print(v1 + v2)

# Subtraction
print(v1 - v2)

# Multiplication (element-wise)
print(v1 * v2)

# Division (element-wise)
print(v1 / v2)

# Dot product (tich vo huong)
print(v1 %*% v2)


#--------------------------------------------------#
#------------ different-length vectors ------------#
#--------------------------------------------------#

v3 <- c(5, 7, 4, 8, 0, 11)
v4 <- c(4, 10)

print(v3 + v4) # 9 17  8 18  4 21

# Here, the length of v4 is 2, but v3 is 6
# So, when perform calculation, the vector v4 will be recycled
# Meaning (4, 10) => (4, 10, 4, 10, 4, 10)
# Then the recycled one is used for v3 + v4

v3 <- c(1, 2, 3)
v4 <- c(4, 10)   #(4,10) -> (4, 10, 4)
print(v3 + v4)


#----------------------------------------#
#------------ vector sorting ------------#
#----------------------------------------#

# Sort numeric vector
v <- c(1, 2, 5, -10, 7, -6, 9)

v_asc = sort(v) #Default is ascending sort
print(v_asc) # -10  -6   1   2   5   7   9

v_desc = sort(v, decreasing = TRUE) #Descending sort
print(v_desc) # 9   7   5   2   1  -6 -10


# Sort character vector
colors <- c("red", "green", "blue", "brown", "magenta", "violet", "turquoise")

colors_asc = sort(colors) #Default is A-Z sort
print(colors_asc) # "blue"      "brown"     "green"  "magenta"   "red"   "turquoise"   "violet"

colors_desc = sort(colors, decreasing = TRUE) #Z-A sort
print(colors_desc) # "violet"    "turquoise" "red"   "magenta"   "green"     "brown"   "blue"
