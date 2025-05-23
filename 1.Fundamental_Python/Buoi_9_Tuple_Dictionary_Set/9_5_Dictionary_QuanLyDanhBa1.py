'''
Tạo danh bạ chứa {'Johnny': '0989741258', 'Katherine':'0903852147', 'Misu': '0913753951', 'Jack' : '0933753654'}
Các lựa chọn: 1-Xem danh bạ, 2-Tra cứu thông tin, 3-Thêm thông tin, 4-Kết thúc
'''
print()
print('CHƯƠNG TRÌNH QUẢN LÝ DANH BẠ DANH BẠ'.center(50))
print('-'*50)
print('''Các lựa chọn:
      1-Xem danh bạ 
      2-Tra cứu thông tin 
      3-Thêm thông tin 
      4-Kết thúc ''')

danhBa = {'Johnny': '0989741258', 'Katherine':'0903852147', 'Misu': '0913753951', 'Jack' : '0933753654'}

while True:
    choice = input('\nMời bạn nhập lựa chọn: ')
    
    if choice == '1':
        print('XEM DANH BẠ'.center(50))
        print('Tên'.ljust(34),'SĐT'.ljust(15))
        print('-'*50)
        for ten,sdt in danhBa.items():
            print(f'{ten:34} {sdt:15}')
    
    elif choice == '2':
        print('TRA CỨU THÔNG TIN'.center(50))
        print('-'*50)
        traCuu = input('Mời bạn nhập thông tin cần tra cứu (tên hoặc SĐT): ').strip().title()
        if traCuu in danhBa.keys() or traCuu in danhBa.values():
            for ten,sdt in danhBa.items():
                if traCuu == ten: print(f'Kết quả: {ten} - {sdt}')
                elif traCuu == sdt: print(f'Kết quả: {ten} - {sdt}')
                else: continue
        else: print('Thông tin nhập vào không tồn tại trong danh bạ')
        
    elif choice == '3':
        print('CẬP NHẬT THÔNG TIN'.center(50))
        print('-'*50)
        ten = input('Mời bạn nhập tên mới: ').strip().title()
        sdt = input('Mời bạn nhập sdt cho tên trên: ')
        if sdt in danhBa: 
            print('Số này đã tồn tại trong danh bạ.')
        else: 
            danhBa[ten] = sdt
            print('Thêm thành công!')
    
    elif choice == '4':
        print('--Kết thúc--')
        break
    
    else: print('>>>Lỗi: lựa chọn này khôn tồn tại.')