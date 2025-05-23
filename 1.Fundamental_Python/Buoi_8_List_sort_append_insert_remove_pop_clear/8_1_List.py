'''
List là một dạng tập hợp trong python, gồm nhiều phần tử.
Mỗi phần tử  của List có thể  CÙNG HOẶC KHÁC kiểu dữ liệu. Nếu cùng kiểu dữ liệu thì dễ  xử  lý hơn.
Các phần tử  phân cách nhau bằng dấu phẩy ,

Phần tử  đầu tiên có index = 0
Phần tử  cuối cùng index = số  phần tử  - 1
(vd list có 4 phần tử  thì ptử  cuối cùng có index = 4 - 1 = 3)
'''
print()

#Khởi tạo list rỗng:
list1 = list()
list2 = []
print()

#Khởi tạo list với các giá trị mặc định:
lst_int = [213,321,56198,65489,213]
lst_Thongtin = ['001','Ling Xiaoyu',True,1.65,22]
print(lst_Thongtin)
print()

#Trích xuất phần tử của list thông qua index
pt1 = lst_Thongtin[0] # '001'
pt2 = lst_Thongtin[1] # 'Ling Xiaoyu'
ptCuoi = lst_Thongtin[-1] # 22    (= lst_Thongtin[4])
print()

#Trích xuất nhiều dữ liệu hơn:
lst_Weekdays = ['Thứ 2','Thứ 3','Thứ 4','Thứ 5','Thứ 6','Thứ 7','Chủ nhật']
lst_Ngaylam = lst_Weekdays[0:5] #Stop ở index = 5 nhưng không lấy phần tử đó, tức không lấy 'Thứ 7'
lst_Ngaynghi =lst_Weekdays[5:]  #Start ở index = 5, tức lấy phần tử  đó luôn cho đến phần còn lại
print()

#Nếu các phần tử  trong list ở dạng số :
soPhanTuList = len(lst_int)
sumList = sum(lst_int)
maxList = max(lst_int)
minList = min(lst_int)
soLanXuatHien = lst_int.count(213) #Đếm xem giá trị 213 xuất hiện bao nhiêu lần trong list
print()

#Các phép toán với list
lst1 = [1,3,5]
lst2 = [2,4,6,8]
lst3 = ['A','B','C']

lstCong = lst1 + lst2 # [1,3,5,2,4,6,8] tạo ra list mới, id mới chứa kết quả

lstNhan = lst1*3 # [1,3,5,1,3,5,1,3,5]  tạo ra list mới, id mới chứa kết quả

lst3.extend(lst1) # ['A','B','C',1,3,5] thêm phần tử  lst1 vào lst3, không tạo ra id mới, chỉ ghi đè lên
#lst3 += lst1 cũng cho ra kết quả tương đương

print()

#Kiểm tra xem giá trị đó có trong list không:
k1 = 213 in lst_int # True
k2 = 5 in lst_int #False

#Tìm index của giá trị đã biết trong list
i1 = lstNhan.index(5) #Trả về  index = 2, là index của giá trị 5 đầu tiên trong list
i2 = lstNhan.index(5,i1+1) #Bắt đầu dò tìm từ vị trí i1+1, trả về  index = 5
#Nếu trong list không có giá trị đó thì sẽ báo lỗi ValueError
print()

#Sắp xếp
lstA = [6,2,8,7,1,5,3,4,9]
lstB = [6,2,8,7,1,5,3,4,9]

lstA.sort()             #Sắp xếp tăng [1,2,3,4,5,6,7,8,9] làm thay đổi lstA
lstB.sort(reverse=True) #Sắp xếp giảm [9,8,7,6,5,4,3,2,1] làm thay đổi lstB

lstC = ['a','b','c']
lstC.reverse() # ['c','b','a'] Chỉ đảo ngược trình tự ban đầu chứ không sắp xếp

print()

#Tham chiếu đến bộ nhớ (reference type)
lst_rf1 = [6,2,8,7,1,5,3,4,9]
lst_rf2 = lst_rf1 #Lúc này, lst_rf2 sẽ có cùng id bộ nhớ với lst_rf1, vì python sẽ truy cập vào id bộ nhớ của lst_rf1 để tham chiếu và khởi tạo lst_rf2
lst_rf3 = lst_rf1.copy() #Python khởi tạo list mới là lst_rf3 với id lưu trữ khác với lst_rf1

lst_rf2[2] = 300 #Vì lst_rf2 và lst_rf1 share cùng 1 id nên khi điều chỉnh lst_rf2 thì lst_rf1 cũng sẽ thay đổi
#do đến nên dùng .copy() để  khởi tạo lst khác với id khác, để  tránh dữ liệu list gốc bị thay đổi

print()