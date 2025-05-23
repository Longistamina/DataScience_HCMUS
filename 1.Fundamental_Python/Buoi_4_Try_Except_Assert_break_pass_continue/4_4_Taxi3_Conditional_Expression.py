print('\nChương trình tính tiền taxi 3')
print('-'*80)

#----------Bắt lỗi loại xe------------------#
try:
    loaiXe = input('Loại xe bạn đi là (7 hoặc 4): ')
    assert loaiXe == '4' or loaiXe == '7'
except Exception:
    k = True
    while k == True:
        try:
            loaiXe = input('>>>Lỗi: Loại xe phải là 7 hoặc 4, mời nhập lại: ')
            assert loaiXe == '4' or loaiXe == '7'
        except Exception:
            k = True
        else: k = False

#----------Bắt lỗi số  Km------------------#
print()
try:
    soKm = float(input('Số km xe di chuyển là: '))
    assert soKm >= 0
except Exception:
    k = True
    while k == True:
        try:
            soKm = float(input('>>>Lỗi: số km xe di chuyển phải là số  thực dương, mời nhập lại: '))
            assert soKm >= 0
        except Exception:
            k = True
        else:
            k = False

#----------Bắt lỗi thời gian chờ------------------#
print()
try:
    tgCho = int(input('Thời gian chờ là: '))
    assert tgCho >= 0
except Exception:
    k = True
    while k == True:
        try:
            tgCho = int(input('>>>Lỗi: Thời gian chờ phải là số  nguyên dương, mời nhập lại: '))
            assert tgCho >= 0
        except Exception:
            k = True
        else:
            k = False

#-----------Xử  lý tính toán ----------------#
dgMocua, dgDuoi30, dgTren30 = 11000, 15300, 121000 if loaiXe == '4' else 12000, 16100, 13800

#-------Tính tiền di chuyển-----------#
# if soKm <= 0.8:
#     phiDichuyen = dgMocua
# elif soKm <= 30:
#     phiDichuyen = dgMocua + (soKm-0.8)*dgDuoi30
# else: #soKm > 30
#     phiDichuyen = dgMocua + (30-0.8)*dgDuoi30 + (soKm-30)*dgTren30
phiDichuyen = dgMocua if soKm <= 0.8 else dgMocua + (soKm-0.8)*dgDuoi30 if soKm <= 30 else dgMocua + (30-0.8)*dgDuoi30 + (soKm-30)*dgTren30 if soKm > 30

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
