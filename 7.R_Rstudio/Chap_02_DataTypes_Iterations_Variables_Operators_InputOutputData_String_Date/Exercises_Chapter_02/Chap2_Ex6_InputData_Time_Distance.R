input_date <- readline(prompt = "Input a date with format dd-mm-YYY: ")

input_date <- as.Date(input_date, format("%d-%m-%Y"))

cat(
  "Input date: ", paste(input_date), "\n", #use paste(input_date) to pass it as string, not timestamp
  "Current date: ", paste(Sys.Date()), "\n",
  "=================================\n",
  "Time difference in weeks: ", abs(difftime(Sys.Date(), input_date, units = 'weeks')), "\n",
  "Time difference in days: ", abs(difftime(Sys.Date(), input_date, units = 'days')), "\n",
  sep = ""
)
