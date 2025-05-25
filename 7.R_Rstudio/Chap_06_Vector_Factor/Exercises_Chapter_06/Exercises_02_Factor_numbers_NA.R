x <- c(1, 2, 3, 3, 5, 3, 2, 4, NA, 11, 22, 47, 47, 11, 47, 11)
print(x)

x_factor <- factor(x)
print(x_factor)

print(levels(x_factor)) # The NA is not considered as a level, so it was discarded

print(nlevels(x_factor))