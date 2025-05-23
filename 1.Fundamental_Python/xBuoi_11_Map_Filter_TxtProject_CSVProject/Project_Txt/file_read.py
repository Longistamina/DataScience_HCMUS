'''
Python có cung cấp một số method cơ bản để làm việc với các loại tập tin

Trong python chúng được gộp chung thành file object

Đọc rồi trả về dưới dạng string
'''
print()
txtName = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project Txt/DuLieu-txt/ConGapNhau.txt'

#Mở tập tin để đọc 'r'
f = open(txtName,'r',encoding='utf-8') #vì có tiếng Việt có dấu nên chọn utf-8

strND = f.read() #Đọc nội dung trong file rồi lưu hết vào biến strND

f.close() #Đóng tập tin lại

print(strND)