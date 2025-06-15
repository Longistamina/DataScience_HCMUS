# plot(x, y = NULL, main, type, col, xlab, ylab, xlim, ylim, pch, axes)

# x, y: the x and y coordinates for the plot
# main: main title
# xlab: label of x axis
# ylab: label of y axis
# xlim: limits of x axis
# ylim: limits of y axis
# col:  colors vector or palette
# pch:  style of the points
# axes: a logical value indicating whether both axes should be drawn on the plot

# type: 1-character string giving the type of plot desired
#       "p" for points or scatterplot
#       "l" for lines plot
#       "b" for both points and lines
#       "c" for empty points joined by lines
#       "o" for overplotted points and lines
#       "s" and "S" for stair steps
#       "h" for histogram-like vertical lines
#       "n" for not produce any points or lines


###################################
## Example 1: normal scatterplot ##
###################################

data(mtcars)

plot(
    x = mtcars$wt,
    y = mtcars$mpg,
    type = "p",
    xlim = c(1, 6),
    ylim = c(10, 40),
    main = "Weight vs Milage",
    col = "#5c8516"
)


####################################################################
## Example 2: add linear model line to scatterplot using abline() ##
####################################################################

# Draw scatterplot first
plot(
    x = faithful$eruptions,
    y = faithful$waiting,
    type = "p",
    main = "Eruptions vs Waiting",
    xlab = "Eruptions",
    ylab = "Waiting",
    col = "chocolate3",
    cex = 1.2,
    pch = 8,
    xlim = c(1.0, 6.0),
    ylim = c(40, 100)
)

# add linear model line using abline()
abline(lm(faithful$waiting ~ faithful$eruptions), col = "red", lwd = 3)


#################################################
## Example 3: matrix scatterplot using pairs() ##
#################################################

pairs(
    formula = ~wt + mpg + disp + cyl, # the "~" at the beginning of the expressing to makes R interpret this as a formula, not a mathematical expression
    data = mtcars,
    main = "Wt vs Mpg vs Disp vs Cyl",
    col = "#611c1ccb"
)
