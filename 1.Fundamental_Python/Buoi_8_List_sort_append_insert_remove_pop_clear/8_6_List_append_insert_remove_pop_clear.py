lst_int = [213,321,56198,65489,213]

#Thêm phần tử mới vào cuối list
lst_int.append(11)

#Chèn phần tử mới vào vị trí theo index
lst_int.insert(3,25) #Chèn phần tử mới có giá trị 25 vào vị trí có index = 2 trong list

#Gán lại giá trị mới cho phần tử nào đó, loại bỏ giấ trị cũ
lst_int[0] = 1 
print()

#Xoá theo index
lst_Weekdays = ['Thứ 2','Thứ 3','Thứ 4','Thứ 5','Thứ 6','Thứ 7','Chủ nhật']

del(lst_Weekdays[2]) #Xoá phần tử có index = 2 ['Thứ 2','Thứ 3','Thứ 5','Thứ 6','Thứ 7','Chủ nhật']
del(lst_Weekdays[1:4]) #Xoá phần tử  từ index = 2 đến index = 4-1 = 3 ['Thứ 2','Thứ 7','Chủ nhật']
print()

#Xoá theo giá trị phần tử
giatriXoa = 'Thứ 2'
lst_Weekdays.remove(giatriXoa) # ['Thứ 7','Chủ nhật']

lstM = [1,30,5,7,30,9]
lstM.remove(30) #Xoá phần tử  đầu tiên khớp giá trị 30
print()

#Xoá toàn bộ list
lstM.clear() #Trả về list trống [], vẫn còn id trong bộ nhớ
del(lstM)    #Xoá luôn list khỏi bộ nhớ, không còn id
print()

#Lấy phần tử ra khỏi list và gán cho biến khác
hoten = ['Ngô','Bình','Thảo','Nghi']
ho = hoten.pop(0)   #Lấy phần tử  đầu tiên là 'Ngô' ra khỏi list, rồi gán cho biến ho
ten = hoten.pop()   #Lấy phần tử  cuối cùng là 'Nghi' ra khỏi list, rồi gán cho biến ten
#giá trị bị .pop() ra thì sẽ không còn nằm trong list nữa
tenlot = ' '.join(hoten) #Ghép hai phần tử còn lại là 'Bình' và 'Thảo' thành 1 string, phân cách bởi ' '
print()