# plot(x, y = NULL, main, type, col, xlab, ylab, xlim, ylim, lwd)

# x, y: the x and y coordinates for the plot
# main: main title
# xlab: label of x axis
# ylab: label of y axis
# xlim: limits of x axis
# ylim: limits of y axis
# col:  colors vector or palette
# lwd:  line width

# type: 1-character string giving the type of plot desired
#       "p" for points or scatterplot
#       "l" for lines plot
#       "b" for both points and lines
#       "c" for empty points joined by lines
#       "o" for overplotted points and lines
#       "s" and "S" for stair steps
#       "h" for histogram-like vertical lines
#       "n" for not produce any points or lines


#################################
## Example 1: single line plot ##
#################################

# Create sample data
x <- 1:10
y <- x^2
# Create a single line plot
plot(x, y, type = "l", main = "Single Line Plot", 
     xlab = "X values", ylab = "Y values", col = "blue", lwd = 3)


####################################
## Example 2: change xticks label ##
####################################

bears <- c(8, 54, 93, 116, 137)
plot(
     x = bears,
     type = "o",
     col = "red",
     xlab = "Year",
     ylab = "Bear count",
     main = "Number of bears over years",
     xaxt = "n" # This will remove the default xtick values 1, 2, 3, .. n
                # use "yaxt" for y axis
)
axis(
     side = 1,          # 1 means "below", 2 means "left", 3 means "above", 4 means "right"
     at = 1:5,          # the points at which tick-marks are to be drawn
     labels = 2017:2021 # labels to be placed at the tick points
)


###################################
## Example 3: multiple-line plot ##
###################################

# Create sample data
x <- 1:10
y1 <- x^2
y2 <- x^3
y3 <- sqrt(x)

# Create the first line
plot(x, y1, type = "l", col = "red", ylim = c(0, max(y2)), 
     main = "Multiple Line Plot", xlab = "X values", ylab = "Y values", lwd = 3)

# Add additional lines
lines(x, y2, col = "blue", lwd = 3)
lines(x, y3, col = "green", lwd = 3)

# Add a legend
legend("topleft", legend = c("x^2", "x^3", "sqrt(x)"), 
       col = c("red", "blue", "green"), lty = 1)