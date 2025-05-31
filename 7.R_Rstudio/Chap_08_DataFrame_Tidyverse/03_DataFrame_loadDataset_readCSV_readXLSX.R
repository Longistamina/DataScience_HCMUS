3#--------------------------------------#
#----------- built-in dataset ----------#
#---------------------------------------#

# R has many built-in datasets for practicing

# ls() displays all current loaded or created dataframes in current environment
ls()

# data() displays all built-in datasets of R
data()

# data(dataset_name) to load a specific dataset into the environment
data("mtcars")

print(mtcars)

summary(mtcars)


#------------------------------------------#
#------ read_csv() and read_excel() -------#
#------------------------------------------#

# install.packages("readr")
# install.packages("readxl")

library(readr)  #This has read_csv() to read dataframe from .csv file into R
library(readxl) #This has read_excel() to read dataframe from .xlsx or .xls file into R

# read_csv("path/to/file.csv")
# read_excel("path/to/file.xlsx") or .xls

setwd("C:/Users/admin/Documents/Academic/DataScience_HCMUS/7.R_Rstudio/Chap_08_DataFrame_Tidyverse/")

df_csv <- read_csv("data_chap_08/baseball.csv")
print(df_csv)

df_excel <- read_excel("data_chap_08/Iris.xls")
print(df_excel)

# All read commands for csv-type files:
## read_delim()
## read_csv()
## read_csv2()
## read_tsv()

# All read commands for excel-type files:
## read_excel()
## read_xls()
## read_xlsx()

