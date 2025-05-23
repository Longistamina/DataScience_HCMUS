'''
Set {} là một tập hợp nhiều phần tử.
Mỗi phần tử trong set là DUY NHẤT, tức không trùng nhau
Các phần tử  có VALUE KHÔNG ĐỔI
Các phần tử không theo thứ tự thêm vào, không có index
'''
print()
#Tạo lập + chỉnh sửa  set:
set_nums = {1,5,3,8,9}
print(set_nums) # {1, 3, 5, 8, 9}

set_5hanh = {'Kim','Mộc','Thuỷ','Hoả','Thổ'}
print(set_5hanh) #{'Kim', 'Mộc', 'Hoả', 'Thuỷ', 'Thổ'}, thứ tự là ngẫu nhiên không như thứ tự ban đầu

set_fruits = set() #Tạo set rỗng, không dùng set_fruits = {} vì sẽ gây hiểu nhầm là dictionary
set_fruits.add('orange') #Thêm phần tử mới vào

set_fruits.discard('Thuỷ') #Xoá phần tử , không báo lỗi nếu không có phần tử  này trong set
set_fruits.remove('orange') #Xoá phần tử nhưng sẽ báo KeyError nếu set không chứa phần tử này

'Kim' in set_5hanh #True
'Kim' in set_fruits #False

set_fruits.clear() #Xoá các phần tử , trả lại set trống
del(set_fruits)    #Xoá set ra khỏi bộ nhớ, không còn id, không còn set trống

#Lấy element ra khỏi set:
set_fruits = {'orange','apple','grape','strawberry',',mango'}
fruit1 = set_fruits.pop() #Lấy phần tử bất kỳ trong set ra rồi gán vào fruit1, set mất phần tử đó

#len() max() min() sum()
print('\nlen:',len(set_nums))
print('max:',max(set_nums))
print('min:',min(set_nums))
print('sum:',sum(set_nums))

#copy()
set_nums2 = set_nums.copy()
print('\nset_nums2:',set_nums2)

#Các phép toán tập hợp với set:
setA = {1,2,6,3,7}
setB = {1,4,5,8,9}
print('\nsetA =',setA)
print('setB =',setB)

setC = setA | setB #Toán hội (union), gộp setA và setB thành setC, các element trùng chỉ được gộp thành một
print('\nsetC = setA | setB =',setC) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

setD = setA & setB #Toán giao (intersection), lấy ra phần tử chung giữa các set
print('\nsetD = setA & setB =',setD) #{1}

setE = setA - setB #Toán trừ (difference), lấy ra những phần tử  setA có mà setB không có
print('\nsetE = setA - setB =',setE) #{2, 3, 6, 7}

setF = setA ^ setB #Symmetric difference: ngược với Intersection, trả về các element chỉ xuất hiện ở 1 trong các set
print('\nsetF = setA ^ setB =',setF) #{2, 3, 4, 5, 6, 7, 8, 9}

#Sắp xếp, Kết quả trả về  là một list khác, không thay đổi set cũ
setTen = {'Bình','An','Danh','Tâm'}
lstTenAsc = sorted(setTen) #Tăng, ['An', 'Bình', 'Danh', 'Tâm'] 
lstTenDsc = sorted(setTen,reverse=True) #Giảm, ['Tâm', 'Danh', 'Bình', 'An']

#Chuyển đổi list <-> set: riêng hướng từ list -> set sẽ làm mất các giá trị trùng lắp
lstTen = list(setTen)
setTen = set(lstTen)

lstSN = [1,40,5,40,8,(3,4),5,(3,4)] 
setSN = set(lstSN) #{1, 5, (3, 4), 40, 8} các element trùng lắp bị mất, nhập thành một item duy nhất

#set <-> tuple
tupTen = list(setTen)
setTen = set(tupTen)


print()