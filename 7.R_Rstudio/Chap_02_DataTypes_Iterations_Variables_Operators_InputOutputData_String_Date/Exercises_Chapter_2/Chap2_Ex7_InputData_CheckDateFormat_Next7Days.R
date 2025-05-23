is_valid_date <- function(date_string, format = "%d-%m-%Y") {
  parsed_date <- tryCatch(as.Date(date_string, format = format), error = function(e) NA)
  # Convert back to string to check if formatting round-trip matches
  return(!is.na(parsed_date) && format(parsed_date, format) == date_string)
}

date_string <- readline(prompt = "Input a date string with format dd-mm-YYY: ")

while (is_valid_date(date_string) == FALSE) {
  date_string <- readline(prompt = "Your date format is wrong, input again with format dd-mm-YYY: ")
}

date_string <- as.Date(date_string, format("%d-%m-%Y"))

next_seven_days <-seq(date_string, length = 7, by = 1)

print("7 continuing days:")
for (i in 1:length(next_seven_days)) {
  print(format(next_seven_days[i], format = "%d-%m-%Y"))
}
