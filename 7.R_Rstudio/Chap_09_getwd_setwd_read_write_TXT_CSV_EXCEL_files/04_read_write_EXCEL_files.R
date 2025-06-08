# install.packages("xlsx")
# conda install -c conda-forge r-xlsx

#-------------------------------------------------#
#----------------- read.xlsx() -------------------#
#-------------------------------------------------#

library(xlsx)

emp_xlsx = read.xlsx(
    file = "data_chap_09/demo_data/emp_data.xlsx",
    sheetName = "emp", #read from sheet "emp", or "sheet = 1" to read the first sheet
    startRow = NULL,
    endRow = NULL
)
print(emp_xlsx)


city_xlsx = read.xlsx(
    file = "data_chap_09/demo_data/emp_data.xlsx",
    sheetIndex = 2, #read from the 2nd sheet, or "city" sheet
    startRow = NULL,
    endRow = NULL
)
print(city_xlsx)


#--------------------------------------------------#
#----------------- write.xlsx() -------------------#
#--------------------------------------------------#

library(tidyverse)
medals_gold <- read.csv("data_chap_09/demo_data/medals.csv") %>%
    filter(Medal == "Gold")
head(medals_gold)

######
library(xlsx)

# write into a new .xlsx file
write.xlsx(
    medals_gold,
    file = "data_chap_09/demo_data/medals_gold.xlsx"
)

# write into an existed .xlsx file, define the sheet name
write.xlsx(
    medals_gold,
    file = "data_chap_09/demo_data/medals_new.xlsx",
    sheetName = "Gold",
    append = TRUE # This helps avoid overwriting the existed sheet 1
)
# check the medals_new.xlsx sheet "Gold" to see the result