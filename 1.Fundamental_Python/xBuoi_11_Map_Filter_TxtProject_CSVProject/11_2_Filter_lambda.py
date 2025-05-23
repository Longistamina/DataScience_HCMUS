'''
filter() dùng để lọc ra các item trong một tập hợp (sequence)
Kết quả trả về là một sequence mới chứa các item thoả điều kiện mô tả trong function

filter(function,sequence) -> list(kết quả) hoặc tuple(kết quả) 

Nếu điều kiện tương đối đơn giản thì có thể dùng lambda để viết function, không cần def function()
'''
print()
#Ví dụ rút các số  chẵn từ list số nguyên
lstN = [5,7,2,8,9,12,24,5,9,2,11,12]
lstChan = list(filter(lambda x: x%2 == 0, lstN))
print(lstChan)

#Rút số chẵn ra và loại bỏ giá trị trùng: dùng set
setChan = set(filter(lambda x: x%2 == 0, lstN))
print(setChan)

#Tổng các số là bội số của 3:
sumBoi3 = sum(filter(lambda x: x%3 == 0,lstN))
print(sumBoi3)

#Lọc ra những người họ Lê:
lstTen = ['Lê Văn Minh', 'Trần Thị Hải','lê Anh Thư','Lý Quốc Hùng','Lênh Văn Út']
lsthoLe = list(filter(lambda item: item[0:3].lower() == 'lê ',lstTen)) #lấy thêm ký tự ' ' sau chữ 'lê'
print(lsthoLe)

#Lọc ra danh sách HS đậu (điểm >= 5):
lst_Hocsinh = [
    ['Lê','An',9.5],
    ['Lý','Bình',7.5],
    ['Lê','Hạnh',4.5],
    ['Trần','Tâm',10],
    ['Nguyễn','Phúc',9],
    ['Trần','Thanh',3]
]
lstDau = list(filter(lambda item: item[2] >= 5, lst_Hocsinh))
print(lstDau)

#Sắp xếp tăng dần theo điểm số
lstDiemTang = sorted(lst_Hocsinh,key=lambda item: item[2])
lst_Hocsinh.sort(key=lambda item: item[2])

#Sắp xếp giảm dần theo điểm:
lstDiemGiam = sorted(lst_Hocsinh,key=lambda item: item[2],reverse=True)
lst_Hocsinh.sort(key=lambda item: item[2],reverse=True)