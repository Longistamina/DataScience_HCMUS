
bmi_calculate <- function(height, weight) {
  bmi <- weight / (height^2)
  return(bmi)
}

###

bmi_classify <- function(bmi) {
  
  result <- ""
  
  if (bmi < 18.5) {
    result <- "Skinny"
  } else if (bmi < 25) {
    result <- "Normal"
  } else {
    result <- "Obese"
  }
}