library("tidyverse")

obesity_path = "/home/longdpt/Documents/Academic/DataScience_HCMUS/7.R_Rstudio/Chap_08_DataFrame_Tidyverse/data_chap_08/Obesity_data.csv"

obesity = read_csv(obesity_path, show_col_types = FALSE)

print(head(obesity, n = 10))

############### data1 storing: id gender height weight bmi age

data1 = obesity %>%
    select(c(id, gender, height, weight, bmi, weight, age))

print(head(data1))


############## data2 = data1 with bmi >= 18.5 and <= 24.9

data2 = data1 %>%
    filter(bmi >= 18.5, bmi <= 24.9)

print(head(data2))

print(nrow(data2))


############# data1: new column height_m = height / 100
############# data1: ascending by bmi 
data1 = data1 %>%
    mutate(height_m = height / 100) %>%
    arrange(bmi)

print(head(data1))


############ data1: groupby gender, calculate mean height and mean weight
print(data1 %>%
    group_by(gender) %>%
    summarize(
        mean_height = mean(height, na.rm = T),
        mean_weight = mean(weight, na.rm = T)
    ))


############ data1: count the gender and age
gender_count = data1 %>%
    count(gender)
print(gender_count)

age_count = data1 %>%
    count(age)
print(age_count)



########### data3: 10 samples from data1
data3 = data1 %>%
    sample_n(10)

print(data3)



########### data4: 2% samples from data1
data4 = data1 %>%
    sample_frac(0.02)

print(data4)