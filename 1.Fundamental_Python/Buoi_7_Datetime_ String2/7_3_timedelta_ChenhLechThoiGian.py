from datetime import date,datetime,timedelta
print()
#Tính chênh lệch theo ngày và giây
day1 = datetime(2018,6,18,7,30,00)
day2 = datetime(2019,7,20,8,32,20)

t1 = day2-day1 #Chênh lệch thời gian - timedelta()
print(t1)
soNgayChenhLech = t1.days
soGiayChenhLech = t1.seconds

#Demo cho timedelta():
ngayMai = date.today() + timedelta(days=1)
ngayHomQua1 = date.today() + timedelta(days=-1)
ngayHomQua2 = date.today() - timedelta(days=1)

t = timedelta(days=5,hours=1,minutes=10,seconds=30)
tongSoGiay = t.total_seconds() #Quy đổi hết sự chênh lệch thời gian về đại lượng giây = 436230 giây

print()
