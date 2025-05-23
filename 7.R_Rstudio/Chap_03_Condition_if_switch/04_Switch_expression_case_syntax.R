# switch(expression, case1, case2, case3, ... caseN)
# switch will check which case the expression satisfies, then execute the code of that case
# if there are many satisfied cases (more than 1), then the first satisfied case will be chosen

## switch() checks index
x <- switch(2, "dog", "cat", "goat" )
print(x) #return "cat" as 2 is the index of "cat" in the string list

x <- switch(4, "dog", "cat", "goat")
print(x) #return NULL as no element in the list has index = 4


## switch() checks item's name
y <- switch("color", 
            "color" = "black", 
            "shape" = "straight", 
            "length" = 20)
print(y) #return "black" as "color" is the name of item "black"

y <- switch("from", 
            "color" = "black", 
            "shape" = "straight", 
            "length" = 20)
print(y) #return NULL as no item in the list has name = "from"


## Example: input arithmetic operator
number1 <- as.numeric(readline(prompt = 'Input number1: '))
number2 <- as.numeric(readline(prompt = 'Input number2: '))
operator <- readline(prompt = 'Input one ARITHMETIC operator: ')

switch(operator, 
       "+" = print(paste("Sum =", number1, "+", number2, "=", number1 + number2)),
       "-" = print(paste("Subtract =", number1, "-", number2, "=", number1 - number2)),
       "*" = print(paste("Multiply =", number1, "*", number2, "=", number1 * number2)),
       "/" = print(paste("Divide =", number1, "/", number2, "=", number1 / number2))
       )
