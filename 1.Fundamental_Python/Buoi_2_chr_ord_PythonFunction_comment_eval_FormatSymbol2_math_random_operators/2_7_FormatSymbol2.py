#Literal String Interporation v3.6
#python.org/dev/peps/pep-0498/

tienluong=5000 #integer (số nguyên)
heSoLuong=1.475 #float (số thực)
hoten="Trần Ngọc Dung" #character / string

str1 = f'Họ tên: {hoten}\n Tiền lương: {tienluong}\n Hệ số  lương: {heSoLuong}'
print(str1)

print('-'*50)

#Thêm dấu cách nghìn (dấu phẩy cho tiền lương) và làm tròn heSoLuong 2 chữ số thập phân
str2 = f'Họ tên: {hoten}\n Tiền lương: {tienluong:,} VND\n Hệ số  lương: {heSoLuong:.2f}'
print(str2)

print('-'*50)

#Thêm dấu cách nghìn và làm tròn hai số lẻ cho tiền lương
str3 = f'Họ tên: {hoten}\n Tiền lương: {tienluong:,.2f} VND\n Hệ số  lương: {heSoLuong}'
print(str3)

