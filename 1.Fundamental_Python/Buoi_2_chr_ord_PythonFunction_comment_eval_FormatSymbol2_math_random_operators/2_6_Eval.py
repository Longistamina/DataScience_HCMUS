#eval() đánh giá xem chuỗi đó có thể là kiểu dữ liệu nào,
# rồi convert chuỗi thành kiểu dữ liệu đó

k1=eval('2+3+5') #---> hiểu như biểu thức, trả về kết quả = 10
k2=eval('25') #---> hiểu như số nguyên, trả về 25 dạng integer
k3=eval('1.75') #---> hiểu như số thực, trả về 1.75 dạng float
k4=eval('20,23,45') #----> hiểu như 1 tuple, convert thành tuple
k5=eval('[12,13,14,15]') #----> hiểu như 1 list, convert thành list
print()

k=eval('abc') #-->báo lỗi vì eval xem đây là biến chưa được định nghĩa
