# boxplot(formula, data, notch, varwidth, names, xlab, ylab, main))
# boxplot(x, data, notch, varwidth, names, xlab, ylab, main)

# formula:  a formula, such as ‘y ~ grp’, where ‘y’ is a numeric vector
#           of data values to be split into groups according to the
#           grouping variable ‘grp’ (usually a factor)

# x:        a vector of data values as input for boxplot
# data:     a data.frame (or list) from which the variables in ‘formula’ should be taken
# notch:    set TRUE to draw the notch, default is FALSE
# varwidth: set TRUE to draw the boxes' widths proportional to the square-roots of the number of observations in the groups
# names:    group labels which will be printed under each boxplot
# xlab:     label of x axis
# ylab:     label of y axis
# main:     name of the plot
# col:       a vector of colors for the bars or bar components (default is "grey")

df_baseball <- read.csv("data_chap_11/baseball.csv")
head(df_baseball)


######################################
## Example 1: boxplot with no notch ##
######################################

boxplot(
    x = df_baseball$height,
    main = "Height of baseball players",
    col = "darkseagreen1",
    ylab = "meters"
)


###################################
## Example 2: boxplot with notch ##
###################################

boxplot(
    x = df_baseball$weight,
    notch = TRUE,
    varwidth = TRUE,
    main = "Weight of baseball players",
    col = "chocolate",
    ylab = "kilograms"
)


#####################################################################
## Example 3: boxplot many groups/boxes using formula 'y ~ groups' ##
#####################################################################

boxplot(
    formula = Temp ~ Month, 
    data = airquality,
    main = "Different boxplots for each month",
    notch = TRUE,
    xlab = "Month Number",
    ylab = "Degree Fahrenheit",
    col = c("orange", "cyan4", "firebrick3", "darkolivegreen2"),
    border = "black"
)


###################################################################################
## Example 4: boxplot with 2 crossed factors using formula 'y ~ group1 * group2' ##
###################################################################################

boxplot(
        formula = len ~ supp * dose, 
        data = ToothGrowth, 
        notch = TRUE, 
        col = c("gold", "darkgreen"),
        main = "Tooth Growth", 
        xlab = "Supplement and Dose"
)
# Color pattern:
#   OJ supp + 0.5 dose: gold
#   VC supp + 0.5 dose: darkgreen
#   OJ supp + 1.0 dose: gold
#   VC supp + 1.0 dose: darkgreen
#   OJ supp + 2.0 dose: gold
#   VC supp + 2.0 dose: darkgreen


######################################################################################
## Example 5: boxplot with factor(categ_variable) using formula 'y ~ factor(group)' ##
######################################################################################

boxplot(
    formula = mpg ~ am * factor(cyl), # Must convert the numeric variable "cyl" into factor datatype
    data = mtcars,
    notch = TRUE, 
    col = c("#a63e3e", "#3423d1")
)

