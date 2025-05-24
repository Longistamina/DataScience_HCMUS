# while: check the break condition first, then execute commands

# while (break condition) {
#   commands
# }

time <- 1

while (time <= 5) {
  print(paste("Time: ", time))
  time <- time+1
}

#############

i = 1

while (i == 1) {
  cat("\nHello!\n\n")
  cat("Continue or Stop?\n 1: Continue\n others: Stop\n")
  i = readline(prompt =  "Your choice: ")
  i = as.numeric(i)
  if (i != 1) {
    cat("You chose Stop")
  } else {
    cat("You chose Continue")
  }
}

############

# In GoogleColab or JupyterNotebook, use message() to display text after each loop
# Otherwise (using print()), they will wait until the loop ends to show all text

# In R, can use cat(), print() or message
