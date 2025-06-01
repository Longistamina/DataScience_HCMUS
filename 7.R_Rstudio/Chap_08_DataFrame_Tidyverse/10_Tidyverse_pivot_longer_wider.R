# In the tidyverse (specifically the tidyr package), 
# the functions pivot_longer() and pivot_wider() are used to reshape data:

library(tidyverse)
setwd("C:/Users/admin/Documents/Academic/DataScience_HCMUS/7.R_Rstudio/Chap_08_DataFrame_Tidyverse/")

#------------------------------#
#----- pivot_longer() ---------#
#------------------------------#

# Use when: You have multiple columns that represent values of a single variable 
# and you want to gather them into two columns: 
#       + one for the column names (variable type) 
#       + and one for the values.

# convert to long format or tall format

# this is like pandas.melt() in Python

# Sample wide data
df_wide <- tibble(
  name = c("Alice", "Bob"),
  math = c(90, 85),
  science = c(95, 88)
)
print(df_wide)

# Convert to long format or tall format
df_long <- df_wide %>%
  pivot_longer(
    cols = math:science,   # columns to pivot
    names_to = "subject",  # new column with original column names
    values_to = "score"    # new column with values
  )
print(df_long)


#-----------------------------#
#----- pivot_wider() ---------#
#-----------------------------#

# Use when: You have a column with variable types and another with values, 
# and you want to spread them into multiple columns.

# convert to wide format

# This is like pandas.pivot() or pandas.pivot_table() in Python

# Example data: Student scores across multiple exams
df_long <- tibble(
  student = c("Alice", "Alice", "Bob", "Bob"),
  exam = c("midterm", "final", "midterm", "final"),
  score = c(88, 93, 75, 80)
)
print(df_long)

# Use pivort_wider() to convert long to wide format
df_wide <- df_long %>%
  pivot_wider(
    names_from = exam,      # Use exam types as column names
    values_from = score     # Fill cells with scores
  )
print(df_wide)