'''
Xét điểm trung bình:
0-3.5: kém
3.5-5: yếu
5-6.5: trung bình
6.5-8: khá
8-10: giỏi
'''
print()
print('XÉT ĐIỂM TRUNG BÌNH HỌC TẬP')
print('-'*60)


try:
    diemtb=float(input("Nhập điểm trung bình: "))
    assert diemtb >=0 and diemtb <= 10 #Đặt ra điều kiện mà nếu không thoả sẽ bị xem là lỗi

except ValueError: 
    k = True
    while k == True:
        try:
            diemtb=float(input('>>>Lỗi: Điểm trung bình phải là số, mời nhập lại: '))
            assert diemtb >=0 and diemtb <= 10
        except ValueError:
            k = True
        except AssertionError:
            l = True
            while l == True:
                try:
                    diemtb=float(input('>>>Lỗi: Điểm trung bình phải nằm giữa 0 và 10, mời nhập lại: '))
                    assert diemtb >=0 and diemtb <= 10
                except ValueError:
                    l = False
                except AssertionError:
                    l = True
                else:
                    l = False
                    k = False
        else:
            k = False

except AssertionError:
    k = True
    while k == True:
        try:
            diemtb=float(input('>>>Lỗi: Điểm trung bình phải nằm giữa 0 và 10, mời nhập lại: '))
            assert diemtb >=0 and diemtb <= 10
        except AssertionError:
            k = True
        except ValueError:
            l = True
            while l == True:
                try:
                    diemtb=float(input('>>>Lỗi: Điểm trung bình phải là số, mời nhập lại: '))
                    assert diemtb >=0 and diemtb <= 10
                except ValueError:
                    l = True
                except AssertionError:
                    l = False
                else:
                    l = False
                    k = False
        else:
            k = False

 
if diemtb >= 8:
    print('Xếp loại giỏi.')
elif diemtb >= 6.5:
    print('Xếp loại khá.')
elif diemtb >= 5:
    print('Xếp loại trung bình.')
elif diemtb >= 3.5:
    print('Xếp loại yếu.')
else:
    print('Xếp loại kém.')

print()