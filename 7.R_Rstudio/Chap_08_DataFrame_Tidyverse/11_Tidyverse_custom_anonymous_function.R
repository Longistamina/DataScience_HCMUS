# Tidyverse offers purr and magritrr to create custom functions inside the %>% pipeline
# like .pipe(lambda df: df....) in Python
# This helps execute commands that are not originall support by tidyverse (as example below)

library(tidyverse)

data("mtcars")

# Sample data
input_df <- mtcars
head(input_df)

#-------------------------------#
#--------- Example 1 -----------#
#-------------------------------#

# Chain with magrittr and purrr-style lambda
output_df <- input_df %>%
  filter(mpg > 20) %>%
  { 
    # This block is like lambda df: ...
    x <- .
    colnames(x)[colnames(x) == "cyl"] <- "cylinder"
    x
  }

# {...} a code block that acts like an anonymous function (similar to Python’s lambda df: ...)

# . is the current piped dataframe (filtered df with mpg > 20)
# the symbol . is a placeholder that represents the value being passed along the pipe at that point.

# x <- . to assign it to x as a convenient variable name (you could also just use . directly)

# colnames(x)[colnames(x) == "cyl"] <- "cylinder"
## => this to change the column name "cyl" into "cylinder"
##    without creating new column

head(output_df)
