# Create a vector named friends, containing the name of 3 friends
# Write a loop to input new friends' name into the vector
# Set condition to stop the loop

friends_vector <- c("Andy", "Bacon", "Cindy")
len_friends <- length(friends_vector)

repeat {
  new_friend = readline(prompt = "Input the name of a new friend: ")
  friends_vector[len_friends + 1] = new_friend
  len_friends <- length(friends_vector)
  
  i <- readline(prompt = "Continue: 1, Stop: others ___ Your choice: ")
  cat(" ")
  if (i != "1") {
    break
  }
}

cat("There are ", len_friends, " in your friend list.",
    "\nThey are: ", paste(friends_vector, collapse = ", "), sep = "")
