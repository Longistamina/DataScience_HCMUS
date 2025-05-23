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
        thuTrongngay = ['Thứ 2','Thứ 3','Thứ 4','Thứ 5','Thứ 6','Thứ 7','Chủ nhật']
        thuTiengAnh = ngaySinh.strftime('%A')
        print(f'Ngày sinh của bạn rơi vào {thuTrongngay[wday]}, tiếng Anh là {thuTiengAnh}.')
    
    ttuc = input('\nNếu muốn tiếp tục, nhập [y], ngược lại nhập phím bất kỳ để kết thúc: ').strip().lower()
    if ttuc == 'y': continue
    else: break
print('--Kết thúc--')