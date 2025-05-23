lst_Hocsinh = [
    ['Lê','An',9.5],
    ['Lý','Bình',7.5],
    ['Lê','Hạnh',4.5],
    ['Trần','Tâm',10],
    ['Nguyễn','Phúc',9],
    ['Trần','Thanh',3]
]

#Trích ra hai danh sách học sinh đậu (>= 5.0) và rớt, rồi in hai danh sách ra màn hình + thống kê
lstDau = []
lstRot = []

for item in lst_Hocsinh:
    if item[2] >= 5: lstDau.append(item)
    else: lstRot.append(item)

print()
print('-'*42)
print('DANH SÁCH HỌC SINH ĐẬU'.center(42))
print()
print('STT'.center(5),'Họ và tên'.ljust(25),'Điểm'.rjust(10))
idau = 1
for ho,ten,diem in lstDau:
    strHoten = f'{ho} {ten}'
    strEnd = f'{str(idau).center(5)} {strHoten:25} {diem:10}'
    print(strEnd)
    idau += 1
print('\nSố  học sinh đậu:',idau-1)

print()
print('-'*42)
print('DANH SÁCH HỌC SINH RỚT'.center(42))
print()
print('STT'.center(5),'Họ và tên'.ljust(25),'Điểm'.rjust(10))
irot = 1
for ho,ten,diem in lstRot:
    strHoten = f'{ho} {ten}'
    strEnd = f'{str(irot).center(5)} {strHoten:25} {diem:10}'
    print(strEnd)
    irot += 1
print('\nSố  học sinh rớt:',irot-1)

#Sắp xếp tăng dần theo điểm số  (điểm số là item[2]):
lstDiemTang = sorted(lst_Hocsinh,key=lambda item: item[2])
lst_Hocsinh.sort(key=lambda item: item[2])

#Sắp xếp giảm dần theo điểm:
lstDiemGiam = sorted(lst_Hocsinh,key=lambda item: item[2],reverse=True)
lst_Hocsinh.sort(key=lambda item: item[2],reverse=True)

print()