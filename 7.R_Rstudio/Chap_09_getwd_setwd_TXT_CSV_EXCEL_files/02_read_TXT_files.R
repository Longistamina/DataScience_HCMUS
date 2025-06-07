#-------------------------------------------------------------------#
#---------------------- use readLines() ----------------------------#
#-------------------------------------------------------------------#
content_1 <- readLines("data_chap_09/demo_data/license.txt")
print(content_1)
# [1] "These data files are derived by splitting up the data set downloaded from:"
# [2] "https://www.ontario.ca/data/ontario-public-schools-enrolment"              
# [3] "under the Open Government License - Ontario:"                              
# [4] "https://www.ontario.ca/page/open-government-licence-ontario"      

print(length(content_1)) # Count the number of lines (or vectors) of this text
                         #4

print(nchar(content_1)) # Count the number of characters (elements) of each line (vector) from this text
                        # 74 60 44 59

content_2 <- readLines("data_chap_09/demo_data/bai_tho.txt", encoding = "UTF-8") #For vietnamese
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

lst_content_2 <- scan("data_chap_09/demo_data/bai_tho.txt", encoding = "UTF-8", sep = " ", what = character())
print(lst_content_2)
print(length(lst_content_2))
# [1] "Mùa"   "xuân"  "là"    "Tết"   "trồng" "cây"   "Làm"   "cho"   "đất"  
# [10] "nước"  "càng"  "ngày"  "càng"  "xuân" 
# 14 elements (words)