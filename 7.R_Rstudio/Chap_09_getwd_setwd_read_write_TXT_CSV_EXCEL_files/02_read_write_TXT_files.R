data_path <- "data_chap_09/demo_data/"

#-------------------------------------------------------------------#
#---------------------- use readLines() ----------------------------#
#-------------------------------------------------------------------#

# readLines() return a list/vector contain all lines/elements of the text

content_1 <- readLines(paste(data_path, "license.txt", sep = ""))
print(content_1)
# [1] "These data files are derived by splitting up the data set downloaded from:"
# [2] "https://www.ontario.ca/data/ontario-public-schools-enrolment"              
# [3] "under the Open Government License - Ontario:"                              
# [4] "https://www.ontario.ca/page/open-government-licence-ontario"      

print(length(content_1)) # Count the number of lines (or vectors) of this text
                         #4

print(nchar(content_1)) # Count the number of characters (elements) of each line (vector) from this text
                        # 74 60 44 59

content_2 <- readLines(paste(data_path, "license.txt", sep = ""), encoding = "UTF-8") #For vietnamese
print(content_2)
# [1] "Mùa xuân là Tết trồng cây"           
# [2] "Làm cho đất nước càng ngày càng xuân"
# [3] ""
print(length(content_2))
print(nchar(content_2))

# file.size() returns the size of the file in bytes
print(file.size("data_chap_09/demo_data/bai_tho.txt")) # 89 (means 89 bytes)


#--------------------------------------------------------------#
#---------------------- use scan() ----------------------------#
#--------------------------------------------------------------#

# scan() works like .split() or re.split() in Python
# it split the text into many elements based on a given delimiter ("," or " " ....)

# default, scan() treats inputs as real
# so, to scan text file, must set what = character()

lst_content_2 <- scan(paste(data_path, "bai_tho.txt", sep = ""), encoding = "UTF-8", sep = " ", what = character())
print(lst_content_2)
print(length(lst_content_2))
# [1] "Mùa"   "xuân"  "là"    "Tết"   "trồng" "cây"   "Làm"   "cho"   "đất"  
# [10] "nước"  "càng"  "ngày"  "càng"  "xuân" 
# 14 elements (words)


#--------------------------------------------------------------------#
#---------------------- use read.table() ----------------------------#
#--------------------------------------------------------------------#

# read.table() helps read table-type txt file and returns a DATAFRAME

txt_table <- read.table(paste(data_path, "Table0.txt", sep = ""))
print(txt_table)
print(class(txt_table)) #"data.frame"


#------------------------------------------#
#------------- use write() ----------------#
#------------------------------------------#

# write() helps write a bunch of contents into a text file

# use file() to open a file
content_to_write = "Odin the Alfather"

file_name <- file(
    description = paste(data_path, "written_text.txt", sep = ""), #define a path to .txt file to open and write
    open = "a", #open mode is append
    encoding = "UTF-8"
)

write(content_to_write, file = file_name) # Write the content_to_write to the writtent_text.txt
                                          # find and open the writtent_text.txt to check


#------------------------------------------------#
#------------- use write.table() ----------------#
#------------------------------------------------#

# write.table() helps write table-type text into .csv or .tsv (NOT support .xlsx or excel files)

df_to_write = data.frame(
    "ID" = c(1, 2, 3),
    "Name" = c("Sensan", "Normadic", "Linking"),
    "Age" = c(18.2, 14.3, 12.1)
)

write.table(
    df_to_write,
    file = paste(data_path, "written_table.txt", sep = ""), # or .csv or .tsv
    sep = "\t",
    row.names = FALSE
)

# row.names = FALSE to avoid writing row names as a separate column.
# quote = TRUE to enclose all character or factor data in double quotes (" ")