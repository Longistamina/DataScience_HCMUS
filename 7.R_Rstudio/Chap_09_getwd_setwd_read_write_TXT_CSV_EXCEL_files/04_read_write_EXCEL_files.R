#-------------------------------------------------#
#----------------- read_xlsx() -------------------#
#-------------------------------------------------#

# install package "readxl" to read excel files
# install.packages("readxl")

library(readxl)

emp_xlsx = read_xlsx(
    path = "data_chap_09/demo_data/emp_data.xlsx",
    sheet = "emp", #read from sheet "emp", or "sheet = 1" to read the first sheet
    skip = 0 # skip rows = 0
)
print(emp_xlsx)


city_xlsx = read_xlsx(
    path = "data_chap_09/demo_data/emp_data.xlsx",
    sheet = 2, #read from the 2nd sheet, or "city" sheet
    skip = 0 # skip rows = 0
)
print(city_xlsx)


#--------------------------------------------------#
#----------------- write_xlsx() -------------------#
#--------------------------------------------------#

medals_gold <- read.csv("data_chap_09/demo_data/medals.csv") %>%
    filter(Medal == "Gold")
head(medals_gold)

# install package "writexl" to write excel files
# install.packages("writexl")
# conda install -c conda-forge r-writexl (do this in venv terminal)

library(writexl)

write_xlsx(
    medals_gold,
    path = "data_chap_09/demo_data/medals_gold.xlsx"
)