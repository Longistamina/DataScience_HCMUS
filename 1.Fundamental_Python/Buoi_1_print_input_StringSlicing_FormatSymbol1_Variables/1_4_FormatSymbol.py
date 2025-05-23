tienluong=5000 #integer (số nguyên)
heSoLuong=1.475 #float (số thực)
hoten="Trần Ngọc Dung" #character / string

strTT1="Họ tên: "+hoten +"\nTiền lương: "+str(tienluong)
print(strTT1)
print("-"*50)
strTT2="Họ tên: %s \nTiền lương: %i \nHệ số lương: %f"%(hoten,tienluong,heSoLuong)
print(strTT2)
print("-"*50)
strTT3="Họ tên: %s \nTiền lương: %i \nHệ số lương: %.2f"%(hoten,tienluong,heSoLuong)
print(strTT3)