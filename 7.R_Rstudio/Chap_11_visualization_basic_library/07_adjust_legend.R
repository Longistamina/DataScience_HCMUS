# To avoid the overlap between the legend and the plot, do as below

# First, expand the right margin to make room for the legend
par(mar = c(5.1, 4.1, 4.1, 8.1), xpd = TRUE)

# Then draw your plot
# pie(....)
# barplot(....)

# Now add legend with inset()
legend(
    x = "topright",          # x here is the position or coordinate of the legend table
    legend = legend_labels,  # a character or expression vector of length ≥1 to appear in the legend
    cex = 0.9,               # cex means character_expansion
    fill = colors,           # fill to add color pattern for each legend color box
    inset = c(-0.25, 0)      # This pushes the legend outside the plot boundary
)
