'''
os là module dùng để  thao tác theo kiểu quản trị hệ thống như đổi tên tập tin, xoá tập tin,...
'''
print()

pathname = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project Txt/DuLieu-txt'
import os

#Tạo mới một file test_os.text, chọn mode 'w+' để  write và read
with open(f'{pathname}/test_os.txt','w+',encoding='utf-8') as f:
    f.write('Hello, this is test_os.txt file, just to test os module')
    f.seek(0) #Dời con trỏ về đầu lại mới đọc được content, vì sau khi f.write() xong nó sẽ nằm ở cuối
              #Nếu không f.seek(0) thì f.read() sẽ chỉ đọc được string rỗng
    strND = f.read()
f.close()

print(strND)

#----------rename-------remove-----------------------#
os.rename(f'{pathname}/test_os.txt',f'{pathname}/test_os2.txt') #Đổi tên file test_os.txt thành test_os2.txt
print('The file has been renamed to test_os2.txt')

os.remove(f'{pathname}/test_os2.txt') #Xoá tập tin VB02.txt
print('The file has been deleted')

#-------------cwd, listdir---------------------------#
print()
thuMucHienHanh = os.getcwd() #cwd = current working directory, trả về đường dẫn đến cwd
lstTenTaptin = os.listdir(thuMucHienHanh) #Trả về list tên các tập tin có trong thư mục nào đó

for item in lstTenTaptin:
    print(item)
print('--In xong--')

#-------------_Xoá màn hình----------------------#
os.system('clear') #Dành cho linux và macOS
#os.system('cls') #Cho windows

print('Thử câu lệnh xoá bất kể hệ điều hành là gì')
os.system('cls' if os.name == 'nt' else 'clear') #os.name ==  'nt' => windows, chọn 'cls'
                                    #Ngược lại, os.name == 'possix' => Linux MacOs, chọn 'clear'

print('\nĐã xoá nội dung cũ')