# Tidyverse offers purr and magritrr to create custom functions inside the %>% pipeline
# like .pipe(lambda df: df....) in Python


data("mtcars")

# Sample data
df <- mtcars


#-------------------------------#
#--------- Example 1 -----------#
#-------------------------------#

# Chain with magrittr and purrr-style lambda
output_df <- df %>%
  filter(mpg > 20) %>%
  { 
    # This block is like lambda df: ...
    .x <- .
    .x$power_to_weight <- .x$hp / .x$wt
    .x
  }

# {...} a code block that acts like an anonymous function (similar to Python’s lambda df: ...)

# . is the current piped dataframe (filtered df with mpg > 20)
# the symbol . is a placeholder that represents the value being passed along the pipe at that point.

# .x <- . to assign it to .x as a convenient variable name (you could also just use . directly)

# .x$power_to_weight <- .x$hp / .x$wt
#     Create a new column named "power_to_weight"
#     Calculates horsepower divided by weight (.x$hp / .x$wt)
#     This new column is added to .x

print(output_df)
