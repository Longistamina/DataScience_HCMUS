print('\nChương trình tính tiền taxi 3')

while True:
    print('-'*80)

    #----------Bắt lỗi loại xe------------------#
    try:
        loaiXe = input('Loại xe bạn đi là (7 hoặc 4): ')
        assert loaiXe == '4' or loaiXe == '7'
    except Exception:
        while True:
            try:
                loaiXe = input('>>>Lỗi: Loại xe phải là 7 hoặc 4, mời nhập lại: ')
                assert loaiXe == '4' or loaiXe == '7'
            except Exception: continue #Tiếp  tục vòng lặp
            else: break # Thoát khỏi vòng lặp

    #----------Bắt lỗi số  Km------------------#
    print()
    try:
        soKm = float(input('Số km xe di chuyển là: '))
        assert soKm >= 0
    except Exception:
        while True:
            try:
                soKm = float(input('>>>Lỗi: số km xe di chuyển phải là số  thực dương, mời nhập lại: '))
                assert soKm >= 0
            except Exception: continue
            else: break

    #----------Bắt lỗi thời gian chờ------------------#
    print()
    try:
        tgCho = int(input('Thời gian chờ là: '))
        assert tgCho >= 0
    except Exception:
        while True:
            try:
                tgCho = int(input('>>>Lỗi: Thời gian chờ phải là số  nguyên dương, mời nhập lại: '))
                assert tgCho >= 0
            except Exception: continue
            else: break

    #-----------Xử  lý tính toán ----------------#
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
    print()
    print(f'Phí di chuyển: {phiDichuyen:,} VND')
    print(f'Phí chờ: {phiCho:,} VND')
    print(f'Tổng phí: {phiTaxi:,} VND')
    print()
    ketThuc = input('Nhấn phím bất kỳ để  tiếp tục, hoặc [k] để kết thúc chương trình: ').strip().lower()
    if ketThuc == 'k': break
    else: continue

'''
.strip() loại bỏ ký tự khoảng trắng ở hai đầu chuỗi

>>> ten='    avádv    '
>>> ten.strip()
'avádv'
>>> 
'''

'''
.lower() chuyển về chữ thường

>>> ten='ACVD'
>>> ten.lower()
'acvd'
'''