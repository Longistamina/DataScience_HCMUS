lst_Hocsinh = [
    ['Lê','An',9.5],
    ['Lý','Bình',7.5],
    ['Lê','Hạnh',4.5],
    ['Trần','Tâm',10],
    ['Nguyễn','Phúc',9],
    ['Trần','Thanh',3]
]

#Trích danh sách đậu rớt bằng list comprehension
#Đậu >= 5

lstDau = [hs for hs in lst_Hocsinh if hs[2] >= 5]
lstRot = [hs for hs in lst_Hocsinh if hs[2] <5]

print(f'\n{lstDau}')
print(lstRot)

#Cách cổ điển
lstDau = []
lstRot = []

for item in lst_Hocsinh:
    if item[2] >= 5: lstDau.append(item)
    else: lstRot.append(item)