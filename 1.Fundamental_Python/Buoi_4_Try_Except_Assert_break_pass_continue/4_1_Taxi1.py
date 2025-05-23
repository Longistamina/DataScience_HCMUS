print('\n Chương trình tính tiền taxi 1')
print('-'*80)
loaiXe = input('Loại xe bạn đi là (7 hoặc 4): ')
soKm = float(input('Số km xe di chuyển là: '))
tgCho = int(input('Thời gian chờ là: '))

if loaiXe == '4':
    dgMocua = 11000
    dgDuoi30 = 15300
    dgTren30 = 12100
else: # 7 chỗ
    dgMocua = 12000
    dgDuoi30 = 16100
    dgTren30 = 13800

#-------Tính tiền di chuyển-----------#
if soKm <= 0.8:
    phiDichuyen = dgMocua
elif soKm <= 30:
    phiDichuyen = dgMocua + (soKm-0.8)*dgDuoi30
else: #soKm > 30
    phiDichuyen = dgMocua + (30-0.8)*dgDuoi30 + (soKm-30)*dgTren30

#------Tính tiền chờ----------------#
phiCho = 0
if tgCho > 5: phiCho = (tgCho - 5)*750

#-------Phí tổng-------------#
phiTaxi = phiDichuyen + phiCho

#--------Kết quả--------------#
print('-'*80)
print(f'Phí di chuyển: {phiDichuyen:,} VND')
print(f'Phí chờ: {phiCho:,} VND')
print(f'Tổng phí: {phiTaxi:,} VND')
