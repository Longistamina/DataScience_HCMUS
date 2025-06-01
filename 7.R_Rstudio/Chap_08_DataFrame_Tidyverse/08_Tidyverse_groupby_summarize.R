# Tidyverse is a popular and powerful package in R for data processing and wrangling
# Tidyverse contains also dplyr and ggplot2

# Some main commands in tidyverse:
## arrange()
## filter()
## mutate()
## select()
## summarize()

# output_df <- function(input_df, conditions)

# output_df <- input_df %>% 
#     function_1(conditions) %>% 
#     function_2(conditions) %>%
#     function_3(conditions) %>%


# install.packages("tidyverse")
library(tidyverse)

setwd("C:/Users/admin/Documents/Academic/DataScience_HCMUS/7.R_Rstudio/Chap_08_DataFrame_Tidyverse/")


#------------------------------------#
#-------- read pokemon.csv ----------#
#------------------------------------#

df_pokemon = read_csv("data_chap_08/pokemon.csv")
head(df_pokemon)


#---------------------------------------------#
#------- group_by() and summarize() ----------#
#---------------------------------------------#

# group_by() and summarize() (or summarise() in British spelling) are commonly used to 
## group data by one or more variables 
## and then compute summary statistics for each group.

## This is like .groupby() then .agg(aggregate_function) in Python pandas

df_pokemon_summary = df_pokemon %>%
  group_by(`Type 1`) %>% #Group pokemon df by `Type 1` variable
  summarize(
    count = n(), # n() gives the current group size
    mean_Atk = mean(Attack, na.rm = T), # remove NA is TRUE
    median_Atk = median(Attack, na.rm = T),
    mean_Def = mean(Defense, na.rm = T),
    median_Def = median(Defense, na.rm = T)
  )

head(df_pokemon_summary)