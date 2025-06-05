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


#---------------------------------#
#--------- mutate() --------------#
#---------------------------------#

# mutate() helps add new columns or modify existing ones in a data frame or tibble.

# add new column Compare: if Attack > Defense, return 1, else return 0
df_pokemon_compare = df_pokemon %>%
  select(c("Name", "Type 1", "Attack", "Defense")) %>%
  mutate(Compare = ifelse(Attack > Defense, 1, 0))

head(df_pokemon_compare)


# add and modify multiple columns
## add Atk_level: if attack < 50 then 0, elif < 100 then 1, else 2
## modify Legendary: if FALSE then 0, else 1
df_pokemon_atk_lv = df_pokemon %>%
  select(c("Name", "Type 1", "Attack", "Legendary")) %>%
  mutate(
    Atk_level = ifelse(Attack < 50, 0, ifelse(Attack < 100, 1, 2)),
    Legendary = ifelse(Legendary == FALSE, 0, 1)
    ) %>%
  select(Name, `Type 1`, Attack, Atk_level, Legendary)  # Reorder columns

head(df_pokemon_atk_lv)