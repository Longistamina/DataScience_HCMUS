# Vector is a 1D iteration whose values belong to 1 datatype only
# If a vector has one character type element, then the vector is also character type

# Atomic vector: a vector whose datatype is homogeneous
# Recursive vector (list): a vector whose datatype is heterogeneous (have different datatypes)

# In general, when referring vector in R, it's atomic vector

# There are 6 types of vector in R:
#   1. logical vector
#   2. integer vector
#   3. double vector (double is float in Python)
#   4. complex vector
#   5. character vector
#   6. raw vector

# single-element vector: a vector whose length is 1
# multiple-element vector: a vector whose length is >1


#----------------------------------------------#
#------------- single-element vector ----------#
#----------------------------------------------#

# Atomic character SE vector
print("abc")

# Atomic integer SE vector
print(63L)

# Atomic double SE vector
print(12.5)

# Atomic logical SE vector
print(TRUE)

# Atomic complex SE vector
print(2+3i)

# Atomic raw SE vector
print(charToRaw("hello")) #Return hexadecimal ASCII codes


#------------------------------------------------#
#------------- multiple-element vector ----------#
#------------------------------------------------#

# Use c() to create ME vector
v <- c("red", "green", "blue")
print(v) # "red"   "green" "blue" 

# Use start:end to create numeric ME vector
v <- 1:10
print(v) # 1  2  3  4  5  6  7  8  9 10

v <- 1.6:5.6
print(v) # 1.6 2.6 3.6 4.6 5.6

v <- 5.8:11.4
print(v) # 5.8  6.8  7.8  8.8  9.8 10.8
         # The 11.4 is discarded as it does not respect the rule

# Use seq(start, end, by = ) to create ME vector
v <- seq(2, 10, by = 0.5)
print(v)


#-------------------------------------------------#
#------------- indexing vector elements ----------#
#-------------------------------------------------#

colors <- c("red", "green", "blue", "brown", "magenta", "violet", "turquoise")

# indexing one element
colors[2] # "green"

# indexing multiple elements using c()
colors[c(2, 4, 5)] # "green"   "brown"   "magenta"

# ignoring items 2 and 4 using c(-2, -4)
colors_new <- colors[c(-2, -4)]
print(colors_new) # "red"       "blue"      "magenta"   "violet"    "turquoise"
                  # deleted "green" and "brown"


#-------------------------------------------#
#------------- append new element ----------#
#-------------------------------------------#

colors <- c("red", "green", "blue")
print(colors)

#Append new element at positin length(vector) + 1
colors[length(colors)+1] = "brown"

print(colors)
