'''
write many rows = writerows
'''
print()
import csv 

pathName = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project csv/DuLieu-csv'

lstDSHV = [
    ['MS01', 'Trần Anh', 'Tuấn', 9.5], 
    ['MS02', 'Lê Quốc', 'Anh', 9.0], 
    ['MS03', 'Trần Anh', 'Bình', 6.5], 
    ['MS04', 'Nguyễn Thúy', 'An', 7.5], 
    ['MS05', 'Trần Anh', 'Thư', 5.0], 
    ['MS06', 'Lý Thanh', 'Tâm', 3.5], 
    ['MS07', 'Trần Lê Nhất', 'Hạnh', 9.5], 
    ['MS08', 'Trần Bửu', 'Nguyên', 4.0], 
    ['MS09', 'Lê Thanh', 'Tuấn', 8.0]
]  

#----------------------Ghi thêm nhiều dòng, mode 'w'----------------#
with open(f'{pathName}/dshv.csv','w',encoding='utf-8-sig',newline='') as f: 
    csv.writer(f).writerows(lstDSHV) #Ghi từng list con trong lstDSHV ra nhiều dòng, mỗi dòng một list con

print('--kết thúc demo ghi nhiều dòng--')

