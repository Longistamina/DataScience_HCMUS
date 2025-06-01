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


#----------------------------#
#-------- select() ----------#
#----------------------------#

# select() selects columns based on column names or indices

# select columns whose indices are 2, 5, 7 and 8
df_pokemon_sub = select(df_pokemon, c(2, 5, 7, 8))
head(df_pokemon_sub)

# using %>% to select column based on names
df_pokemon_sub = df_pokemon %>%
  select(c("Name", "Type 1", "Total", "Legendary"))

head(df_pokemon_sub)


####### reorder column using select() ######
df_pokemon_sub_reorder = df_pokemon %>%
  select(c("Name", "Type 1", "Total", "Legendary")) %>%
  select(c(Name, Total, `Type 1`, Legendary)) # Reorder column
                                              # use `Type 1` because it has space character

head(df_pokemon_sub_reorder)
  

head(df_pokemon_sub)

#-------------------------------#
#-------- select_if() ----------#
#-------------------------------#

# select_if() selects columns based on a condition (predicate function)
# select_if(data, predicate_function)

# select_if() with is.numeric as predicate function to get the numeric columns only
df_pokemon_sub = df_pokemon %>%
  select_if(is.numeric)

head(df_pokemon_sub)
str(df_pokemon_sub) #Have only numeric columns

