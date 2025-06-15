#------------------------------------------------------#
#--------------------- 2D pie chart -------------------#
#------------------------------------------------------#

# pie(x, labels, radius, main, col, clockwise)

## x:         a vector storing data for pie chart
## labels:    a vector storing the labels/names for each part
## radius:    the radius of the pie chart (from -1 to 1)
## main:      title of the pie chart
## col:       a vector storing colors hex code, or palette name to use
## clockwise: TRUE to draw clockwise, FALSE to draw anti-clockwise (default is FALSE)

###############
## Example 1 ##
###############

data_1 <- c(46, 37, 35, 53)
labels_1 <- c("10A1", "10A2", "10A3", "10A4")

pie(x = data_1, labels = labels_1)

pie(
    x = data_1,
    labels = labels_1,
    col = rainbow(length(data_1)), # create a rainbow palette according to the length of data_1 vector
    clockwise = TRUE, # Draw in clockwise direction
    main = "Number of students in each class"
)

##############################################################################
## Example 2: use table() to create frequency table of categorical variable ##
##############################################################################

data(iris)
head(iris, n = 3)
#   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
# 1          5.1         3.5          1.4         0.2  setosa
# 2          4.9         3.0          1.4         0.2  setosa
# 3          4.7         3.2          1.3         0.2  setosa

table(iris$Species)
# setosa versicolor  virginica 
#     50         50         50 

pie(x = table(iris$Species))

###########################################################
## Example 3: draw pie chart with percentage and legends ##
###########################################################

data_2 <- c(45, 46.5, 50, 35, 22)
data_2_percent <- round((100 * data_2) / sum(data_2), 2)

legend_labels <- c("HP", "Lenovo", "Asus", "Acer")

pie(
    x = data_2,
    labels = paste(data_2_percent, "%", sep = ""), # Use paste() to add the "%" into each element of data_2_percent
    col = rainbow(length(data_2)), # sep = "" so that it will be "45%" not "45 %"
    clockwise = TRUE,
    main = "Market share of some laptop producers"
)

legend(
    x = "topright", # x here is the position or coordinate of the legend table
    legend = legend_labels, # a character or expression vector of length ≥1 to appear in the legend
    cex = 0.8, # cex means character_expansion
    fill = rainbow(length(data_2)) # fill to add color pattern
)


#------------------------------------------------------#
#--------------------- 3D pie chart -------------------#
#------------------------------------------------------#

# To draw 3D pie chart, must use pie3D() from plotrix package
# The arguments are similar

# install.packages("plotrix")
# conda install -c conda-forge r-plotrix
library("plotrix")


# pie3D(x, labels, radius, main, col)

## x:         a vector storing data for pie chart
## labels:    a vector storing the labels/names for each part
## radius:    the radius of the pie chart (from -1 to 1)
## main:      title of the pie chart
## col:       a vector storing colors hex code, or palette name to use

###############
## Example 1 ##
###############
data_1 <- c(46, 37, 35, 53)
labels_1 <- c("10A1", "10A2", "10A3", "10A4")

pie3D(
    x = data_1,
    labels = labels_1,
    col = rainbow(length(data_1)), # create a rainbow palette according to the length of data_1 vector
    main = "Number of students in each class"
)


###########################################################
## Example 2: draw pie chart with percentage and legends ##
###########################################################data_2 <- c(45, 46.5, 50, 35, 22)
data_2_percent <- round((100 * data_2) / sum(data_2), 2)

legend_labels <- c("HP", "Lenovo", "Asus", "Acer")

pie3D(
    x = data_2,
    labels = paste(data_2_percent, "%", sep = ""), # Use paste() to add the "%" into each element of data_2_percent
    col = rainbow(length(data_2)), # sep = "" so that it will be "45%" not "45 %"
    main = "Market share of some laptop producers"
)

legend(
    x = "topright", # x here is the position or coordinate of the legend table
    legend = legend_labels, # a character or expression vector of length ≥1 to appear in the legend
    cex = 0.8, # cex means character_expansion
    fill = rainbow(length(data_2)) # fill to add color pattern
)
