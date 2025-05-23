print('\nChương trình tính tiền taxi 2')
print('-'*80)
#---------------------Bắt lỗi loại xe--------------#
try:
    loaiXe = input('Loại xe bạn đi là (7 hoặc 4): ')
    assert loaiXe == '4' or loaiXe == '7'
except AssertionError:
    k = True
    while k == True:
        try:
            loaiXe = input('>>>Lỗi: chỉ nhập loại xe là 4 hoặc 7, xin nhập lại: ')
            assert loaiXe == '4' or loaiXe == '7'
        except AssertionError:
            k = True
        else:
            k = False
else:
    pass

#----------------Bắt lỗi số  Km---------------#
print()
try:
    soKm = float(input('Số km xe di chuyển là: '))
    assert soKm >= 0
except ValueError:
    k = True
    while k == True:
        try:
            soKm = float(input('>>> Lỗi: Số km phải là số  thực dương, yêu cầu nhập lại: '))
            assert soKm >= 0
        except ValueError:
            k = True
        except AssertionError:
            l = True
            while l == True:
                try:
                    soKm = float(input('>>> Lỗi: Số km phải là số  thực dương, yêu cầu nhập lại: '))
                    assert soKm >= 0
                except AssertionError:
                    l = True
                except ValueError:
                    l = False
                    k = True
                else:
                    l = False
                    k = False
        else:
            k = False    

except AssertionError:
        k = True
        while k == True:
            try:
                soKm = float(input('>>> Lỗi: Số km phải là số  thực dương, yêu cầu nhập lại: '))
                assert soKm >= 0
            except AssertionError:
                k = True
            except ValueError:
                l = True
                while l == True:
                    try:
                        soKm = float(input('>>> Lỗi: Số km phải là số  thực dương, yêu cầu nhập lại: '))
                        assert soKm >= 0
                    except ValueError:
                        l = True
                    except AssertionError:
                        l = False
                        k = True
                    else:
                        l = False
                        k = False
            else:
                k = False

#----------------Bắt lỗi thời gian chờ---------------#
print()
try:
    tgCho = int(input('Thời gian chờ là: '))
    assert tgCho >= 0

except ValueError:
    k = True
    while k == True:
        try:
            tgCho = int(input('>>>Lỗi: Thời gian chờ phải là số nguyên dương, mời nhập lại: '))
            assert tgCho >= 0
        except ValueError:
            k = True
        except AssertionError:
            l = True
            while l == True:
                try:
                    tgCho = int(input('>>>Lỗi: Thời gian chờ phải là số nguyên dương, mời nhập lại: '))
                    assert tgCho >= 0
                except AssertionError:
                    l = True
                except ValueError:
                    l = False
                    k = True
                else:
                    l = False
                    k = False
        else:
            k = False

except AssertionError:
        k = True
        while k == True:
            try:
                tgCho = int(input('>>>Lỗi: Thời gian chờ phải là số nguyên dương, mời nhập lại: '))
                assert tgCho >= 0
            except AssertionError:
                k = True
            except ValueError:
                l = True
                while l == True:
                    try:
                        tgCho = int(input('>>>Lỗi: Thời gian chờ phải là số nguyên dương, mời nhập lại: '))
                        assert tgCho >= 0
                    except ValueError:
                        l = True
                    except AssertionError:
                        l = False
                        k = True
                    else:
                        l = False
                        k = False
            else:
                k = False
        

#--------------Xử  lý tính toán---------------#
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
