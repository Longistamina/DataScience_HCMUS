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

diemtb=float(input("Nhập điểm trung bình: "))

while diemtb < 0 or diemtb > 10:
    diemtb=float(input('Điểm trung bình phải nằm giữa 0 và 10, mời nhập lại: '))

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