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


########################################################
# Example 1: use vector data and draw normal bar chart #
########################################################

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


##########################################################################
# Example 2: use matrix data and draw stacked bar chart, and add legends #
##########################################################################

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


##################################################################
# Example 4: use "beside = TRUE" to draw side-stacking bar chart #
##################################################################

year <- c(2014, 2015, 2016, 2017)
first_fallen <- c(309, 271, 263, 255)
one_hundred_fallen <- c(310, 314, 312, 304)

data_tree <- data.frame(
    row.names = year,
    first_fallen,
    one_hundred_fallen
)
print(data_tree)
#      first_fallen one_hundred_fallen
# 2014          309                310
# 2015          271                314
# 2016          263                312
# 2017          255                304

par(mar = c(5.1, 4.1, 4.1, 8.1), xpd = TRUE) # expand the right margin to make room for the legend

barplot(
    t(as.matrix(data_tree)), # Convert dataframe into matrix and transpose it
                             # By doing so, each column will represent a year
                             # so, each bar block will represent the data of each year
    beside = TRUE,
    main = "First and last fallen of leaf fall in Yellow Birch",
    col = c("brown", "orange")
)

legend(
    x = "bottomright",
    legend = c("first_fallen", "100%_fall"),
    fill = c("brown", "orange"),
    cex = 0.7,
    inset = c(-0.25, 0) 
)