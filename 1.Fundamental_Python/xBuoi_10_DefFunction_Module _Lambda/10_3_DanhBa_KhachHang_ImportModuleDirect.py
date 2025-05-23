'''
Import module vào để  xử  lý danh bạ khách hàng
'''
import Module_QuanLyDanhBa3 as modDB
#Nếu module và file "main" cùng nằm trong một folder thì có thể  import directly được

print()
print('CHƯƠNG TRÌNH QUẢN LÝ DANH BẠ DANH BẠ KHÁCH HÀNG'.center(50))
print('-'*50)
print('''Các lựa chọn:
    1-Xem danh bạ 
    2-Tra cứu thông tin 
    3-Thêm thông tin 
    4-Kết thúc ''')

danhBaKH = {'Hoàng': '0989741258', 'Hà':'0903852147', 'Huy': '0913753951', 'Hải' : '0933753654'}

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