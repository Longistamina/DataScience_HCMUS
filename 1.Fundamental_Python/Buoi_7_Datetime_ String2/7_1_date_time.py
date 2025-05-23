#https://www.programiz.com/python-programming/datetime
#-----------------------------------------------------------------#
from datetime import datetime #Từ module datetime, ta import class datetime vào để dùng
from datetime import date
#-----------------------------------------------------------------#
print()
print(datetime.now()) #Thời điểm hiện hành
print(datetime.today()) #Ngày hiện hành
hienhanh1 = datetime.now()
hienhanh2 = datetime.today()

ngayhienhanh = hienhanh1.day     #Trích xuất ngày
thang = hienhanh1.month          #Trích xuất tháng
nam = hienhanh1.year             #Trích xuất năm

#max: datetime.datetime(9999, 12, 31, 23, 59, 59, 999999) giá trị datetime lớn nhất của python.
#là năm 9999, tháng 12, ngày 31 lúc 23h 59 phút 59 giây 999999 mili giây

#min: datetime.datetime(1, 1, 1, 0, 0) giá trị datetime nhỏ nhất của python.
#là năm 1, tháng 1, ngày 1 lúc 0 giờ, 0 phút 0 giây

print()

#-------------------------------------------#
ngaysinh1 = date(1890,5,19)             #Khởi tạo biểu thức datetime, năm 1890 tháng 5 ngày 19
ngaysinh2 = datetime(1890,5,19,23,30)   #Như trên, nhưng bổ  sung thêm giờ và phút
#Lưu ý: nếu gõ datetime.date() hoặc datetime.datetime() thì sẽ bị lỗi vì đó là hàm khác

#-----Khởi tạo biểu thức datetime từ một chuỗi nào đó theo mẫu định dạng------#
ngay1 = datetime.strptime('18/2/2024','%d/%m/%Y') # datetime.datetime(2024, 2, 18, 0, 0)
ngay2 = datetime.strptime('18-2-2024','%d-%m-%Y') # datetime.datetime(2024, 2, 18, 0, 0)
ngay3 = datetime.strptime('2/18/2024','%m/%d/%Y') # datetime.datetime(2024, 2, 18, 0, 0)
print()

#----Chuyển biểu thức datetime sang chuỗi, ngược với strptime()---------------#
ngay4 = ngay1.strftime('%d-%m-%Y')    #  '18-02-2024'
ngay5 = ngay2.strftime('%A %d/%m/%Y') #  'Sunday 18/02/2024' Dữ liệu trả về dạng chuỗi
ngay6 = ngay3.strftime('%a %m/%d/%Y') #  'Sun 02/18/2024'
print()

#-------------------------------#
thu = ngay1.strftime('%A') #Cho biết thứ trong tuần, trả về dạng chuỗi là 'Sunday'
ithu = ngay1.weekday() #Cho biết thứ trong ngày dưới dạng chỉ số, trả về  6 = Sunday
#(0: Monday, 1: Tuesday,....., 6: Sunday)

