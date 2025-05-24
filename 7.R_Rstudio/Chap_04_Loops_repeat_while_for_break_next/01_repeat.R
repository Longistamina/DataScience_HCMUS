# repeat: execute commands first, then check the break condition

# repeat {
#   commands
#   if (break condition) {
#      break
#   }
# }

time <- 1

repeat {
  print(paste("Time: ", time))
  time <- time + 1
  if (time > 5) {
    break
  }
}

############

# In GoogleColab or JupyterNotebook, use message() to display text after each loop
# Otherwise (using print()), they will wait until the loop ends to show all text

# In R, can use cat(), print() or message