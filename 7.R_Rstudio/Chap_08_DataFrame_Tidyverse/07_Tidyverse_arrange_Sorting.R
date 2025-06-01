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

df_pokemon = read_csv("data_chap_08/pokemon.csv") %>%
  select(Name, `Type 1`, `Type 2`, Total, HP, Attack, Defense)

head(df_pokemon)


#-----------------------------------------#
#------------- arrange() -----------------#
#-----------------------------------------#

# arrange() is used to sort rows of a data frame (or tibble) by the values of one or more columns.

### sort Total column ascending
df_pokemon_asc <- df_pokemon %>%
  arrange(Total)

head(df_pokemon_asc)


### sort Total column descending
df_pokemon_desc <- df_pokemon %>%
  arrange(desc(Total))

head(df_pokemon_desc)


### sort multiple columns
df_pokemon_sort_mult <- df_pokemon %>%
  arrange(Total, desc(HP), Attack, desc(Defense)) # first one Total has the highest priority

head(df_pokemon_sort_mult)