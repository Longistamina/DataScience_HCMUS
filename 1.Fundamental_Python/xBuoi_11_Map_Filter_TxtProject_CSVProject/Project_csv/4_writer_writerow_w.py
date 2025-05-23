'''
write 1 row = writerow
'''
print()
import csv 
pathName = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project csv/DuLieu-csv'

#----------------------Ghi một dòng, mode 'w'----------------#
with open(f'{pathName}/dssv.csv','w',encoding='utf-8-sig',newline='') as f: 
                       #Tên file chưa tồn tại nên sẽ được tạo mới, dssv.csv
                                            #newline='' tức mỗi dòng mới sẽ cách nhau một ký tự trống ''
    lstThongtin = ['MS01', 'Trần','An', '09123456789'] #list chứa thông tin cần ghi vào     
    csv.writer(f).writerow(lstThongtin) #writerow là ghi theo từng dòng
print('--kết thúc demo ghi một dòng--')

#Nếu file đã tồn tại mà để  'w' thì dữ liệu mới sẽ ghi đè lên dữ liệu cũ, mất dữ liệu cũ