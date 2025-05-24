multiplicators <- seq(1, 10, 1)

######################## one column of multiplicand

multiplicand <- as.integer(readline(prompt = "Input your multiplicand: "))

print(paste("\nMultiplication table of ", multiplicand))

s = ""
for (number in multiplicators) {
  s <- paste(s,"\n", multiplicand, "x", number, "=", multiplicand*number)
}

cat(s)


######################## many columns of multiplicands

begin <- as.integer(readline(prompt = "Input your begin multiplicand: "))
end <- as.integer(readline(prompt = "Input your end multiplicand: "))

s = ""
for (i in multiplicators) {
  for (j in c(begin : end)) {
    s <- paste(s, '\t', j, 'x', i, '=', j*i)
  }
  s <- paste(s, '\n')
}

cat(s)