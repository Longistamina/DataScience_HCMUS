score <- readline(prompt = "Input student's score: ")
score <- as.numeric(score)

if (score < 5.0) {
  print("Weak")
} else if (score < 7.0) {
  print("Average")
} else if (score < 8.0) {
  print("Good")
} else if (score < 9.0) {
  print("Very good")
} else {
  print("Excellent")
}