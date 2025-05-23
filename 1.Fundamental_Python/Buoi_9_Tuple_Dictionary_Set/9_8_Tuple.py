''' Tuple ()
Là dạng tập hợp chứa nhiều phần tử, mỗi phần tử  có value và index.
Tuple cố  định số  phần tử , không cho phép thêm sửa xoá, thay đổi thứ tự như list (Read-only)
Các phần tử  phải có cùng kiểu dữ liệu

Các method khác tuple đều có giống list, ngoại trừ sort, reverse, remove, pop, insert, extend, append

Nên dùng tuple trong trường hợp không muốn người khác thay đổi tập dữ liệu của mình
'''

#Khởi tạo tuple:
tup1 = ('one','two','three','four')
tup2 = (1,2,3,4,5)
tup3 = 6,7,8,9,10
tup4 = 8,         #Nếu chỉ có một phần tử thì phải kết thúc bằng dấu phẩy để nó hiểu là tuple
tup5 = ('abc',)

#chuyển list thành tuple
lst_thu = ['Thứ 2','Thứ 3','Thứ 4','Thứ 5','Thứ 6','Thứ 7','Chủ nhật']
tup_thu = tuple(lst_thu)

