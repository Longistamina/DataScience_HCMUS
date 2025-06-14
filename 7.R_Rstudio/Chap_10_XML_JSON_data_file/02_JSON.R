
setwd("/home/longdpt/Documents/Academic/DataScience_HCMUS/7.R_Rstudio/Chap_10_XML_JSON_data_file/")

# JSON is a lightweight text format designed for data transfering
# JSON is driven from JavaSript
# The extension (tail) of a JSON file is .json
# Most platforms and programming languages nowadays, if not all, can read and process .json file

#-------------------------------------------------#
#-------------- JSON file structure --------------#
#-------------------------------------------------#

# {"book": [
#     {
#         "title": "Applied Linear Statistical Models",
#         "publisher": "McGraw Hill",
#         "isbn": "9780073108742",
#         "pages": "1396",
#         "author": [
#             "Michael Kutner",
#             "William Li",
#             "Christopher Nachtsheim",
#             "John Neter"
#         ],
#         "attribute": [
#             "Exercises",
#             "Illustrations",
#             "Readability"
#         ]
#     },
# ....
# }

# Data in .json file is store as "key":value format like Dictionary in Python
# (NOTE: the key in .json file must ALWAYS be a STRING, i.e in side quotes '' or double quotes "")

# Each {} represents an object
# Each [] represents a list

# JSON support these datatypes:
#   string
#   object (JSON object)
#   array
#   boolean
#   null

# NOT SUPPORT function, date and "undefined"


########## Install library

# install.packages("httr")
# install.packages("jsonlite")

# conda install -c conda-forge r-httr r-jsonlite


#--------------------------------------------------#
#-------------- read .json files ------------------#
#--------------------------------------------------#

library("jsonlite")

# Read json file into a json_text object using fromJSON()
books_json_text <- fromJSON("data_chap_10/demo_data/books.json")

head(books_json_text)
print(class(books_json_text)) # "list" (not dataframe)


# convert the json_text object into dataframe using as.data.frame()
df_books <- as.data.frame(books_json_text)

head(df_books)
print(class(df_books))


# use books_json_text$Mathematics$book to remove the unnecessary prefix "Mathematics.book." from the column name
df_books <- as.data.frame(books_json_text$Mathematics$book)

head(df_books)
print(class(df_books))