print()

#Two dimensional lists:
lst_Khachhang = [
    ['Lê','An',2000],
    ['Lê','Thanh Bình',300000],
    ['Lý','Hồng Phúc',500000000]
]

# Cách 1
for item in lst_Khachhang:
    ho = item[0]
    ten = item[1]
    print(f'{ho} {ten}')

#Cách 2:
print()
for ho,ten,tien in lst_Khachhang:
    print(f'{ho} {ten}: {tien} VND')

#Kiểu cách:
print()
print('DANH SÁCH KHÁCH HÀNG'.center(42))
print('-'*42)
print('STT'.center(5),'Họ tên'.ljust(25),'Số  tiền'.rjust(10))
print('-'*42)
tongTien = 0
i = 1
for ho,ten,tien in lst_Khachhang:
    strHoten = f'{ho} {ten}'
    strEnd = f'{str(i).center(5)} {strHoten:25} {tien:10,}'
    print(strEnd)
    i += 1
    tongTien += tien
print('-'*42)
print(f'Tổng số  tiền: {tongTien:,} VND')

#Nhập thông tin vào list:
ho = input('Nhập họ: ')
ten = input('Nhập tên: ')
soTien = int(input('Nhập số  tiền: '))
khachHangmoi = [ho,ten,soTien]

lst_Khachhang = append(khachHangmoi)