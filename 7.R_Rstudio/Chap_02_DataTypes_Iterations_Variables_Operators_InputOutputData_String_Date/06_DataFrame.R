#DataFrame is a 2D iteration like matrix, but it contains many different datatypes

#Create dataframe
BMI <- data.frame(
  gender = c("Male", "Male", "Female"),
  height = c(152, 171.5, 165),
  weight = c(81, 93, 78),
  age = c(42, 38, 26)
)

print(BMI)