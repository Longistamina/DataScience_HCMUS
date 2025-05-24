# break: help escape a loop when a condition is satisfied

x <- 1

while (TRUE) {
  print(x)
  x = x + 1
  
  if (x > 5) {
    print("Time to break!!!")
    break
  }
}
