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


#-------------------------------#
#--------- count() -------------#
#-------------------------------#

# count() will return the frequency of each unique value in a column

# Count the frequency of each pokemon type (Type 1)
type_1_count <- df_pokemon %>% 
  count(`Type 1`)

print(type_1_count)


#------------------------------#
#------- sample_n() -----------#
#------------------------------#

# sample_n(size) randomly samples a NUMBER of rows from a data frame or tibble.

# pick out 5 random samples from df_pokemon
pokemon_5 = df_pokemon %>%
  sample_n(5)

print(pokemon_5)


#---------------------------------#
#------- sample_frac() -----------#
#---------------------------------#

# sample_fract() randomly samples a FRACTION/PERCENTAGE of rows from a data frame or tibble.

# pick out randomly 20% rows from df_pokemon
pokemon_20percent = df_pokemon %>%
  sample_frac(0.2)

head(pokemon_20percent)

dim(pokemon_20percent) # 20% of 800 rows = 160 rows