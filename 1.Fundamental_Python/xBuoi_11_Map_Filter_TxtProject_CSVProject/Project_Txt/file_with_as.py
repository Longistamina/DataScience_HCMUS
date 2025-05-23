'''
with...as... Cũng tương tự import smth as smth
'''
print()
txtName = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project Txt/DuLieu-txt/ConGapNhau.txt'

#Mở tập tin để đọc 'r'
with open(txtName,'r',encoding='utf-8') as f: #vì có tiếng Việt có dấu nên chọn utf-8

    strND = f.read() #Đọc nội dung trong file rồi lưu hết vào biến strND

f.close() #Đóng tập tin lại

print(strND)