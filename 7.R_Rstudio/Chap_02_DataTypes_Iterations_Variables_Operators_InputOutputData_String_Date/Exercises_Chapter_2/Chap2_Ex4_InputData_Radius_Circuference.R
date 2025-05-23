area_circle <- as.numeric(readline(prompt = "Input area of a circle: "))

radius <- sqrt(area_circle/pi)
circumference_circle <- 2*pi*radius

cat("Area of the circle: ", area_circle, "\n",
    "====================================", "\n",
    "Radius (approximate): ", round(radius, digits = 2), "\n", 
    "Circumference of the circle (approximate): ", round(circumference_circle, digits = 2), 
    sep = "")
