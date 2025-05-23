#Tạo lập dictionary từ list key và list value sẵn có
#Sử dụng hàm zip()

print()
lstMaSo = ['H01','H02','H03','H04'] 
lstDonGia = [100,200,300,400]

dicDSHH = {}

for ms,dg in zip(lstMaSo,lstDonGia):
    dicDSHH[ms] = dg
print(dicDSHH)
print()

#Nhắc lại là các key không được trùng nhau, nếu không sẽ bị lỗi giải thuật, vd như sau:
print()
lstMaSo2 = ['H01','H02','H03','H04','H01'] #Có hai key H01 trùng nhau 
lstDonGia2 = [100,200,300,400,500]

dicDSHH2 = {}

for ms,dg in zip(lstMaSo2,lstDonGia2):
    dicDSHH2[ms] = dg
print(dicDSHH2) #{'H01': 500, 'H02': 200, 'H03': 300, 'H04': 400}, giá trị 100 bị thay thế bằng 500 do trùng key
print()

#Sửa: 
print()
lstMaSo3 = ['H01','H02','H03','H04','H01'] #Có hai key H01 trùng nhau 
lstDonGia3 = [100,200,300,400,500]

dicDSHH3 = {}

for ms,dg in zip(lstMaSo2,lstDonGia2):
    if ms not in dicDSHH3: dicDSHH3[ms] = dg #kiểm tra xem key đó đã có sẵn trong dict chưa, chưa có thì mới cập nhật và thêm vào, có rồi thì bỏ qua
print(dicDSHH3) #{'H01': 100, 'H02': 200, 'H03': 300, 'H04': 400} giá trị 500 không được cập nhật cho H01
print()