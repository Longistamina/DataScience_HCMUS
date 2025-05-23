name <- readline(prompt = "Input your name: ")
YoB <- readline(prompt = "Input your year of birth: ")
weight <- as.numeric(readline(prompt = "Input your weight: "))
height <- as.numeric(readline(prompt = "Input your height: "))

BMI <- weight/(height^2)

cat("Name: ", name, "\n",
    "Year of birth: ", YoB, "\n",
    "Weight (kg): ", weight, "\n",
    "Height (m): ", height, "\n",
    "BMI: ", BMI, 
    sep = "")
