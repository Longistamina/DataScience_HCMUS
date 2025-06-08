#------------------------------------------#
#------ read_csv() and read_excel() -------#
#------------------------------------------#

# install.packages("readr")
# install.packages("readxl")

library(readr)  #This has read_csv() to read dataframe from .csv file into R
library(readxl) #This has read_excel() to read dataframe from .xlsx or .xls file into R

# read_csv("path/to/file.csv")
# read_excel("path/to/file.xlsx") or .xls

# setwd("C:/Users/admin/Documents/Academic/DataScience_HCMUS/7.R_Rstudio/Chap_08_DataFrame_Tidyverse/")

df_csv <- read_csv("data_chap_08/baseball.csv")
print(df_csv)

df_excel <- read_xlsx(
    "data_chap_08/Iris.xls", 
    sheet = 1, # Read the first sheet, or sheet = "sheet_name"
    skip = 0 # skip no row
) 

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


#----------------------------------------------------------------#
#------------ check if the read file is dataframe ---------------#
#----------------------------------------------------------------#

# check if the read data is dataframe
print(is.data.frame(df_csv))

print(is.data.frame(df_excel))


#---------------------------------------------------------#
#------------ write_csv() and write_xlsx() ---------------#
#---------------------------------------------------------#

# Below are the functions that helps write your dataframe into a .csv, .tsv or .xlsx files for storing

# write_csv() for .csv files
write_csv(
    df_csv, 
    file = "data_chap_08/written_df.csv", 
)

# write_tsv() for .tsv files
write_tsv(
    df_csv, 
    file = "data_chap_08/written_df.tsv", 
)

# write_xlsx() for excel files
library(writexl)
write_xlsx(
    df_excel,
    path = "data_chap_08/written_df.xlsx"
)