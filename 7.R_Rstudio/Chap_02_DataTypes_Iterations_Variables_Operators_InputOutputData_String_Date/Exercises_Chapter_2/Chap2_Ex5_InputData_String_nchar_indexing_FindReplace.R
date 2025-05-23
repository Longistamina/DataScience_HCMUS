str1 <- readline(prompt = "Input string 1: ")
str2 <- readline(prompt = "Input string 2: ")
str3 <- readline(prompt = "Input string 3: ")
index_substr <- as.numeric(readline(prompt = "Input the index of substring: "))
target_str <- readline(prompt = "Input target string: ")
replace_str <- readline(prompt = "Input replace string: ")

if (target_str == ""){
  target_str <- " "
}

str4 <- substr(str1, start = index_substr, stop = nchar(str1))
str5 <- substr(str1, start = 1, stop = index_substr)
str_new <- chartr(target_str, replace_str, str1)

cat(
  'Length of str1 "', str1, '": ', nchar(str1), '\n',
  'Length of str2 "', str2, '": ', nchar(str2), '\n',
  'Length of str3 "', str3, '": ', nchar(str3), '\n',
  'str4 = str1 from index ', index_substr, ' to ', nchar(str1),'-end: "', str4, '"', '\n',
  'str5 = str1 from index 1-first to ', index_substr, ': "', str5, '"', '\n',
  'str_new = str1 from replacing "', target_str, '" with "', replace_str, '": "', str_new, '"', '\n',
  sep = ''
)

