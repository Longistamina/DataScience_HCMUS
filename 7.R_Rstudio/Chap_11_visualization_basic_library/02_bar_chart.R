# barplot(height, xlab, ylab, main, names.arg, col)

# height:    either a vector or matrix of values describing the bars which make up the plot
# xlim:      limits of the x axis
# ylim:      limits of the x axis
# xlab:      label of x axis
# ylab:      label of y axis
# main:      name of the plot
# names.arg: a vector of names to be plotted below each bar or group of bars
# col:       a vector of colors for the bars or bar components (default is "grey")
# border:    color of the blocks' border


## Example 1: use vector data and draw normal bar chart
data_1 <- c(5, 10, 20, 5)
block_names <- c("Excellent", "Very good", "Good", "Medium")

barplot(
    height = data_1,
    xlab = "Grade",
    ylab = "Student counts",
    names.arg = block_names,
    main = "Grade of Class 10A1",
    col = "cyan4",
    border = "brown4"
)


## Example 2: use matrix data and draw stacked bar chart, and add legends
classes <- c("10A1", "10A2", "10A3")
grades <- c("Excellent", "Very good", "Good", "Medium")

grades_matrix <- matrix(
    c(5, 6, 7, 15, 14, 13, 20, 21, 22, 5, 4, 3),
    nrow = 4, ncol = 3,
    byrow = TRUE,
    dimnames = list(grades, classes)
)

print(grades_matrix)
#           10A1 10A2 10A3
# Excellent    5    6    7
# Very good   15   14   13
# Good        20   21   22
# Medium       5    4    3

colors <- c("darkolivegreen2", "chocolate", "darkcyan", "firebrick3")

# First, expand the right margin to make room for the legend
par(mar = c(5.1, 4.1, 4.1, 8.1), xpd = TRUE)

# draw stacked bar chart
barplot(
    height = grades_matrix, # Since the input data is a matrix, R will treat each column as each bar block
    names.arg = classes,
    xlab = "Grade",
    ylab = "Student counts",
    main = "Grade of 3 classes",
    col = colors
)

# add legend
legend(
    x = "topright",
    legend = grades,
    cex = 0.9,
    fill = colors,
    inset = c(-0.25, 0) # This pushes the legend outside the plot boundary
)
