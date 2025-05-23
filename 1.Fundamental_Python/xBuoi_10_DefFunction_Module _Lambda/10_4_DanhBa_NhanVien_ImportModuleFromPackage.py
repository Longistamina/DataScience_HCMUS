'''
Import module từ một thư mục (folder, package) khác vào để sử dụng.
Tức module và file "main" không cùng nằm trong một thư mục
'''

from ModulePackages import Module_QLDanhBa as modDB  # Cách 1
import ModulePackages.Module_QLDanhBa as modDB       # Cách 2
from ModulePackages import *                         # Cách 3: cách này import hết tất cả module có trong package vào
# cách 3 sẽ không cần TenPackage.function() mà gọi thẳng function() ra dùng luôn

#ModulePackages là folder mẹ chứa file Module_QLDanhBa.py cần import vào

#from MotherFolder import module1,module2 as viettat1,viettat2 - Gọi nhiều module cùng lúc

print()
print('CHƯƠNG TRÌNH QUẢN LÝ DANH BẠ DANH BẠ NHÂN VIÊN'.center(50))
print('-'*50)
print('''Các lựa chọn:
    1-Xem danh bạ 
    2-Tra cứu thông tin 
    3-Thêm thông tin 
    4-Kết thúc ''')

danhBaKH = {'Thu': '0989741258', 'Hoài':'0903852147', 'Minh': '0913753951', 'Marcus' : '0933753654'}

while True:
    choice = input('\nMời bạn nhập lựa chọn: ')
    
    if choice == '1':
        modDB.xuly_xem_danhba(danhBaKH)
    
    elif choice == '2':
        print('TRA CỨU THÔNG TIN'.center(50))
        print('-'*50)
        traCuu = input('Mời bạn nhập thông tin cần tra cứu (tên hoặc SĐT): ').strip().title()
        kqtracuu = modDB.xuly_tracuu_danhba(traCuu,danhBaKH)
        print(kqtracuu)
        
    elif choice == '3':
        print('CẬP NHẬT THÔNG TIN'.center(50))
        print('-'*50)
        ten = input('Mời bạn nhập tên mới: ').strip().title()
        sdt = input('Mời bạn nhập sdt cho tên trên: ')
        kqthem = modDB.xuly_them_thongtin(ten,sdt,danhBaKH)
        print(kqthem)

    elif choice == '4':
        kqketthuc = modDB.xuly_ketthuc()
        print(kqketthuc)
        break
    
    else: print('>>>Lỗi: lựa chọn này khôn tồn tại.')