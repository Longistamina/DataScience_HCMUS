'''
seek() để  dời con trỏ đến vị trí nhất định, đánh dấu bằng byte

vd: seek(8,0) dời con trỏ đi 8 byte, vị trí bắt đầu dời là index = 0 (đầu văn bản)
    seek(5,3) dời con trỏ đi 5 byte, vị trí bắt đầu dời tại index = 3 (vị trí thứ 4 trong văn bản)
'''
print()
txtName = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project Txt/DuLieu-txt/VB01.txt'

#Mở tập tin để đọc 'r'
f = open(txtName,'r',encoding='utf-8') #vì có tiếng Việt có dấu nên chọn utf-8

strND0 = f.read() #Đọc toàn bộ file rồi lưu dưới dạng str, con trỏ sẽ nằm ở cuối văn bản

f.seek(0)         #Dời con trỏ về đầu văn bản

strND1 = f.read(5) #Đọc nội dung trong 5 byte đầu tiên

f.seek(5,0)        #Dời con trỏ từ đầu xuống 5 byte tiếp theo

strND2 = f.read(6) #Đọc tiếp 6 byte tiếp theo từ vị trí con trỏ trở đi sau khi dời

f.close() #Đóng tập tin lại

print(strND0) #Hello, this is file VB01.txt
print(strND1) #Hello
print(strND2) #, this

#f.tell() cho biết vị trí hiện hành của con trỏ