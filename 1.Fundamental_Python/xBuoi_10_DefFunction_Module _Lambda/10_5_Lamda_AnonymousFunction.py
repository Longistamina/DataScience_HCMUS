'''
Anonymous Function (hay lambda) là hàm ẩn danh vì nó không được khai báo theo tiêu chuẩn bằng từ khoá def,
thay vào đó được viết ngắn gọn bằng cách sử dụng từ khoá lambda để tạo ra các function ngắn, hoặc method ngắn,
chỉ trong một dòng lệnh

lambda có thể có nhiều tham số để truyền vào, nhưng chỉ trả về  MỘT KẾT QUẢ duy nhất

lambda không thể chứa nhiều command hoặc expression

lambda không thể được gọi trực tiếp để  print kết quả vì nó yêu cầu một expression, tức không dùng print để in kết quả của lambda được

lambda có local namspace của nó và không thể  truy cập các biến khác và cả các biến trong phạm vi global namespace
'''
import math

#ví dụ: tính s = (x*x + 1)^n
s = lambda x,n: math.pow(math.pow(x,2)+1,n)
print('\ns =',s(2,3))

#Ví dụ tính x^2
bp = lambda x: x**2
x = 3
print(f'{x}^2 =',bp(x))

#vd tổng x+y
tongxy = lambda x,y: x+y
sum = tongxy(2,9)
print(sum)

#check số  chẵn
laSochan = lambda x: x%2 == 0
check4 = laSochan(4) #True
check5 = laSochan(5) #False

print()