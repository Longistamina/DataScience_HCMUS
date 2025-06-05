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

#setwd("C:/Users/admin/Documents/Academic/DataScience_HCMUS/7.R_Rstudio/Chap_08_DataFrame_Tidyverse/")


#------------------------------------#
#-------- read pokemon.csv ----------#
#------------------------------------#

df_pokemon = read_csv("data_chap_08/pokemon.csv")
head(df_pokemon)


#-------------------------------#
#--------- filter() ------------#
#-------------------------------#

# filter() helps select rows satisfying specific conditions
# filter(input_df, conditon_1, condition_2, ...)
# input_df %>% filter(condition_1, condition_2)

# Filter rows where total range from [500, 600]
df_pokemon_500_600 = df_pokemon %>%
  filter((Total >= 500) & (Total <= 600)) # must be Total - NOT "Total"

head(df_pokemon_500_600)
str(df_pokemon_500_600)


## Note: if the column name has space character, 
## then put them in like this `column name` (like SQL)
df_pokemon_grass_poison = df_pokemon %>%
  filter((`Type 1` == "Grass") & `Type 2` == "Poison") # must be `Type 1` - NOT "Type 1"

head(df_pokemon_grass_poison)
str(df_pokemon_grass_poison)

# Filter rows where Attack > Defense
df_pokemon_atk_dfs = df_pokemon %>%
  filter(Attack > Defense)

head(df_pokemon_atk_dfs)
dim(df_pokemon_atk_dfs)