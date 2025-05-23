# Can use "...." or '....' to create a string
# "" and '' are empty strings

a <- "one"
b <- 'two'
c <- 'three'

print(paste(a, b, c))

print(paste(a, b, c, sep = ', '))

print(paste(a, b, c, sep = ''))

# nchar() to count the number of character in a string
s <- "this is a string"
print(nchar(s))

# toupper() and tolower()
s1 <- "this is the first string"
print(toupper(s1))

s2 <- "THIS IS THE SECOND STRING"
print(tolower(s2))

# substring(original_string, first, last)
s <- "this is the first string"
sub_s <- substring(s, first = 5, last = 18)
print(sub_s)

# chartr(old, new, original_string) to replace a character with another character in the string
s <- "Today is New Year day"
print(chartr(" ", "_", s))

# strsplit(original_string, delimiter) to split a string in to a list
s <- "Today is New Year day"
char_list <- strsplit(s, " ") #return a list object
word_list <- unlist(char_list) #use unlist() to make it become a vector
print(word_list)

# sort(x, decreasing = FALSE, ...) to sort a list of numeric or character values
sorted_list <- sort(word_list, decreasing = FALSE)
print(sorted_list)

sorted_list <- sort(word_list, decreasing = TRUE)
print(sorted_list)

