'''
append 1 row = writerow in mode 'a'
'''
print()
import csv 
maSo = input('Nhập mã số cần thêm: ')
ho = input('Nhập họ cần thêm: ')
ten = input('Nhập tên cần thêm: ')
sdt = input('Nhập sdt cần thêm: ')
#----------------------Thêm nội dung, mode = 'a'----------------#
pathName = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project csv/DuLieu-csv'

with open(f'{pathName}/dssv.csv','a',encoding='utf-8-sig',newline='') as f:
    lstThongtin = [maSo, ho, ten, sdt]      
    csv.writer(f).writerow(lstThongtin)
print('--kết thúc demo thêm nội dung mới vào file cũ--')

#