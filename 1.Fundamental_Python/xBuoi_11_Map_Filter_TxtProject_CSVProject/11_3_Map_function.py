'''
map() là áp dụng một hàm nào đó cho toàn bộ phần tử trong sequence (giống tapply() trong R)
'''
print()
import math

lstN1 = [1,2,3,4,5,6]
lstN2 = [11,22,33,44,55,66]
lstNbinhphuong = list(map(lambda x: x**2,lstN1))
print(lstN1)
print(lstNbinhphuong)

lstCanB2 = list(map(math.sqrt, lstNbinhphuong))
print(lstCanB2)

#Tổng hai dãy
lstTongN1N2 = list(map(lambda n1,n2: n1+n2, lstN1,lstN2))
print()
print(lstN1)
print(lstN2)
print(lstTongN1N2)

#Chuyển các phần tử sang integer:
print()
lstStr = ['10','20','30']
lstInt = list(map(int,lstStr))
print(lstStr)
print(lstInt)

#Rút điểm ra từ danh sách học sinh
print()
lst_Hocsinh = [
    ['Lê','An',9.5],
    ['Lý','Bình',7.5],
    ['Lê','Hạnh',4.5],
    ['Trần','Tâm',10],
    ['Nguyễn','Phúc',9],
    ['Trần','Thanh',3]
]
lstDiem = list(map(lambda item: item[2],lst_Hocsinh))
sumDiem = sum(lstDiem)
print(sumDiem)