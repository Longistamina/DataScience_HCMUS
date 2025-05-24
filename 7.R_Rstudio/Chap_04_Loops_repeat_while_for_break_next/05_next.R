# next: move to the next looping round if a condition is satisfied

numbers <- seq(1, 10, 1)

for (num in numbers) {
  if ((num %% 2) != 0) {
    next
  }
  cat(num, "is an event number\n")
}
