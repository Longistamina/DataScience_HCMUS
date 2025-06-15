# hist(x, main, xlab, xlim, ylim, breaks, col, border)

# x:      a vector of values for which the histogram is desired
# freq:   TRUE to draw frequency historgram, FALSE to draw density histogram (default is TRUE)
# main:   main title
# xlab:   label of x axis
# ylab:   label of y axis
# xlim:   limits of x axis
# ylim:   limits of y axis
# col:    colors vector or palette
# border: color of the cells' border

# breaks: a vector giving the breakpoints between histogram cells,
#         a function to compute the vector of breakpoints,
#         a single number giving the number of cells for the histogram,
#         a character string naming an algorithm to compute the number of cells (see ‘Details’),
#         a function to compute the number of cells.


data(airquality)

###############################################
## Example 1: draw histogram using frequency ##
###############################################

hist(
    x = airquality$Temp,
    main = "Histogram of Temperature",
    xlab = "Celcius degree",
    col = "orange",
    freq = TRUE # draw with frequency
)


#############################################
## Example 2: draw histogram using density ##
#############################################

hist(
    x = airquality$Temp,
    main = "Histogram of Temperature",
    xlab = "Celcius degree",
    col = "cyan4",
    freq = FALSE # draw with density
)

############################################################################
## Example 3: draw histogram with density (likelihood) line overlay on it ##
############################################################################

hist(
    x = airquality$Temp,
    main = "Histogram of Temperature",
    xlab = "Celsius degree",
    col = "#c37f4f",
    freq = FALSE  # Must use density scale for proper overlay
)

# Add density (likelihood) curve
# lines() function is to add a line plot into an already existed plot, not to draw new one
lines(density(airquality$Temp), col = "#6d16c3", lwd = 3)