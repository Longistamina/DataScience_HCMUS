# source: this command help import and use a user-defined function from a separate .R file

# source(path_to_function/function.R)

source('BMI_practice_functions/bmi_functions.R')
# There are 2 user-defined functions in bmi_functions.R
# This command will import all 2 functions into this script

h = 1.8
w = 90

bmi <- bmi_calculate(height = h, weight = w)

bmi_type <- bmi_classify(bmi)

cat(
    "BMI: ", bmi, '\n',
    "Type: ", bmi_type,
    sep = "")