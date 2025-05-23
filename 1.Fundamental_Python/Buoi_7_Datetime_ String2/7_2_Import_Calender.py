import calendar
print()

#Kiểm tra năm nhuận
laNamNhuan1 = calendar.isleap(2000) #True
laNamNhuan2 = calendar.isleap(1999) #False

tuple_MR = calendar.monthrange(2019,11)
#Kết quả trả về  là một tuple (4,30)
# 4 là .weeday() hay thứ của ngày đầu tiên của tháng, tức ngày 1/11/2019 rơi vào thứ 6
# 30 là tháng 11 có 30 ngày

#Số ngày trong tháng
soNgayTrongThang1 = calendar.monthrange(2019,11)[1] #Lấy phần tử thứ 2 trong tuple MR, là số ngày trong tháng = 30
soNgayTrongThang2 = tuple_MR[1] #=> 30

#Chỉ số  thứ (weekday) của ngày đầu tiên
chiSoThu1 = calendar.monthrange(2019,11)[0]
chiSoThu2 = tuple_MR[0]

#Lấy cả hai thông số trên:
chiSoThu,soNgayTrongThang = calendar.monthrange(2020,8)
#chiSoThu = calendar.monthrange(2020,8)[0]
#soNgayTrongThang = calendar.monthrange(2020,8)[1]

#Lịch tháng
lichThang11nam2019 = calendar.monthcalendar(2019,11)
print(lichThang11nam2019)
#[[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 0]]
#[[0, 0, 0, 0, 1, 2, 3], tuần 1, đi từ Thứ 2 -> CN
#[4, 5, 6, 7, 8, 9, 10], tuần 2
#[11, 12, 13, 14, 15, 16, 17], tuần 3
#[18, 19, 20, 21, 22, 23, 24], tuần 4
#[25, 26, 27, 28, 29, 30, 0]]  tuần 5
print()