'''
Gom các câu lệnh chức năng vào các hàm function của chương trình quản lý danh bạ (QLDB)
'''
#User-defined-function
#----------------------------------------------------------------
def xuly_xem_danhba():
    print('XEM DANH BẠ'.center(50))
    print('Tên'.ljust(34),'SĐT'.ljust(15))
    print('-'*50)
    for ten,sdt in danhBa.items():
        print(f'{ten:34} {sdt:15}')
#-----------------------------------------------------------------
def xuly_tracuu_danhba(traCuu):
    if traCuu in danhBa.keys() or traCuu in danhBa.values():
        for ten,sdt in danhBa.items():
            if traCuu == ten: kq = f'Kết quả: {ten} - {sdt}'
            elif traCuu == sdt: kq = f'Kết quả: {ten} - {sdt}'
            else: continue
    else: kq = 'Thông tin nhập vào không tồn tại trong danh bạ'
    return kq
#-----------------------------------------------------------------
def xuly_them_thongtin(ten,sdt):
    if sdt in danhBa: 
        kq='Số này đã tồn tại trong danh bạ.'
    else: 
        danhBa[ten] = sdt
        kq='Thêm thành công!'
    return kq
#-----------------------------------------------------------------
def xuly_ketthuc():
    kq = '--Kết thúc--'
    return kq
#Code của function - "__main__" module

if __name__ == '__main__':
#Nếu các câu lệnh được chạy trong trực tiếp trong file chính, tức file có source code của nó thì __name__ == __main__ sẽ True, khi đó câu lệnh dưới mới được thực thi
#Nếu chạy gián tiếp, tức import vào chương trình khác để  chạy thì __name__ == __main__ sẽ là False, và câu lệnh dưới if không được thực thi
    
    danhBa = {'Johnny': '0989741258', 'Katherine':'0903852147', 'Misu': '0913753951', 'Jack' : '0933753654'}

    print()
    print('CHƯƠNG TRÌNH QUẢN LÝ DANH BẠ DANH BẠ'.center(50))
    print('-'*50)
    print('''Các lựa chọn:
        1-Xem danh bạ 
        2-Tra cứu thông tin 
        3-Thêm thông tin 
        4-Kết thúc ''')

    while True:
        choice = input('\nMời bạn nhập lựa chọn: ')
        
        if choice == '1':
            xuly_xem_danhba()
        
        elif choice == '2':
            print('TRA CỨU THÔNG TIN'.center(50))
            print('-'*50)
            traCuu = input('Mời bạn nhập thông tin cần tra cứu (tên hoặc SĐT): ').strip().title()
            kqtracuu = xuly_tracuu_danhba(traCuu)
            print(kqtracuu)
            
        elif choice == '3':
            print('CẬP NHẬT THÔNG TIN'.center(50))
            print('-'*50)
            ten = input('Mời bạn nhập tên mới: ').strip().title()
            sdt = input('Mời bạn nhập sdt cho tên trên: ')
            kqthem = xuly_them_thongtin(ten,sdt)
            print(kqthem)

        elif choice == '4':
            kqketthuc = xuly_ketthuc()
            print(kqketthuc)
            break
        
        else: print('>>>Lỗi: lựa chọn này khôn tồn tại.')
#print()