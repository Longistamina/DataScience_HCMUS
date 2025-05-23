'''
Yêu cầu nhập ngày sinh,  trả về  thứ trong tuần.
'''

from datetime import datetime

while True:
    try:
        ngaySinh = datetime.strptime(input('\nMời nhập ngày sinh của bạn theo cú pháp dd/mm/yyyy: '),'%d/%m/%Y')
    except Exception:
        print('''>>>Lỗi: dữ liệu nhập vào không hợp lệ.
        +Cú pháp phải là dd/mm/yyyy, ví dụ: 19/05/1890
        +Ngày phải từ 1 đến 30 hoặc 31 tuỳ tháng. 
        +Riêng đối với tháng 2 thì ngày tối đa là 28 hoặc 29, nếu là 29 phải đảm bảo đúng năm nhuận.
        +Tháng phải từ 1 đến 12.
        +Năm phải từ 1 đến 9999 ''')
    else:
        wday = ngaySinh.weekday()

        if wday == 0: thu = 'Thứ 2'
        elif wday == 1: thu = 'Thứ 3'
        elif wday == 2: thu = 'Thứ 4'
        elif wday == 3: thu = 'Thứ 5'
        elif wday == 4: thu = 'Thứ 6'
        elif wday == 5: thu = 'Thứ 7'
        else: thu = 'Chủ nhật'

        print(f'Ngày sinh của bạn rơi vào {thu}.')
    
    ttuc = input('\nNếu muốn tiếp tục, nhập [y], ngược lại nhập phím bất kỳ để kết thúc: ').strip().lower()
    if ttuc == 'y': continue
    else: break
print('--Kết thúc--')